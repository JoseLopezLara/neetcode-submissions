class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        distinctValues = dict();

        for idx, value in enumerate(nums):
            for distinctValueK, distinctValueV in distinctValues.items():
                if value + distinctValueK == target:
                    return [distinctValueV, idx]

            distinctValues[value] = idx
