from collections import deque
def solution(n, computers):
    ans=0
    visit=[0]*n
    q=deque()

    def dfs(start):
        visit[start] = 1
        
        for idx in range(n) :
            if idx!=start and computers[start][idx]==1 and visit[idx]==0:
                dfs(idx)
    for i in range(n) :
        if visit[i]==0 :
            dfs(i)
            ans+=1
    return ans
'''
def dfs(n, computers, visit, idx):
    visit[idx]=1
    for i in range(n) :
        if idx!=i and computers[idx][i]==1 :
            if visit[i]==0 :
                dfs(n, computers, visit, i)
'''