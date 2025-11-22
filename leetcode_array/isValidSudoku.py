class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        submat = [set() for _ in range(9)]


        for i in range(9):
            for j in range(9):
                val = board[i][j]

                if val == '.':
                    continue
                if val in rows[i]:
                    return False
                else:
                    rows[i].add(val)

                if val in cols[j]:
                    return False
                else:
                    cols[j].add(val)

                idx = (i//3)*3 + (j//3)

                if val in submat[idx]:
                    return False
                else:
                    submat[idx].add(val)
        return True

    


        
