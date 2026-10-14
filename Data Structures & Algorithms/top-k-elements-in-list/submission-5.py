class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        mostFrecuence = {}
        frecuenceDict = {} # num : frecuence

        for n in nums:
            frecuenceDict[n] = frecuenceDict.get(n, 0) + 1
        
        #print(f'frecuenceDict: {frecuenceDict}')
        for idx, (num, freq) in enumerate(frecuenceDict.items()):
            #print (f'idx: {idx}')
            
            if idx < k:
                mostFrecuence[num] = freq
                continue
            
            #print (f'mostFrecuence: {mostFrecuence}')

            cLowestFrequence = float('inf')
            cLowestFrequenceNum = float('inf')
            for cMostFrequenceNum, cMostFrequence in mostFrecuence.items():
                # Get the current lowest frequence
                if cMostFrequence < cLowestFrequence:
                    cLowestFrequence = cMostFrequence
                    cLowestFrequenceNum = cMostFrequenceNum

            # Check if the current lowest frequence is lowest than that
            # the frequence tha we are iterating
            if freq > cLowestFrequence:
                mostFrecuence.pop(cLowestFrequenceNum)
                mostFrecuence[num] = freq
        
        return list(mostFrecuence.keys())

        