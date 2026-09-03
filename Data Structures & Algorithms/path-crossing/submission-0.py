class Solution:
    def isPathCrossing(self, path: str) -> bool:
        x=0
        y=0
        visited = {(0,0)}
        for move in path:
            if move == "N":
                y+=1
            if move == "S":
                y-=1
            if move == "E":
                x+=1
            if move == "W":
                x-=1
            

            if (x,y) in visited:
                return True
            else:
                visited.add((x,y))
                
        return False
            