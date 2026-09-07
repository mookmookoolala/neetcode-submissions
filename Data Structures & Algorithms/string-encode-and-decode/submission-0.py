class Solution:

    def encode(self, strs: List[str]) -> str:
        count = {}
        result = ""
        for i in strs:
            result += str(len(i)) + "#" + i
        return result
        

    def decode(self, s: str) -> List[str]:
        result = []
        i = 0
        j = 0

        while i < len(s):
            j = i
            while s[j] != "#":
                j += 1
            
            k = int(s[i:j])
            word = s[j+1:j + 1 + k]
            result.append(word)
            i = j + 1 + k
        return result


