import sys
import heapq

input=sys.stdin.readline

INF=sys.maxsize
v, e=map(int, input().split())
k=int(input())
graph=[[] for _ in range(v+1)]
distance=[INF]*(v+1)
q=[]
for _ in range(e) :
    a, b, c=map(int, input().split())
    graph[a].append([b, c])

def dijkstra(start):
    distance[start]=0
    now=heapq.heappush(q, [0, start])

    while q:
        min, node=heapq.heappop(q)
        for next_node, cost in graph[node]:
            if distance[next_node]>min+cost:
                distance[next_node]=min+cost
                heapq.heappush(q, [min+cost, next_node])
dijkstra(k)

for d in distance[1:]:
    if d==INF :
        print("INF")
    else:
        print(d)