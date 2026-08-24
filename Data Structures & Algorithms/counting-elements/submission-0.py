class Solution:
    def countElements(self, arr: List[int]) -> int:
        number = set(arr)

        start = 0

        for x in arr:
            if x+1 in number:
                start += 1
        return start           
        