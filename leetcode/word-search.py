class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        numRows, numCols = len(board), len(board[0])
        wordPath = set()

        def dfs(r, c, length):
            if length == len(word):
                return True
            
            if (min(r, c) < 0 or
                r == numRows or
                c == numCols or
                word[length] != board[r][c] or
                (r, c) in wordPath
            ):
                return False
            
            wordPath.add((r, c))

            res = (
                dfs(r + 1, c, length + 1) or
                dfs(r - 1, c, length + 1) or
                dfs(r, c + 1, length + 1) or
                dfs(r, c - 1, length + 1)
            )

            wordPath.remove((r, c))
            
            return res
        
        for row in range(numRows):
            for col in range(numCols):
                if dfs(row, col, 0):
                    return True
        return False