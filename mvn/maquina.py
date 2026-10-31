"""Montador absoluto e executor de um subconjunto MVN, criados nesta edição.

Não substituem a validação no simulador oficial da disciplina.
"""
from dataclasses import dataclass,field
from pathlib import Path
import re

OPS={'JP':0,'JZ':1,'JN':2,'LV':3,'+':4,'-':5,'*':6,'/':7,'LD':8,'MM':9,'SC':10,'RS':11,'HM':12,'GD':13,'PD':14}

def montar(arquivos):
    registros=[];simbolos={};pc=0;ocupados=set()
    for arquivo in arquivos:
        for numero,linha in enumerate(Path(arquivo).read_text().splitlines(),1):
            partes=linha.split(';',1)[0].split()
            if not partes:continue
            if partes[0]=='@':
                if len(partes)!=2:raise ValueError('Diretiva de origem inválida')
                pc=int(partes[1].removeprefix('/'),16);continue
            if partes[0] not in OPS and partes[0]!='K':
                label=partes.pop(0)
                if label in simbolos:raise ValueError('Símbolo duplicado: '+label)
                simbolos[label]=pc
            if len(partes)!=2 or (partes[0] not in OPS and partes[0]!='K'):raise ValueError(f'{arquivo}:{numero}: sintaxe inválida')
            if pc%2 or not 0<=pc<=4094 or pc in ocupados:raise ValueError('Sobreposição/endereço inválido')
            ocupados.add(pc);registros.append((pc,*partes));pc+=2
    memoria=bytearray(4096)
    for endereco,op,arg in registros:
        valor=int(arg[1:],16) if arg.startswith('/') else simbolos.get(arg)
        if valor is None:raise ValueError('Símbolo não definido: '+arg)
        if op=='K':
            if not 0<=valor<65536:raise ValueError('Palavra fora de 16 bits')
            word=valor
        else:
            if not 0<=valor<4096:raise ValueError('Operando fora de 12 bits')
            word=(OPS[op]<<12)|valor
        memoria[endereco:endereco+2]=word.to_bytes(2,'big')
    return memoria,simbolos

def assinado(word):return word-65536 if word&0x8000 else word

@dataclass
class Maquina:
    memoria:bytearray
    entrada:bytes=b''
    pc:int=0
    acumulador:int=0
    cursor:int=0
    parou:bool=False
    trace:list=field(default_factory=list)
    max_trace:int=1000
    def ler(self,endereco):
        if endereco%2 or not 0<=endereco<=4094:raise ValueError('Acesso desalinhado ou fora da memória')
        return int.from_bytes(self.memoria[endereco:endereco+2],'big')
    def escrever(self,endereco,valor):
        self.ler(endereco);self.memoria[endereco:endereco+2]=(valor&0xffff).to_bytes(2,'big')
    def passo(self):
        if self.parou:raise RuntimeError('Máquina parada')
        anterior=self.pc;instrucao=self.ler(self.pc);op=instrucao>>12;arg=instrucao&0xfff;self.pc+=2
        if op==0:self.pc=arg
        elif op==1:
            if self.acumulador==0:self.pc=arg
        elif op==2:
            if self.acumulador&0x8000:self.pc=arg
        elif op==3:self.acumulador=arg
        elif op in (4,5,6,7):
            a,b=assinado(self.acumulador),assinado(self.ler(arg))
            if op==4:v=a+b
            elif op==5:v=a-b
            elif op==6:v=a*b
            else:
                if not b:raise ZeroDivisionError('Divisão MVN por zero')
                v=abs(a)//abs(b)*(1 if (a>=0)==(b>=0) else -1)
            self.acumulador=v&0xffff
        elif op==8:self.acumulador=self.ler(arg)
        elif op==9:self.escrever(arg,self.acumulador)
        elif op==10:self.escrever(arg,self.pc);self.pc=arg+2
        elif op==11:self.pc=self.ler(arg)
        elif op==12:self.parou=True
        elif op==13:
            if arg!=0x300:raise NotImplementedError('Somente disco 0: GD /300')
            chunk=self.entrada[self.cursor:self.cursor+2];self.cursor+=2;self.acumulador=int.from_bytes(chunk.ljust(2,b'\0'),'big')
        elif op==14:raise NotImplementedError('PD não é usado pelo programa fornecido')
        else:raise NotImplementedError('Opcode não implementado')
        if len(self.trace)<self.max_trace:self.trace.append({'pc':f'{anterior:04X}','instrucao':f'{instrucao:04X}','acumulador':f'{self.acumulador:04X}'})
    def executar(self,limite=200000):
        for _ in range(limite):
            if self.parou:return
            self.passo()
        raise TimeoutError('Limite de instruções excedido')
