from collections import deque
def solution(n, edge):
    q=deque()
    graph=[[] for _ in range(n+1)]
    distance=[-1]*(n+1)
    for a, b in edge :
        graph[a].append(b)
        graph[b].append(a)
    q.append(1)
    distance[1]=0

    while q :
        node=q.popleft()
        for next in graph[node] :
            if(distance[next]==-1) :
                distance[next]=distance[node]+1
                q.append(next)
    ans=max(distance)
    return distance.count(ans)