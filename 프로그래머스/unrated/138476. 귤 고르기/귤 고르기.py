from collections import defaultdict

def solution(k, tangerine):
    answer = 0
    kinds=defaultdict(int)
    for t in tangerine :
        kinds[t]+=1
        
    kinds=sorted(kinds.items(), key=lambda x:-x[1])
    
    for key, value in kinds :
        k-=value
        answer+=1
        if k<=0 :
            break

    return answer