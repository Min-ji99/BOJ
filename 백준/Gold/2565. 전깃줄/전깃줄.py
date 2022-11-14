
n=int(input())

connect = []
for i in range(n) :
    connect.append(list(map(int, input().split())))
    
connect.sort()
dp=[1]*n
for i in range(n) :
    for j in range(i) :
        if connect[i][1]>connect[j][1] and dp[i]<dp[j]+1:
            dp[i]=dp[j]+1
            
print(n-max(dp))