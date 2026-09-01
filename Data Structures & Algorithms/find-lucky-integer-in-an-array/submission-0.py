class Solution:
    def findLucky(self, arr: List[int]) -> int:
        value = {}
        largest = -1
        for i in arr:
            value[i] = value.get(i, 0) + 1

        for l,m in value.items():
            if m == l:
                largest=max(largest, l)
        return largest

        