from collections import defaultdict
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # STP1: Init vars
        mostFrecuence = []
        frequenceDict = {}

        bucketSortAux = [[]] * len(nums)

        # STP2: Get frequences
        for n in nums:
            frequenceDict[n] = frequenceDict.get(n, 0) + 1
        
        # STP3: Insert frequence into arrey bucket sort
        for n, f in frequenceDict.items():
            #bucketSortAux[f-1] += [n]
            bucketSortAux[f-1] = bucketSortAux[f-1] + [n]

        # STP4: Get the last 2 positions
        for v in bucketSortAux[::-1]:
            if v is []:
                continue
            if len(mostFrecuence) < k:
                mostFrecuence += v  

        return mostFrecuence

        