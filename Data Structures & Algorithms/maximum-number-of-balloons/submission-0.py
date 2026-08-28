class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        count = {}
        word = ["b","a","l","l","o","o","n"]
        for n in text:
            count[n] = count.get(n, 0)+1

        x = min(
            count.get("b", 0),
            count.get("a", 0),
            count.get("l", 0)//2,
            count.get("o", 0)//2,
            count.get("n", 0)
        )

        return x
                    