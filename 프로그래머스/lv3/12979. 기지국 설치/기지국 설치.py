import math

def solution(n, stations, w):
    answer = 0
    next=1
    for station in stations :
        if station-w-next>0:
            answer+=math.ceil((station-w-next)/(w*2+1))
        next=station+w+1
    if next<=n:
        answer+=math.ceil((n-next+1)/(w*2+1))
    return answer