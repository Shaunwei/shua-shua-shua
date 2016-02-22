'''
-1 as not used
1 as black chip
0 as white chip
'''

class UnionFind:
    def __init__(self, n):
        self.parents = {}
        # dummy outbound
        self.n = n

    def _id(self, i, j):
        return i * self.n + j

    def add(self, i, j):
        p = self._id(i, j)
        self.parents[p] = p

    def find(self, i, j):
        father = self._id(i, j)
        while self.parents[father] != father:
            father = self.parents[father]

        p = self._id(i, j)
        while self.parents[p] != father:
            temp = self.parents[p]
            self.parents[p] = father
            p = temp
        return father

    def union(self, i, j, x, y):
        if self._id(x, y) not in self.parents:
            self.add(x, y)
        p1 = self.find(i, j)
        p2 = self.find(x, y)

        if p1 == p2:
            return
        if p1 < p2:
            self.parents[p2] = p1
        else:
            self.parents[p1] = p2


class Solution:
    def __init__(self, board):
        self.board = board
        self.uf = UnionFind(len(board) + 2)
        self.setup_dummy(len(board) + 2)

    def setup_dummy(self, n):
        corners = [(0, 0), (0, n - 1), (n - 1, 0), (n - 1, n - 1)]
        for i, j in corners:
            self.uf.add(i, j)
            self.uf.union(0, 0, i, j)

        for x in range(1, n - 1):
            self.uf.union(0, x - 1, 0, x)
            self.uf.union(x - 1, 0, x, 0)
            self.uf.union(n - 1, x - 1, n - 1, x)
            self.uf.union(x - 1, n - 1, x, n - 1)


    def solve(self):
        n = len(self.board) + 2
        for i in range(1, n - 1):
            for j in range(1, n - 1):
                if self.board[i - 1][j - 1]:
                    self.uf.add(i, j)
                    if self.valid_up_right(i, j):
                        if self.valid_up_left(i, j):
                            if i > 1 and self.board[i - 2][j - 1] == 0:
                                self.bfs(i - 2, j - 1)
                            self.uf.union(i - 1, j + 1, i, j)
                            self.uf.union(i - 1, j - 1, i, j)
                        elif self.valid_left(i, j):
                            if i > 1 and self.board[i - 2][j - 1] == 0:
                                self.bfs(i - 2, j - 1)
                            self.uf.union(i - 1, j + 1, i, j)
                            self.uf.union(i, j - 1, i, j)
        self.closing_last_line(n - 1)

    def closing_last_line(self, n_1):
        i = n_1
        for j in range(1, n_1):
            if self.valid_up_right(i, j) and self.valid_up_left(i, j):
                if self.board[i - 2][j - 1] == 0:
                    self.bfs(i - 2, j - 1)

    def valid_up_right(self, i, j):
        if i > 1:
            if j == len(self.board):
                return True
            else:
                return self.board[i - 2][j] == 1
        return False

    def valid_up_left(self, i, j):
        if i > 1:
            if j == 1:
                return True
            else:
                return self.board[i - 2][j - 2] == 1
        return False

    def valid_left(self, i, j):
        if j == 1:
            return True
        else:
            return self.board[i - 1][j - 2] == 1


    def bfs(self, i, j):
        queue = []
        queue.append([i, j])
        m = len(self.board)
        self.board[i][j] = -1
        while queue:
            mi, mj = queue.pop(0)
            if mi > 0 and self.board[mi - 1][mj] == 0:
                queue.append([mi - 1, mj])
                self.board[mi - 1][mj] = -1
            if mj > 0 and self.board[mi][mj - 1] == 0:
                queue.append([mi, mj - 1])
                self.board[mi][mj - 1] = -1
            if mi < m - 1 and self.board[mi + 1][mj] == 0:
                queue.append([mi + 1, mj])
                self.board[mi + 1][mj] = -1
            if mj < m - 1 and self.board[mi][mj + 1] == 0:
                queue.append([mi, mj + 1])
                self.board[mi][mj + 1] = -1



if __name__ == '__main__':
    boards = [
        [
            [-1, 1,  1],
            [ 1, 0,  1],
            [ 1, 0,  1]
        ],
        [
            [-1, 1, -1],
            [ 1, 0,  1],
            [-1, 1, -1]
        ],
        [
            [ 0, 1, -1],
            [ 0, 0,  1],
            [ 1, 1, -1]
        ],
    ]
    for board in boards:
        s = Solution(board)
        s.solve()
        for r in s.board:
            print(r)
        print('--------')
'''
[-1, 1, 1]
[1, -1, 1]
[1, -1, 1]
--------
[-1, 1, -1]
[1, -1, 1]
[-1, 1, -1]
--------
[-1, 1, -1]
[-1, -1, 1]
[1, 1, -1]
'''
