import bisect
# Online Python - IDE, Editor, Compiler, Interpreter
class HitCounter:

    def __init__(self):
        self.ts = []

    def hit(self, timestamp: int) -> None:
        self.ts.append(timestamp)

    def getHits(self, timestamp: int) -> int:
        return len(self.ts) - bisect.bisect_left(self.ts, timestamp - 300 + 1)

hitCounter = HitCounter()
print(hitCounter.hit(1))
print(hitCounter.hit(2))
print(hitCounter.hit(3))
print(hitCounter.getHits(4))
print(hitCounter.hit(300))
print(hitCounter.getHits(300))
print(hitCounter.getHits(301))

