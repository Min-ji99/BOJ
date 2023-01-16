def solution(cap, n, deliveries, pickups):
    answer = 0
    deliveries=deliveries[::-1]
    pickups=pickups[::-1]

    delivery_cnt=0
    pickup_cnt=0
    for i in range(n) :
        delivery_cnt+=deliveries[i]
        pickup_cnt+=pickups[i]
        while delivery_cnt>0 or pickup_cnt>0 :
            answer+=(n-i)*2
            delivery_cnt-=cap
            pickup_cnt-=cap
    return answer