class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        distinctValues = dict(); # value : index

        for idx, value in enumerate(nums):
            diff = target - value

            if diff in distinctValues:
                return [distinctValues[diff], idx]
                
            #for distinctValueK, distinctValueV in distinctValues.items():
            #    if value + distinctValueK == target:
            #        return [distinctValueV, idx]

            distinctValues[value] = idx
