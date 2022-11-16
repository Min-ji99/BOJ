from collections import deque

n, k=map(int, input().split())

MAX=100000
lines=[0]*(MAX+1)
visit=[False]*(MAX+1) #index 0은 걷는 경우 index 1은 점프하는 경우

q=deque()
q.append(n)
visit[n]=True
while q:
    x=q.popleft()
    if x*2<=MAX and visit[x*2]==False:
        visit[x*2]=True
        lines[x*2]=lines[x]
        q.appendleft(x*2)
    if x+1<=MAX and visit[x+1]==False:
        visit[x+1]=True
        lines[x+1]=lines[x]+1
        q.append(x+1)
    if x-1>=0 and visit[x-1]==False:
        visit[x-1]=True
        lines[x-1]=lines[x]+1
        q.append(x-1)
print(lines[k])