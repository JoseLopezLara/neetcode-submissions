from collections import Counter
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # NOTE: It's an easy way
        # cout_dict = Counter(list(s))
        # print(cout_dict.get('e'))

        
        # Edge validation
        if len(s) != len(t):
            return False

        # Main algorithm
        s_dicc = dict();
        t_dicc = dict();

        # Building a dictionary for counting the number of letters 
        for idx in range(len(s)):
            s_dicc[s[idx]] = s_dicc.get(s[idx], 0) + 1
            t_dicc[t[idx]] = t_dicc.get(t[idx], 0) + 1

        # Verify anagram
        for k, v in s_dicc.items():
            if k not in t_dicc:
                return False
            if v != t_dicc[k]:
                return False
        
        return True
