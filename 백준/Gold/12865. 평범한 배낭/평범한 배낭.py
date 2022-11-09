import sys
input=sys.stdin.readline

n, k=map(int, input().split())
things=[list(map(int, input().split())) for _ in range(n)]
things.sort()
dp=[[0]*(k+1) for _ in range(n+1)]

for i in range(1, n+1):
    for j in range(1, k+1):
        weight=things[i-1][0]
        if j<weight :
            dp[i][j]=dp[i-1][j]
        else:
            dp[i][j]=max(dp[i-1][j-weight]+things[i-1][1], dp[i-1][j])

print(dp[n][k])