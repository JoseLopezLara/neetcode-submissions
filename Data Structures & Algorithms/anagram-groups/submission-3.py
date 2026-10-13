class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        enagramsDict = dict() # sortedEnagram : [word, word]
        # print(type(sorted('word')))
        for word in strs:
            sortedWord = "".join(sorted(word))

            if sortedWord in enagramsDict:
                enagramsDict[sortedWord] = enagramsDict[sortedWord] + [word]
            else:
                enagramsDict[sortedWord] = [word]    

        # print(enagramsDict)

        return list(enagramsDict.values())