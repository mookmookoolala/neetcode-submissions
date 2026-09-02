class Solution:
    def divideArray(self, nums: List[int]) -> bool:
        count = {}
        if len(nums)%2 != 0:
            return False

        for i in nums:
            count[i] = count.get(i, 0) + 1
        
        for l,m in count.items():
            if m%2 != 0:
                return False
        return True
        