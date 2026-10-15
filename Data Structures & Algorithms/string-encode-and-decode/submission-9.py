import json
from collections import defaultdict
class Solution:

    def encode(self, strs: List[str]) -> str:
        wordsMap = defaultdict(list)   # "word" : [int (ending position), int, ..., int]
        r = '';

        for idx, s in enumerate(strs):
            if wordsMap[s] is not None:
                wordsMap[s].append(idx)
            else:
                wordsMap[s] = [idx]
        
        return json.dumps(wordsMap)

    def decode(self, s: str) -> List[str]:
        wordsMap = json.loads(s)

        # Edge case optimization
        if wordsMap == {}: return []

        lastPlace = 0;
        for k, v in wordsMap.items():
            for p in v:
                if p > lastPlace:
                    lastPlace = p

        r = ['' for _ in range(lastPlace + 1)]

        for k, v in wordsMap.items():
            for p in v:
                r[p] = k
        
        return r
            