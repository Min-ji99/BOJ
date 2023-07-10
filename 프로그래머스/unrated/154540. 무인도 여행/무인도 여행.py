from collections import deque

def solution(maps):
    answer=[]
    n=len(maps)
    m=len(maps[0])
    boards=[]
    visit=[[False]*m for _ in range(n)]
    dx, dy=[-1, 1, 0, 0], [0, 0, -1, 1]
    
    for i in range(n) :
        tmp=[]
        for j in range(m) :
            if maps[i][j]=='X':
                tmp.append(0)
            else:
                tmp.append(int(maps[i][j]))
        boards.append(tmp)
                
    def bfs(i, j):
        q=deque()
        q.append([i, j])
        cnt=boards[i][j]
        visit[i][j]=True
        
        while q:
            x, y=q.popleft()
            
            for i in range(4):
                nx, ny=x+dx[i], y+dy[i]
                if 0<=nx<n and 0<=ny<m and visit[nx][ny]==False:
                    if boards[nx][ny]>0:
                        cnt+=boards[nx][ny]
                        q.append([nx, ny])
                        visit[nx][ny]=True
        return cnt
    for i in range(n) :
        for j in range(m) :
            if boards[i][j]>0 and not visit[i][j] :
                answer.append(bfs(i, j))
                
    if len(answer)==0 :
        return [-1]
    return sorted(answer)