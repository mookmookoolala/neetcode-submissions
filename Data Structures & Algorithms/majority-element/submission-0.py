class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        counts = {}
        
        for n in nums:
            counts[n] = counts.get(n, 0) + 1
        for keys,values in counts.items():
            if values > len(nums)/2:
                return keys
            