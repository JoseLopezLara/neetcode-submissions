class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # nums  =    [1, 2, 4, 6]
        # r     =    [1, 1, 2, 8]
        # r     =    [48, 24, 12, 8]
        
        # prx   =    [1, 2, 8, 48]
        # sux   =    [48,48,24,6]
        r   = [1 for _ in range(len(nums))]

        prx = 1
        for i, n in enumerate(nums):
            prx *= n
            r[i+1] = prx
            
            if i == len(nums) - 2:
                break;

        sux = 1
        for i, n in reversed(list(enumerate(nums))):
            sux *= n
            r[i-1] *= sux
            
            if i == 1:
                break;
        
        return r



