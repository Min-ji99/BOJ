from collections import defaultdict
import math

def cal_time(in_time, out_time) :
    in_hour, in_minute=map(int, in_time.split(":"))
    out_hour, out_minute=map(int, out_time.split(":"))
    
    return (out_hour-in_hour)*60+(out_minute-in_minute)

def cal_fee(info, fees) :
    total=0
    
    for i in range(len(info)) : #짝수는 In, 홀수는 Out
        if i%2==1 :
            total+=cal_time(info[i-1], info[i])
            
    #입차만 있는 경우
    if len(info)%2==1 :
        total+=cal_time(info[-1], "23:59")
        
    if total<=fees[0] :
        return fees[1]
    return fees[1]+math.ceil((total-fees[0])/fees[2])*fees[3]
    
def solution(fees, records):
    answer = []
    infos=defaultdict(list) #key : 차량번호, value : 시간
    
    for record in records :
        time, num, status=record.split(" ")
        infos[num].append(time)
    
    
    for info in sorted(infos.items()) : #차량번호 기준 정렬
        answer.append(cal_fee(info[1], fees))
    
    return answer