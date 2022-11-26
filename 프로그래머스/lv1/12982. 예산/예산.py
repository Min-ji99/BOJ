def solution(d, budget):
    answer = 0
    tmp=budget
    d.sort()
    cnt=0
    for i in d:
        if i<=tmp :
            cnt+=1
            tmp-=i
        else:
            break
    return cnt