from itertools import combinations
from collections import Counter

def solution(orders, course):
    answer = []
    set_menu=[]
    for c in course:
        set_menu=[]
        for order in orders :
            for comb in combinations(order, c):
                comb=''.join(sorted(comb))
                set_menu.append(comb)
                
        counter=Counter(set_menu)
        if len(counter)==0 :
            continue
        counter=sorted(counter.items(), key=lambda x:-x[1])
        maxCnt=0
        for key, value in counter :
            if value>=2 and maxCnt<=value :
                answer.append(key)
                maxCnt=value
            else:
                break
        
    return sorted(answer)
        