class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        self.fa = [i for i in range(len(edges) + 1)]
        self.ans = []
        for i in range(len(edges)):
            self.unionSet(edges[i][0], edges[i][1])
        return self.ans

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
        if x == y:
            self.ans += [index1, index2]