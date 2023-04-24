from collections import defaultdict

def solution(topping):
    answer = 0
    left=defaultdict(int)
    right=defaultdict(int)
    
    for i in range(len(topping)):
        right[topping[i]]+=1
    
    for i in range(len(topping)) :
        if topping[i] not in left :
            left[topping[i]]=1
        else:
            left[topping[i]]+=1
        if right[topping[i]]==1:
            del right[topping[i]]
        else:
            right[topping[i]]-=1
        
        if len(left)==len(right) :
            answer+=1
        
    return answer