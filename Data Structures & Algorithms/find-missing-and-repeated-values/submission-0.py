class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        count = {}
        gone = []
        for row in grid:
            for number in row:
                count[number] = count.get(number, 0) + 1
        for key,values in count.items():
            if values >= 2:
                gone.append(key)

        for n in range(1, len(grid)**2+1):
            if n not in count:
                gone.append(n)
                
        return gone
                        
                    
