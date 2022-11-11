n=int(input())

dp=[0]*31
dp[2]=3


for i in range(4, n+1, 2) :#홀수인 경우는 0
    #dp[i-2]*dp[2] 3x2가 뒤에 오는 경우
    dp[i]=dp[i-2]*3+sum(dp[:i-2])*2+2

print(dp[n])