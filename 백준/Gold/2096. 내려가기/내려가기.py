import sys

input=sys.stdin.readline

n=int(input())
max_dp=[0]*3
min_dp=[0]*3

max_tmp=[0]*3
min_tmp=[0]*3
for i in range(n) :
    a, b, c=map(int, input().split())
    for j in range(3) :
        if j==0 :
            max_tmp[j]=a+max(max_dp[1], max_dp[0])
            min_tmp[j]=a+min(min_dp[0], min_dp[1])
        elif j==1:
            max_tmp[j]=b+max(max_dp[0], max_dp[1], max_dp[2])
            min_tmp[j]=b+min(min_dp[0], min_dp[1], min_dp[2])
        else:
            max_tmp[j]=c+max(max_dp[1], max_dp[2])
            min_tmp[j]=c+min(min_dp[1], min_dp[2])
    for j in range(3) :
        max_dp[j]=max_tmp[j]
        min_dp[j]=min_tmp[j]
        
print(max(max_dp), min(min_dp))