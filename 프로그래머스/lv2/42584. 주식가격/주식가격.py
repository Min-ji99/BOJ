# 주식 가격
from collections import deque

def solution(prices):
    answer = []
    queue = deque(prices)
    # print(queue)
    
    while queue:
        price = queue.popleft()
        time = 0
        for num in queue:
            time += 1
            if price > num:
                break
        answer.append(time)
    # print(answer)
    return answer
'''
def solution(prices):
    answer = [0]*len(prices)
    for i in range(len(prices)) :
        for j in range(i+1, len(prices)) :
            if prices[i]<=prices[j] :
                answer[i]+=1
            else:
                answer[i]+=1
                break
    return answer
    '''