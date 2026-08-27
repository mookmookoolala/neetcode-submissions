class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        count = {}
        unique = []
        for n in arr:
            count[n] = count.get(n, 0) + 1

        for key,value in count.items():
            if value < 2:
                unique.append(key)
                if len(unique) >= k:
                    return unique[k-1]

        return ""


        