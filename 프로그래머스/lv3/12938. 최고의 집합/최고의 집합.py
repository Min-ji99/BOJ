'''
중간값들의 곱이 최대
'''
def solution(n, s):
    answer = []

    if n>s :
        return [-1]
    
    answer=[s//n for x in range(n)]
    reminder=s%n
    pos=0
    while reminder!=0 :
        answer[pos]+=1
        reminder-=1
        pos+=1
    return sorted(answer)