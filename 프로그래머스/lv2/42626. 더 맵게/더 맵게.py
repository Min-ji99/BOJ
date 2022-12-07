import heapq

def solution(scoville, K):
    heap=[]
    answer=0
    for s in scoville :
        heapq.heappush(heap, s)
    while heap[0]<K :
        if len(heap)==1 :
            return -1
        a=heapq.heappop(heap)
        b=heapq.heappop(heap)
        heapq.heappush(heap, a+b*2)
        answer+=1
    return answer