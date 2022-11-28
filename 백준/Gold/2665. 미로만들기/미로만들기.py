import sys, heapq

input=sys.stdin.readline

n=int(input())
maps=[list(map(int, input().rstrip())) for _ in range(n)]

visit=[[0]*n for _ in range(n)]

dx=[0, 0, -1, 1]
dy=[1, -1, 0, 0]

def dijkstra():
    q=[]
    heapq.heappush(q, [0, 0, 0])
    visit[0][0]=1
    while q:
        wall, x, y=heapq.heappop(q)
        if x==n-1 and y==n-1 :
            print(wall)
            return
        for i in range(4) :
            nx=x+dx[i]
            ny=y+dy[i]
            if 0<=nx<n and 0<=ny<n and visit[nx][ny]==0 :
                visit[nx][ny]=1
                if maps[nx][ny]==0 :
                    heapq.heappush(q, [wall+1, nx, ny])
                else:
                    heapq.heappush(q, [wall, nx, ny])
dijkstra()