'''
q1의 합이 정답보다 크면 pop 작으면 append
'''
from collections import deque

def solution(queue1, queue2):
    answer = 0
    q1, q2=deque(queue1), deque(queue2)
    
    sum_q1=sum(queue1)
    sum_q2=sum(queue2)
    result=(sum_q1+sum_q2)//2
    
    while(q1 and q2):
        if sum_q1==result:
            return answer
            
        if sum_q1 >result :
            sum_q1-=q1.popleft()
        else:
            tmp=q2.popleft()
            sum_q1+=tmp
            q1.append(tmp)
        answer+=1
    return -1