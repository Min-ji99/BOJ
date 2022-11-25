import heapq, sys

def solution(N, road, K):
    distance=[sys.maxsize]*(N+1)
    graph=[[] for _ in range(N+1)]
    for r in road :
        graph[r[0]].append([r[1], r[2]])
        graph[r[1]].append([r[0], r[2]])

    def dijkstra(start) :
        distance[start]=0
        q=[]
        heapq.heappush(q, [0, start])

        while q :
            weight, node=heapq.heappop(q)
            for next_node, wei in graph[node]:
                if wei+weight<distance[next_node]:
                    distance[next_node]=wei+weight
                    heapq.heappush(q, [wei+weight, next_node])
    dijkstra(1)

    return len([x for x in distance if x<=K])