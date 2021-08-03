class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        # 方向数组
        di = [-1, 0, 0, 1]
        dj = [0, -1, 1, 0]
        m = len(grid)
        n = len(grid[0])
        visited = [[False] * n for i in range(m)]
        self.fa = [0] * (m * n)
        ans = 0
        for i in range(m):
            for j in range(n):
                self.fa[i * n + j] = i * n + j

        for i in range(m):
            for j in range(n):
                if not visited[i][j] and grid[i][j] == "1":
                    visited[i][j] = True
                    for k in range(4):
                        ni = i + di[k]
                        nj = j + dj[k]
                        if ni < m and nj < n and ni >= 0 and nj >= 0 and not visited[ni][nj] and grid[ni][nj] == "1":
                            self.unionSet(i * n + j, ni * n + nj)

        for i in range(m):
            for j in range(n):
                if grid[i][j] == "1" and self.fa[i * n + j] == i * n + j:
                    ans += 1
        return ans

    def find(self, index):
        if self.fa[index] == index:
            return index
        else:
            self.fa[index] = self.find(self.fa[index])
        return self.fa[index]

    def unionSet(self, index1, index2):
        x = self.find(index1)
        y = self.find(index2)
        if x != y:
            self.fa[x] = y