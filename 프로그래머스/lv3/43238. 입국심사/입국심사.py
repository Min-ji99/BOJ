def solution(n, times) :
    start=0
    end=n*max(times)
    while start<=end :
        mid=(start+end)//2
        total=0
        for time in times :
            total+=mid//time
        if total>=n :
            end=mid-1
        else:
            start=mid+1
    return start