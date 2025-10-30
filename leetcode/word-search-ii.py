class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        trie = {}
        for word in words:
            node = trie
            for ch in word:
                node = node.setdefault(ch, {})
            node['word'] = word
        
        rows, cols = len(board), len(board[0])
        res = []

        def dfs(r, c, node):
            ch = board[r][c]
            if ch not in node:
                return
            node = node[ch]
            if 'word' in node:
                res.append(node['word'])
                node.pop('word')
            
            board[r][c] = '0' # mark visited
            for dr, dc in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                nr, nc = r + dr, c + dc
                if 0 <= nr < rows and 0 <= nc < cols and board[nr][nc] != '0':
                    dfs(nr, nc, node)
            board[r][c] = ch
        
        for r in range(rows):
            for c in range(cols):
                dfs(r, c, trie)
        return res