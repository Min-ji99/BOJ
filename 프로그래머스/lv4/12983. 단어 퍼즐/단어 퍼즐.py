def solution(strs, t):
    answer = 0
    n=len(t)
    dp=[float('inf')]*(n+1)
    dp[0]=0
    for i in range(1, n+1):
        for k in range(1, 6):
            if i<k : start = 0
            else : start=i-k
            if t[start:i] in strs :
                dp[i]=min(dp[i], dp[i-k]+1)
    if dp[-1]==float('inf') :
        return -1
    else : return dp[-1]