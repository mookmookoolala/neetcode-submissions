class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        longest = 0
        number = set(nums)
        for n in number:
            if n-1 in number:
                continue
            
            current = n
            length = 1
            
            while current+1 in number:
                current += 1
                length += 1
        
            longest = max(longest, length)
        return longest
        
        

