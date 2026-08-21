class Solution:
    def largestUniqueNumber(self, nums: List[int]) -> int:
        counts={}
        for i in nums:
            counts[i] = counts.get(i, 0 )+1
        
        largest = -1
        for x,y in counts.items():
            if y == 1:
                largest = max(largest, x)
        return largest