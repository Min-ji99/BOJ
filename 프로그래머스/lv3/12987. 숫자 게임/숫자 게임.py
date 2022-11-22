def solution(A, B):
    answer = 0
    A.sort()
    B.sort()
    idx=len(B)-1
    for i in range(len(A)-1, -1, -1):
        if A[i] < B[idx]:
            answer+=1
            idx-=1
    return answer