class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        def is_valid(r, c, ch):
            box = (r // 3) * 3 + (c // 3)
            return not (ch in rows[r] or ch in cols[c] or ch in boxes[box])
        
        def place(r, c, ch):
            board[r][c] = ch
            rows[r].add(ch)
            cols[c].add(ch)
            boxes[(r // 3) * 3 + (c // 3)].add(ch)
        
        def remove(r, c, ch):
            board[r][c] = "."
            rows[r].remove(ch)
            cols[c].remove(ch)
            boxes[(r // 3) * 3 + (c // 3)].remove(ch)
        
        def backtrack(pos=0):
            if pos == len(empty):
                return True
            r, c = empty[pos]
            for ch in '123456789':
                if is_valid(r, c, ch):
                    place(r, c, ch)
                    if backtrack(pos + 1):
                        return True
                    remove(r, c, ch)
            return False
        
        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        boxes = [set() for _ in range(9)]
        empty = []

        for r in range(9):
            for c in range(9):
                if board[r][c] == '.':
                    empty.append((r, c))
                else:
                    place(r, c, board[r][c])
        
        backtrack()