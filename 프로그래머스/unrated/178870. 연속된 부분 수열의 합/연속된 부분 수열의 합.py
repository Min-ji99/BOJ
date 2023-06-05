def solution(sequence, k):
    n=len(sequence)
    answer=[0, n-1]
    
    if sequence[0]==k:
        return [0, 0]
    
    start, end=0, 1
    cur=sequence[start]+sequence[end]
    min_length=n
    while start<=end and start<n and end<n :
        if cur==k :
            if end-start<min_length:
                answer=[start, end]
                min_length=end-start
            cur-=sequence[start]
            start+=1
        elif cur<k:
            end+=1
            if end==n :
                break
            cur+=sequence[end]
        else :
            cur-=sequence[start]
            start+=1

    return answer