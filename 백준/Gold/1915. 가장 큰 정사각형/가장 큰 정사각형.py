import sys
input=sys.stdin.readline
n, m=map(int, input().split())
maps=[list(map(int, input().rstrip())) for _ in range(n)]

dp=[[0]*m for _ in range(n)]
for i in range(n) :
    for j in range(m) :
        if i==0 or j==0 :
            dp[i][j]=maps[i][j]
        elif maps[i][j]==1:
            dp[i][j]=min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1])+1
        else:
            dp[i][j]=0
answer=0
for i in range(n) :
    answer=max(answer, max(dp[i]))

print(answer*answer)
