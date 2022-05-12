class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        counts = {}
        for letter in s:
            counts[letter] = counts.get(letter, 0) + 1
        
        inc_stack = deque()
        seen = set()
        for letter in s:
            while len(inc_stack) > 0 and letter < inc_stack[-1]:
                if letter in seen:
                    break
                while inc_stack and counts[inc_stack[-1]] > 1 and letter < inc_stack[-1]:
                    l = inc_stack.pop()
                    counts[l] -= 1
                    seen.remove(l)
                break
            if letter in seen:
                counts[letter] -= 1
            else:
                inc_stack.append(letter)
                seen.add(letter)
        
        return ''.join(inc_stack)