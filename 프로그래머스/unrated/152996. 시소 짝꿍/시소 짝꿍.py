from collections import Counter

def solution(weights) :
    answer=0
    c=Counter(weights)

    #1:1이 짝궁인 경우
    for key, value in c.items() :
        if value>=2 :
            answer+=value*(value-1)//2

    weights=set(weights) #중복 몸무게 제거
    
    #2:3, 2:4, 3:4 비율
    for weight in weights :
        if weight*2/3 in weights :
            answer+=c[weight*2/3] * c[weight]
        if weight*2/4 in weights:
            answer+=c[weight*2/4] * c[weight]
        if weight*3/4 in weights:
            answer+=c[weight*3/4] *c[weight]
            
    return answer