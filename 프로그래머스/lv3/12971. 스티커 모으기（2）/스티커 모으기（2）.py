def solution(sticker) :
    n=len(sticker)
    
    if n==1: return sticker[0]

    dp=[[0]*n for _ in range(2)]
    dp[0][0]=sticker[0] #첫번째 스티커를 뜯은 경우
    dp[0][1]=sticker[0]
    dp[1][1]=sticker[1] #첫번째 스티커를 뜯지 않는 경우
    
    for i in range(2, n-1) :
        dp[0][i]=max(dp[0][i-1], dp[0][i-2]+sticker[i])
    
    for i in range(2, n) :
        dp[1][i]=max(dp[1][i-2]+sticker[i], dp[1][i-1])
    
    return max(dp[0][-2], dp[1][-1])