class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        count = {}

        for n in magazine:
            count[n] = count.get(n, 0) + 1

        for n in ransomNote:
            if n in count and count[n] != 0:
                count[n] -= 1
            else:
                return False
        return True
            
            
        