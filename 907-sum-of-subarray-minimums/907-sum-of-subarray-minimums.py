class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        # not implemented yet
        modulo = 10**9 + 7
        
        monotonic_stack = deque()
        size = len(arr)
        prev_smaller = [i+1  for i in range(len(arr))]
        next_smaller = [size-i for i in range(len(arr))]
            
        for i in range(size):
            while len(monotonic_stack) > 0 and arr[monotonic_stack[-1]] >= arr[i]:
                idx = monotonic_stack.pop()
                next_smaller[idx] = i - idx;
            monotonic_stack.append(i)
        monotonic_stack.clear()
        
        for i in range(size-1, -1, -1):
            while len(monotonic_stack)>0 and arr[monotonic_stack[-1]] > arr[i]:
                idx = monotonic_stack.pop()
                prev_smaller[idx] = idx - i
            monotonic_stack.append(i)
        res = 0
        # print(f'{next_smaller} next_smaller')
        # print(f'{prev_smaller} prev_smaller')
        for i in range(len(arr)):
            res += prev_smaller[i]*next_smaller[i]*arr[i]
        
        return res % modulo