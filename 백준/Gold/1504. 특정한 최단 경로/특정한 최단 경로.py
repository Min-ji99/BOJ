import sys
import heapq

input=sys.stdin.readline
INF=sys.maxsize
n, e=map(int, input().split())
graph=[[] for _ in range(n+1)]

for _ in range(e) :
    a, b, c=map(int, input().split())
    graph[a].append([b, c])
    graph[b].append([a, c])

v1, v2=map(int, input().split())

def dijkstra(start) :
    d=[INF]*(n+1)
    q=[]
    d[start]=0
    heapq.heappush(q, [0, start])
    while q:
        wei, now=heapq.heappop(q)
        for next_node, cost in graph[now]:
            if d[next_node]>wei+cost:
                d[next_node]=wei+cost
                heapq.heappush(q, [wei+cost, next_node])
    return d

start=dijkstra(1)
v1_dijkstra=dijkstra(v1)
v2_dijksta=dijkstra(v2)
answer=min(start[v1]+v1_dijkstra[v2]+v2_dijksta[n], start[v2]+v2_dijksta[v1]+v1_dijkstra[n])

if answer<INF :
    print(answer)
else:
    print(-1)