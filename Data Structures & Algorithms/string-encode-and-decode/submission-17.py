class Solution:

    def encode(self, strs: List[str]) -> str:
        r = ''
        # STP#1 add lenght limmiter
        for s in strs:
            r += str(len(s)) + '~' + s

        return r

    def decode(self, s: str) -> List[str]:
        print(s)
        lastWordPosition, r = 0, []
        print(f"s: {len(s) - 1}")

        while lastWordPosition < len(s) - 1:
            
            # STP#1 get de lenght of the current curren word
            currentWordSizePosition = 0
            #print(lastWordPosition)
            while s[lastWordPosition + currentWordSizePosition] != '~':
                currentWordSizePosition += 1
            
            # STP#2 Add the new word and increment (update) the new last word position
            print(f'len(s[lastWordPosition:lastWordPosition + currentWordSizePosition]): {len(s[lastWordPosition:lastWordPosition + currentWordSizePosition])}')
            
            r.append(s[
                lastWordPosition + currentWordSizePosition + 1 : 
                lastWordPosition + int(s[lastWordPosition:lastWordPosition + currentWordSizePosition]) + len(s[lastWordPosition:lastWordPosition + currentWordSizePosition]) + 1
                ])
            lastWordPosition = lastWordPosition + int(s[lastWordPosition:lastWordPosition + currentWordSizePosition]) + len(s[lastWordPosition:lastWordPosition + currentWordSizePosition]) + 1
            print(lastWordPosition)
            #print(s[lastWordPosition])
            
        return r