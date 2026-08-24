class Solution:
    def calculateTime(self, keyboard: str, word: str) -> int:
        full = {}
        for i,n in enumerate(keyboard):
            full[n] = i

            start = 0
            prev = 0

        for x in word:
            current = full[x]
            start += abs(prev-current)
            prev = current
        
        return start



            
            

             