class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        count = {}
        valid = False
        total = 0


        for i in words:
            valid = True 

            for n in i:
                if n not in allowed:
                    valid = False
         
            if valid:
                total += 1

        return total