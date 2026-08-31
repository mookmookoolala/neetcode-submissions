class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        count = {}
        inverse_count = {}
        if len(pattern) != len(s.split()):
            return False 
        
        word = s.split()

        for i,n in zip(pattern,word):
            if i in count:
                if count[i] != n:
                    return False
            else:
                count[i] = n

            if n in inverse_count:
                if inverse_count[n] != i:
                    return False
            else:
                inverse_count[n] = i

        return True
                
