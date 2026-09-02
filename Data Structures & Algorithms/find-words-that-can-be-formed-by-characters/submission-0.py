class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        count = {}
        total = 0

        for n in chars:
            count[n] = count.get(n, 0) + 1
        
        for word in words:            

            word_count={}
            for i in word:
               word_count[i] = word_count.get(i, 0) + 1
            
            valid = True

            for l,m in word_count.items():
                if m > count.get(l, 0):
                    valid = False
            
            if valid == True:
                total += len(word)
        return total


