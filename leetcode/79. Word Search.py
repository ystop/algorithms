# -*- coding:utf-8 -*-
# 思路: 记住，如果这层不好解决，可以递归到下一层统一解决。注意维护visited数组，

class Solution(object):
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        m = len(board)
        n = len(board[0])
        visited = []
        for i in range(0, m):
            for j in range(0, n):
                if board[i][j] == word[0]:
                    if self._find(board, i, j, 0, word, visited, []):
                        return True
        return False

    def _find(self, board, i, j, pos, word, visited, cur):
        #print board, i, j, pos, word, visited
        if cur == list(word):
            return True
        #print visited
        if i < len(board) and i >= 0 and j < len(board[0]) and j >= 0 and [i, j] not in visited and board[i][j] == word[pos]:
            visited.append([i, j])
            cur.append(board[i][j])
            ret = self._find(board, i + 1, j, pos + 1, word, visited, cur) \
                or self._find(board, i - 1, j, pos + 1, word, visited, cur) \
                or self._find(board, i, j + 1, pos + 1, word, visited, cur) \
                or self._find(board, i, j - 1, pos + 1, word, visited, cur)
            visited.pop()
            cur.pop()
            return ret
        else:
            return False

s = Solution()
print s.exist([
  ['A','B','C','E'],
  ['S','F','C','S'],
  ['A','D','E','E']
], 'ABCCED')
print s.exist([
  ['A','B','C','E'],
  ['S','F','C','S'],
  ['A','D','E','E']
], 'SEE')
print s.exist([
  ['A','B','C','E'],
  ['S','F','C','S'],
  ['A','D','E','E']
], 'ABCB')