import heapq
def solution(n, s, a, b, fares):
 
    def dijkstra(start):
        res = [float('INF') for _ in range(n+1)]
        res[start] = 0
        q = []
        heapq.heappush(q, (res[start], start))
        while q:
            result_x, x = heapq.heappop(q)
            for fu, fw in graph[x]:
                if res[fu] > result_x + fw:
                    res[fu] = result_x + fw
                    heapq.heappush(q, ([res[fu], fu]))
        return res
 
    ans = 200000001
    graph = [[] for _ in range(n+1)]
    for i, j, c in fares:
        graph[i].append((j, c))
        graph[j].append((i, c))
    
    dist = [[]]
    for i in range(1, n+1):
        dist.append(dijkstra(i))
 
    for i in range(1, n+1):
        ans = min(ans, dist[s][i] + dist[i][a] + dist[i][b])
    return ans