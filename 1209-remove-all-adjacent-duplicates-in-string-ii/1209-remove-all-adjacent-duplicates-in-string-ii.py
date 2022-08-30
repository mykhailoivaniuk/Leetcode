from collections import deque
class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        chars = deque()
        for i in range(len(s)):
            if not len(chars):
                chars.append([s[i], 1])
                continue
            if chars[-1][0] == s[i]:
                chars[-1][1] += 1
                if chars[-1][1] == k:
                    chars.pop()
            else:
                chars.append([s[i], 1])
            
        return "".join([x[0]*x[1] for x in chars])