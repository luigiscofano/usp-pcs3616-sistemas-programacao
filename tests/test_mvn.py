import unittest, random
from pathlib import Path
from mvn import Maquina, montar, assinado

ROOT = Path(__file__).resolve().parents[1]


def programa():
    return montar(
        [ROOT / "asm" / f for f in ["main.asm", "le_byte.asm", "pilha.asm", "rpn.asm"]]
    )


def calcular(texto):
    mem, s = programa()
    m = Maquina(mem, texto.encode("ascii"))
    m.executar()
    return m.ler(s["RPN_STATUS"]), assinado(m.ler(s["RPN_RESULT"]))


class TestMvn(unittest.TestCase):
    def test_entradas(self):
        for label, addr in {
            "SUB_LE_BYTE": 0x300,
            "LE_BYTE_RESULT": 0x304,
            "LE_BYTE_ARG": 0x306,
            "SUB_PUSH": 0x500,
            "PUSH_ARG": 0x504,
            "PUSH_ERROR_SLOT": 0x506,
            "SUB_POP": 0x700,
            "POP_RESULT": 0x704,
            "POP_ERROR_SLOT": 0x706,
            "SUB_RPN": 0x900,
            "RPN_RESULT": 0x904,
            "RPN_ERROR_SLOT": 0x906,
            "STACK_POINTER": 0xFFE,
        }.items():
            with self.subTest(label=label):
                self.assertEqual(programa()[1][label], addr)

    def test_exemplos(self):
        for text, want in [
            ("12 3 +\n", 15),
            ("12 3 +", 15),
            ("5 9 -", -4),
            ("20 3 /", 6),
            ("0 7 - 2 /", -3),
            ("65535", -1),
            ("32767 1 +", -32768),
            ("2\t3\r+", 5),
            ("2 3+\n999", 5),
        ]:
            with self.subTest(text=text):
                self.assertEqual(calcular(text), (0, want))

    def test_invalidos(self):
        for text in ["", "+", "1 2", "2 0 /", "1 X", "1 2 + +", " ".join(["1"] * 128)]:
            with self.subTest(text=text):
                self.assertNotEqual(calcular(text)[0], 0)

    def test_operacoes_aleatorias(self):
        r = random.Random(13680334)
        for _ in range(400):
            a, b = r.randrange(200), r.randrange(1, 200)
            op = r.choice(["+", "-", "*", "/"])
            out = {"+": a + b, "-": a - b, "*": a * b, "/": a // b}[op]
            out = assinado(out & 65535)
            self.assertEqual(calcular(f"{a} {b} {op}"), (0, out))

    def chamada(self, m, s, label):
        m.pc = 0
        m.parou = False
        m.escrever(0, 0xA000 + s[label])
        m.escrever(2, 0xC000)
        m.executar()

    def test_bytes(self):
        mem, s = programa()
        m = Maquina(mem, b"ABCD\x00")
        val = []
        for _ in range(6):
            self.chamada(m, s, "SUB_LE_BYTE")
            val.append(m.ler(s["LE_BYTE_RESULT"]))
        self.assertEqual(val, [65, 66, 67, 68, 0, 0])

    def test_todos_bytes(self):
        mem, s = programa()
        m = Maquina(mem, bytes(range(256)))
        for v in range(256):
            self.chamada(m, s, "SUB_LE_BYTE")
            self.assertEqual(m.ler(s["LE_BYTE_RESULT"]), v)

    def test_pilha_limites(self):
        mem, s = programa()
        m = Maquina(mem)
        self.chamada(m, s, "SUB_POP")
        self.assertEqual(m.ler(s["POP_STATUS"]), 1)
        for v in range(127):
            m.escrever(s["PUSH_ARG"], v)
            self.chamada(m, s, "SUB_PUSH")
            self.assertEqual(m.ler(s["PUSH_STATUS"]), 0)
        self.chamada(m, s, "SUB_PUSH")
        self.assertEqual(m.ler(s["PUSH_STATUS"]), 1)
        self.assertEqual(m.ler(s["STACK_POINTER"]), 0xF00)
        for v in reversed(range(127)):
            self.chamada(m, s, "SUB_POP")
            self.assertEqual(m.ler(s["POP_RESULT"]), v)
        self.assertEqual(m.ler(s["STACK_POINTER"]), 0xFFE)

    def test_alinhamento(self):
        m = Maquina(bytearray(4096))
        with self.assertRaises(ValueError):
            m.ler(1)

    def test_timeout(self):
        m = Maquina(bytearray(4096))
        with self.assertRaises(TimeoutError):
            m.executar(20)


if __name__ == "__main__":
    unittest.main()
