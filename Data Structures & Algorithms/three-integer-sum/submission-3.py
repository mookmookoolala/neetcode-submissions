class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        sorted_nums = sorted(nums)
        target = 0
        triplet = []
        for i,n in enumerate(sorted_nums):
            left = i + 1
            right = len(nums) - 1
            if i > 0:
                if sorted_nums[i] == sorted_nums[i-1]:
                    continue
            while left < right:
                if n + sorted_nums[left] + sorted_nums[right] < 0:
                    left += 1
                elif n + sorted_nums[left] + sorted_nums[right] > 0:
                    right -= 1
                elif n + sorted_nums[left] + sorted_nums[right] == 0:
                    triplet.append([n,sorted_nums[left], sorted_nums[right]])
                    left += 1
                    right -= 1
                    while left<right and sorted_nums[left] == sorted_nums[left-1]:
                        left+=1
                    
                    while left<right and sorted_nums[right] == sorted_nums[right+1]:
                        right-=1

        return triplet

                

            
            