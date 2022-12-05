from collections import deque
N, M=map(int, input().split())
matrix=[]
for i in range(N) :
  matrix.append(list(map(int, list(input().strip()))))

dx=[1, -1, 0, 0]
dy=[0, 0, 1, -1]

def bfs() :
  q=deque()
  q.append((0, 0, 1))
  visited=[[[0]*2 for i in range(M)] for i in range(N)]
  visited[0][0][1]=1
  while q:
    x, y, z = q.popleft()
    if x==N-1 and y==M-1 :
      return visited[x][y][z]
    for i in range(4) :
      nx=x+dx[i]
      ny=y+dy[i]
      if 0<=nx<N and 0<=ny<M :
        if matrix[nx][ny]==1 and z==1 :
          visited[nx][ny][0]=visited[x][y][1] +1
          q.append((nx, ny, 0))
        elif matrix[nx][ny]==0 and visited[nx][ny][z]==0 :
          visited[nx][ny][z] = visited[x][y][z]+1
          q.append((nx, ny, z))
  return -1

print(bfs())