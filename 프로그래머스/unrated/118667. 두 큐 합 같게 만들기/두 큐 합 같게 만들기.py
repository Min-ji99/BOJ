'''
from collections import deque

def solution(queue1, queue2):
    answer = -1
    q1=deque(queue1)
    q2=deque(queue2)
    sum1=sum(q1)
    sum2=sum(q2)
    same_sum=(sum1+sum2)//2
    count=0
    while q1 and q2 :
        if sum1==same_sum:
            return count
        elif sum1>same_sum :
            sum1-=q1.popleft()
        elif sum2>same_sum :
            q1.append(q2.popleft())
            sum1+=q1[-1]
        count+=1
        
    return answer
'''
from collections import deque

def solution(queue1, queue2):
    queue1, queue2 = deque(queue1), deque(queue2)
    q1_sum = sum(queue1)
    half_total_sum = (q1_sum + sum(queue2)) // 2  # 두 큐 합의 절반
    cnt = 0

    while queue1 and queue2:
        if q1_sum == half_total_sum:  # 두 큐 합이 같으면 종료
            return cnt
        elif q1_sum > half_total_sum:  # queue1의 합이 더 크면 queue1에서 빼기
            q1_sum -= queue1.popleft()
        else:  # queue1의 합이 queue2보다 작을 때
            queue1.append(queue2.popleft())
            q1_sum += queue1[-1]
        cnt += 1

    return -1  # 두 큐 합이 같아지지 않으면 -1 반환