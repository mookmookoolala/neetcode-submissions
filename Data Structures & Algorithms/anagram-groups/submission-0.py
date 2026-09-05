class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        count = {}
        final = []
        for l in strs:
            m = tuple(sorted(l))
            if m not in count:
                count[m] = []
            count[m].append(l)
        return list(count.values())

            