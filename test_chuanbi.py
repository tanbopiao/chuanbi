"""传璧（CHUANBI）算子单测：名帖完整、行为达标、只增不覆盖。"""
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

    def test_handshake_relay(self):
        token = self.op.handshake("节点甲")
        receipt = self.op.relay({"token": token, "payload": "音信"})
        self.assertTrue(receipt["delivered"])
        with self.assertRaises(PermissionError):
            self.op.relay({"token": "伪物", "payload": "x"})


if __name__ == "__main__":
    unittest.main()
