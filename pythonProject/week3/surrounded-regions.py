class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        self.di = [-1, 0, 0, 1]
        self.dj = [0, -1, 1, 0]
        self.board = board
        self.visited = [[False] * len(self.board[0]) for i in range(len(self.board))]
        self.border = [[False] * len(self.board[0]) for i in range(len(self.board))]

        # 维护self.border True 表示这里与边界的“O”相连
        for i in range(len(self.board)):
            for j in range(len(self.board[0])):
                if self.board[i][j] == "O" and (i == 0 or j == 0 or i == len(self.board) - 1 or j == len(self.board[0]) - 1):
                    self.border[i][j] = True

        #遍历与边界处"O"相邻的"O"
        for i in range(len(self.board)):
            for j in range(len(self.board[0])):
                if self.board[i][j] == "O" and self.border[i][j] and not self.visited[i][j]:
                    self.bfs(i, j)
                    # self.dfs(i, j)

        # 这里如果有"0"没和边界的"0"相邻，将其转化为"X"
        for i in range(len(self.board)):
            for j in range(len(self.board[0])):
                if self.board[i][j] == "O" and not self.border[i][j]:
                    self.board[i][j] = "X"

        return self.board

    def bfs(self, i, j):
        queue = collections.deque()
        queue.append([i, j])
        while queue:
            i, j = queue.popleft()
            for k in range(4):
                ni = i + self.di[k]
                nj = j + self.dj[k]
                if ni < 0 or nj < 0 or ni >= len(self.board) or nj >= len(self.board[0]):
                    continue
                if self.board[ni][nj] == "O" and not self.visited[ni][nj]:
                    queue.append([ni, nj])
                    self.visited[ni][nj] = True
                    self.border[ni][nj] = True


    def dfs(self, i, j):
        self.visited[i][j] = True
        self.border[i][j] = True
        for k in range(4):
            ni = i + self.di[k]
            nj = j + self.dj[k]
            if ni < 0 or nj < 0 or ni >= len(self.board) or nj >= len(self.board[0]):
                continue
            if self.board[ni][nj] == "O" and not self.visited[ni][nj]:
                self.dfs(ni, nj)