class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        values_dicc = {}
        for value in nums:
            if value in values_dicc:
                return True
            
            values_dicc[value] = 0;
        return False;