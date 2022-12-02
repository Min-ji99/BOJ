def solution(strs, t):
    answer = 0
    dp=[float('inf')]*(len(t)+1)
    dp[0]=0
    for i in range(1, len(t)+1) :
        for k in range(1, 6) :
            if i<k :
                start=0
            else:
                start=i-k
            if t[start:i] in strs :
                dp[i]=min(dp[i], dp[i-k]+1)
    if dp[-1]==float('inf'):
        return -1
    return dp[-1]