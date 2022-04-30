class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        G = defaultdict(list)
        for (v, w), value in zip(equations, values):
            G[v].append((w, value))
            G[w].append((v, 1/value))
        def find_path(v, goal):
            if not G[v] or not G[goal]: return -1.0
            visited = set()
            def dfs(v, goal, d):
                if v == goal: return d
                if v in visited: return -1.0
                visited.add(v)
                for w, value in G[v]:
                    tmp = dfs(w, goal, d*value)
                    if tmp != -1.0:
                        return tmp
                return -1.0
            return dfs(v, goal, 1)
        return [find_path(v, w) for v, w in queries]