n, m=map(int, input().split())
list=[]
def dfs(cnt, num) :
    if cnt==m :
        print(' '.join(map(str, list)))
        return
    for i in range(num, n+1) :
        list.append(i)
        dfs(cnt+1, i)
        list.pop()
dfs(0, 1)