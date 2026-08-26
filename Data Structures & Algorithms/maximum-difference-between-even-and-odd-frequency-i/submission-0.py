class Solution:
    def maxDifference(self, s: str) -> int:
        counts = {}
        charseven = []
        charsodd = []
        for n in s:
            counts[n] = counts.get(n, 0) + 1
        
        for keys,values in counts.items():
            if values%2 == 0:
                charseven.append(values)
            else:
                charsodd.append(values)
        return max(charsodd) - min(charseven)