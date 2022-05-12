class Solution:
    def smallestSubsequence(self, s: str) -> str:
        last_seen = {}
        for i in range(len(s)):
            last_seen[s[i]] = i
        
        inc_stack = deque()
        seen = set()
        for i, letter in enumerate(s):
            if letter not in seen:
                while inc_stack and last_seen[inc_stack[-1]] > i and letter < inc_stack[-1]:
                    seen.remove(inc_stack.pop())
                    
                inc_stack.append(letter)
                seen.add(letter)
        
        return ''.join(inc_stack)
        