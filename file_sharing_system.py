from typing import List
from collections import defaultdict
import heapq
# Online Python - IDE, Editor, Compiler, Interpreter
class FileSharing:
    def __init__(self, m: int):
        self.cur = 0
        self.chunks = m
        self.reused = []
        self.user_chunks = defaultdict(set)

    def join(self, ownedChunks: List[int]) -> int:
        if self.reused:
            userID = heapq.heappop(self.reused)
        else:
            self.cur += 1
            userID = self.cur
        self.user_chunks[userID] = set(ownedChunks)
        return userID

    def leave(self, userID: int) -> None:
        heapq.heappush(self.reused, userID)
        self.user_chunks.pop(userID)

    def request(self, userID: int, chunkID: int) -> List[int]:
        if chunkID < 1 or chunkID > self.chunks:
            return []
        res = []
        for k, v in self.user_chunks.items():
            if chunkID in v:
                res.append(k)
        if res:
            self.user_chunks[userID].add(chunkID)
        return sorted(res)

obj = FileSharing(4)
print(obj.join([1,2]))
print(obj.join([2,3]))
print(obj.join([4]))
print(obj.request(1,3))
print(obj.request(2,2))
print(obj.leave(1))
print(obj.request(2,1))
print(obj.leave(2))
print(obj.join([]))

