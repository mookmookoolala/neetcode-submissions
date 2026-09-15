class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        left = 0
        right = 0 
        most_common = 0
        count = {}
        best = 0

        for right in range(len(s)):
            count[s[right]] = count.get(s[right] , 0) + 1

            if count[s[right]] > most_common:
                most_common = count[s[right]]

            size = right - left + 1
            need = size - most_common

            if need > k:
                count[s[left]] -= 1
                left += 1

            best = max(best, right - left + 1)
        return best

        