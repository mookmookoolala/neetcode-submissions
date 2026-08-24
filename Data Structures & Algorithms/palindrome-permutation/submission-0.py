class Solution:
    def canPermutePalindrome(self, s: str) -> bool:
        count = {}

        for ch in s:
            count[ch] = count.get(ch, 0) + 1

        start = 0

        for values in count.values():
            if values %2 != 0:
                start += 1
        
        if start > 1:
            return False
        else:
            return True