class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        count = {}
        value = 0
        for n in nums:
            count[n] = count.get(n, 0) +1

        for l,m in count.items():
            j = m*(m-1)//2
            value += j
        return value

        