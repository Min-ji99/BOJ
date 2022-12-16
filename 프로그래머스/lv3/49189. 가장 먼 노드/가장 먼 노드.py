from collections import deque
def solution(n, edge):
    graph=[[] for _ in range(n+1)]
    q=deque()
    distance=[-1]*(n+1)
    
    for a, b in edge :
        graph[a].append(b)
        graph[b].append(a)
    q.append(1)
    distance[1]=0
    
    while q :
        now=q.popleft()
        for next in graph[now] :
            if distance[next]==-1:
                distance[next]=distance[now]+1
                q.append(next)
    ans=max(distance)
    return distance.count(ans)