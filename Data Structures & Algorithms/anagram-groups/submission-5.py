class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # ----------------------------
        #  ------- MY SOLUTION -------
        # ----------------------------

        # enagramsDict = dict() # sortedEnagram : [word, word]
        # for word in strs:
        #     sortedWord = "".join(sorted(word))
        # 
        #     if sortedWord in enagramsDict:
        #         # enagramsDict[sortedWord] = enagramsDict[sortedWord] + [word]
        #         enagramsDict[sortedWord].append(word)
        #     else:
        #         enagramsDict[sortedWord] = [word]    
        # return list(enagramsDict.values())

        # -----------------------------------------------------------
        # ----- OPTIMAL SOLUTION WITH OUT WATCHING THE SOLUTION -----
        # -----------------------------------------------------------
        enagramsDict = dict() # ASCII enagram mapping : [word, word]
        for word in strs:
            asciiWord = [0] * 26
            for character in word:
                asciiWord[ord(character) - ord("a")] += 1

            if tuple(asciiWord) in enagramsDict:
                enagramsDict[tuple(asciiWord)].append(word)
            else:
                enagramsDict[tuple(asciiWord)] = [word]

        return list(enagramsDict.values())

        # -----------------------------------------------------------
        # ----- OPTIMAL SOLUTION WATCHING THE SOLUTION -----
        # -----------------------------------------------------------
        enagramsDict = dict() # ASCII enagram mapping : [word, word]
        for word in strs:
            asciiWord = [0] * 26
            for character in word:
                asciiWord[ord(character) - ord("a")] += 1

            enagramsDict[tuple(asciiWord)].append(word)

        return list(enagramsDict.values())