from collections import Counter

def check(arr, x, y, tmp, visit) :
    init=arr[x][y]
    for i in range(x, x+tmp) :
        for j in range(y, y+tmp) : 
            if arr[i][j]!=init :
                return 0, 0
    for i in range(x, x+tmp) :
        for j in range(y, y+tmp) :
            visit[i][j]=True
            
    return init, tmp*tmp #압축한 숫자, 개수 반환
            
def solution(arr):
    answer = [0, 0]
    n=len(arr)
    visit=[[False]*n for _ in range(n)]
    counter=Counter()
    
    for i in range(n) :
        counter+=Counter(arr[i])
    #print(counter)
    
    tmp=n
    while tmp>1 :
        for i in range(n) :
            for j in range(0, n, tmp) :
                if i%tmp==0 and not visit[i][j] : #압축하지 않은 경우
                    init, count=check(arr, i, j, tmp, visit)
                    if count>0 :
                        counter[init]-=count-1
        tmp//=2
    return [counter[0], counter[1]]