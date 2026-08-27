class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        count = {}
        full = set(nums)
        output = []

        for n in range(1 ,len(nums)+1):
            if n not in nums:
                output.append(n)
        return output