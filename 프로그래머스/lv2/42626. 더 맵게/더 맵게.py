import heapq

def solution(scoville, K):
    answer = 0
    heap=[]
    for i in scoville:
        heapq.heappush(heap,i)
    while heap[0]<K:
        if len(heap)==1:
            return -1
        sco=0
        sco += heapq.heappop(heap)
        sco += 2 * heapq.heappop(heap)
        heapq.heappush(heap, sco)
        answer += 1
    return answer