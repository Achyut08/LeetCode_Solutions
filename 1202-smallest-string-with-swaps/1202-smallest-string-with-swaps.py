class Solution:
    def smallestStringWithSwaps(self, s: str, pairs: List[List[int]]) -> str:
        """Getting all the indices (island_numbers) and letters (island) that need to be change"""
        def dfs(graph, node, been, island, letters, island_numbers):
            for i in range(len(graph[node])):
                if graph[node][i] not in been:
                    been.add(graph[node][i])
                    island.append(letters[graph[node][i]])
                    island_numbers.append(graph[node][i])
                    dfs(graph, graph[node][i], been, island, letters, island_numbers)
        
        graph = {} # the graph that will store the nodes
        letters = {i: element for i, element in enumerate(s)} # dictionary to help transforming from indices to letters
        for i in range(len(pairs)):
            if pairs[i][0] not in graph:
                graph[pairs[i][0]] = [pairs[i][1]]
            else:
                graph[pairs[i][0]].append(pairs[i][1])
            if pairs[i][1] not in graph:
                graph[pairs[i][1]] = [pairs[i][0]]
            else:
                graph[pairs[i][1]].append(pairs[i][0])
        been = set()
        ans = list(s)
        for i in range(len(pairs)):
            if pairs[i][0] not in been: # if this node hasn't been visited yet
                island = []
                island_numbers = []
                dfs(graph, pairs[i][0], been, island, letters, island_numbers)
                island = sorted(island)
                island_numbers = sorted(island_numbers)
                for i in range(len(island_numbers)): 
                    ans[island_numbers[i]] = island[i] 
        return "".join(ans)