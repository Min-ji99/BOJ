import heapq

def solution(scoville, K):
    answer = 0
    heap=[]
    for s in scoville:
        heapq.heappush(heap, s)
    
    while heap[0]<K:
        new=heapq.heappop(heap)+heapq.heappop(heap)*2
        heapq.heappush(heap, new)
        answer+=1
        
        if heap[0]<K and len(heap)==1:
            return -1
    
    return answer