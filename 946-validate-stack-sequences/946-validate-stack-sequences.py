class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        pop_idx = 0
        cur_stack = []
        for i in range(len(pushed)):
            cur_stack.append(pushed[i])
            while cur_stack and cur_stack[-1] == popped[pop_idx]:
                cur_stack.pop()
                pop_idx += 1
        
        while pop_idx < len(popped):
            if cur_stack[-1] == popped[pop_idx]:
                cur_stack.pop()
                pop_idx += 1
            else:
                return False
            
        return True
        