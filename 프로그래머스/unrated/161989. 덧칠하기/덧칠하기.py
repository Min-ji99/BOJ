def solution(n, m, section):
    answer = 0
    current=0
    for s in section :
        if s>=current :
            answer+=1
            current=s+m
        
    return answer