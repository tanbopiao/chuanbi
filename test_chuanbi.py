"""传璧（CHUANBI）算子骨架单测：名帖完整、桩位齐整、只增不覆盖。"""
import unittest

from chuanbi import Chuanbi


class TestChuanbi(unittest.TestCase):
    def setUp(self):
        self.op = Chuanbi()

    def test_describe(self):
        d = self.op.describe()
        self.assertEqual(d["repo"], "chuanbi")
        self.assertEqual(d["code"], "CHUANBI")
        self.assertTrue(d["anchor"].startswith("Ω₀⊂⊙∞⊂Ω"))
        self.assertTrue(d["mingwen"])

    def test_handshake_stub(self):
        with self.assertRaises(NotImplementedError):
            self.op.handshake(None)

    def test_relay_stub(self):
        with self.assertRaises(NotImplementedError):
            self.op.relay(None)


if __name__ == "__main__":
    unittest.main()
