from pathlib import Path
import sys, json, argparse

root = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(root))
from mvn import Maquina, montar, assinado

p = argparse.ArgumentParser()
p.add_argument("expressao")
p.add_argument("--trace", action="store_true")
a = p.parse_args()
mem, s = montar(
    [root / "asm" / f for f in ["main.asm", "le_byte.asm", "pilha.asm", "rpn.asm"]]
)
m = Maquina(mem, a.expressao.encode("ascii"))
m.executar()
status = m.ler(s["RPN_STATUS"])
resultado = assinado(m.ler(s["RPN_RESULT"]))
print(json.dumps({"status": status, "resultado": resultado}, ensure_ascii=False))
if a.trace:
    (root / "build").mkdir(exist_ok=True)
    (root / "build/trace.json").write_text(json.dumps(m.trace, indent=2))
sys.exit(0 if status == 0 else 2)
