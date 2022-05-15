from collections import defaultdict


class Graph:

    def __init__(self):
        self.g = defaultdict(list)
        self.number_edges = 0
        self.v = set()
        self.s = 0
        self.b = 0

    def add_edge(self, u, v):
        self.g[u].append(v)
        self.v.add(u)
        self.v.add(v)
        self.number_edges = self.number_edges + 1

    def bfs(self, s):
        self.s = s
        queue = []
        visited = defaultdict(int)
        visited[s] = 1
        queue.append(s)
        while queue:
            expand_v = queue.pop(0)
            print(expand_v, end=" ")
            for i in self.g[expand_v]:
                if visited[i] != 1:
                    queue.append(i)
                    visited[i] = 1

    def dfs(self, s):
        self.s = s
        visited = defaultdict(int)
        visited[s] = 1
        self.dfs_util(s, visited)
        for i in self.v:
            if visited[i] != 1:
                self.dfs_util(i, visited)

    def dfs_util(self, s, visited):
        self.s = s
        stack = []
        stack.append(s)
        while stack:
            expand_v = stack.pop()
            print(expand_v, end=" ")
            for i in self.g[expand_v]:
                if visited[i] != 1:
                    stack.append(i)
                    visited[i] = 1


