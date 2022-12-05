import sys
from collections import deque
from itertools import combinations

input=sys.stdin.readline
n, m=map(int, input().split())

dx=[-1, 1, 0, 0]
dy=[0, 0, -1, 1]

boards=[list(map(int, input().split())) for _ in range(n)]

def make_wall(count):
    if count==3:
        bfs()
        return
    for i in range(n) :
        for j in range(m) :
            if(boards[i][j]==0):
                boards[i][j]=1
                make_wall(count+1)
                boards[i][j]=0
def bfs():
    global ans
    q=deque()
    visit=[[0]*m for _ in range(n)]
    for i in range(n) :
        for j in range(m) :
            if(boards[i][j]==1):
                visit[i][j]=1
            elif boards[i][j]==2 :
                visit[i][j]=1
                q.append([i, j])

    while q :
        x, y=q.popleft()
        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]
            if 0<=nx<n and 0<=ny<m and visit[nx][ny]==0:
                if boards[nx][ny]==0:
                    q.append([nx, ny])
                    visit[nx][ny]=1
    cnt=0
    for i in range(n) :
        for j in range(m) :
            if boards[i][j]==0 and visit[i][j]==0:
                cnt+=1
    ans=max(ans, cnt)

ans=0
make_wall(0)
print(ans)