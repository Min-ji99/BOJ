def solution(priorities, location):
    answer=1
    idx=0
    
    while(idx<=location) :
        change=False
        for i in range(idx+1, len(priorities)) :
            if(priorities[idx]<priorities[i]) :
                priorities.append(priorities.pop(idx))
                if location==idx :
                    location=len(priorities)-1
                else:
                    location-=1
                change=True
                break
        if not change :
            if idx==location :
                return answer
            else:
                idx+=1
                answer+=1
    return answer
                    