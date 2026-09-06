class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        jump = []
        total_count = []
        for l in nums:
            count[l] = count.get(l, 0) + 1
        
        for u,t in count.items():
            jump.append((u,t))

        jump.sort(key=lambda x: x[1], reverse = True)
        
        for x in jump[:k]:
            total_count.append(x[0])
            
        return total_count
        