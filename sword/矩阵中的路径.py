# -*- coding:utf-8 -*-
# 请设计一个函数，用来判断在一个矩阵中是否存在一条包含某字符串所有字符的路径。路径可以从矩阵中的任意一个格子开始，
# 每一步可以在矩阵中向左，向右，向上，向下移动一个格子。如果一条路径经过了矩阵中的某一个格子，则之后不能再次进入这个格子。
#  例如 a b c e s f c s a d e e 这样的3 X 4 矩阵中包含一条字符串"bcced"的路径，
# 但是矩阵中不包含"abcb"路径，因为字符串的第一个字符b占据了矩阵中的第一行第二个格子之后，路径不能再次进入该格子。

# 思路：dfs,注意先把字符串转成二维数组。先写边界条件，成功/失败的情况，在写递归过程。注意这里的visited需要pop()因为是
# 可以返回的，而不是统计全局的。
class Solution:
    def hasPath(self, matrix, rows, cols, path):
        # write code here
        new = []
        for i in range(0, rows):
            new.append(matrix[i * cols:i * cols + cols])
        matrix = new
        visited = []
        for i in range(0, rows):
            for j in range(0, cols):
                if self._dfs(matrix, i, j, rows, cols, path, visited, 0, []):
                    return True
        return False


    def _dfs(self,matrix, i, j, rows, cols, path, visited, pos, cur):
        if ''.join(cur) == path:
            return True
        if i < 0 or i >= rows or j < 0 or j >= cols or [i,j] in visited:
            return False
        if path[pos] == matrix[i][j]:
            visited.append([i, j])
            ret =  self._dfs(matrix, i + 1, j, rows, cols, path, visited, pos + 1, cur + [matrix[i][j]]) or \
            self._dfs(matrix, i - 1, j, rows, cols, path, visited, pos + 1, cur + [matrix[i][j]]) or \
            self._dfs(matrix, i, j + 1, rows, cols, path, visited, pos + 1, cur + [matrix[i][j]]) or \
            self._dfs(matrix, i, j - 1, rows, cols, path, visited, pos + 1, cur + [matrix[i][j]])
            visited.pop()
            return ret
        else:
            return False

s = Solution()
print s.hasPath(
    'ABCEHJIGSFCSLOPQADEEMNOEADIDEJFMVCEIFGGS', 5, 8, 'SGGFIECVAASABCEHJIGQEM')