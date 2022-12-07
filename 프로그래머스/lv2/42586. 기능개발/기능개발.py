import math

def solution(progresses, speeds):
    answer=[]
    time=[]
    for i in range(len(speeds)) :
        time.append(math.ceil((100-progresses[i])/speeds[i]))

    now=time[0]
    cnt=1
    for i in range(1, len(time)) :
        if now>=time[i] :
            cnt+=1
        else:
            answer.append(cnt)
            now=time[i]
            cnt=1
    if cnt!=0 :
        answer.append(cnt)
    return answer