class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for row in board:
            seen = set()

            for f in row:
                if f == ".":
                    continue
                if f in seen:
                    return False

                seen.add(f)
            
        for c in range(9):
            seen = set()

            for d in range(9):
                column = board[d][c]

                if column == ".":
                    continue
                
                if column in seen:
                    return False
                
                seen.add(column)
            

        for row in range(3):
            for column in range(3):
                seen = set()

                for box_row in range(3):
                    for box_column in range(3):

                        inner_row = row * 3 + box_row
                        inner_column = column * 3 + box_column

                        full = board[inner_row][inner_column]


                        if full == ".":
                            continue
                        
                        if full in seen:
                            return False
                        
                        seen.add(full)
            
        return True



            
        