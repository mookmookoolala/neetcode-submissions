class Solution:
    def search(self, nums: List[int], target: int) -> int:
        count = len(nums)//2
        left = 0
        right = len(nums) - 1
        middle = (left + right) // 2
        while left <= right:
            if target > nums[middle]:
                left = middle + 1
                middle = (left + right)//2
            
            if target < nums[middle]:
                right = middle - 1
                middle = (left+right)//2

            if target == nums[middle]:
                return middle 

        return -1