import math
def solution(n, stations, w):
    answer=0
    start=1
    for station in stations :
        answer+=math.ceil((station-w-start)/(w*2+1))
        start=station+w+1
    if n>=start :
        answer+=math.ceil((n-start+1)/(w*2+1))

    return answer