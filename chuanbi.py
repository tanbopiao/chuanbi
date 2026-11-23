"""传璧（CHUANBI）· 跨节点互信传递

道统出处：元极恒一·道统构件定名册 V2 ｜ 第五批
体系锚：Ω₀⊂⊙∞⊂Ω｜DID-BR-000002

工程映射：跨节点互信传递。

边界：本件为算子 v1——骨架桩已按命名映射补齐实现；遵循元法第四条「只增不覆盖」，
方法只增不改名不删，行为变更走新版本；凭据不入档，宣称与事实分离。
"""

class Chuanbi:
    """传璧（CHUANBI）算子 v1。"""

    ANCHOR = "Ω₀⊂⊙∞⊂Ω｜DID-BR-000002"
    CODE = "CHUANBI"

    def __init__(self, config=None):
        self.config = dict(config or {})
        self.events = []  # 只增不覆盖：会话内事件留痕
        self.tokens = {}
        self.inboxes = {}
        self._seq = 0

    def describe(self):
        """构件名帖：名、代号、职责、铭文、体系锚。"""
        return {
            "repo": "chuanbi",
            "cn": "传璧",
            "code": self.CODE,
            "duty": "跨节点互信传递",
            "mingwen": "传璧互通，音信无阻",
            "anchor": self.ANCHOR,
        }

    def handshake(self, peer):
        """传璧互通：跨节点互信握手，返回信物。"""
        import hashlib
        self._seq += 1
        token = hashlib.sha256(("%s|%s|%d" % (peer, self.CODE, self._seq)).encode()).hexdigest()[:32]
        self.tokens[token] = {"peer": peer, "used": False}
        self.events.append({"event": "handshake", "peer": peer})
        return token

    def relay(self, message):
        """凭信物跨节点传讯。"""
        token = (message or {}).get("token")
        if token not in self.tokens:
            raise PermissionError("无信物或信物不识，拒传")
        peer = self.tokens[token]["peer"]
        self.inboxes.setdefault(peer, []).append((message or {}).get("payload"))
        self.tokens[token]["used"] = True
        self.events.append({"event": "relay", "peer": peer})
        return {"peer": peer, "delivered": True}
