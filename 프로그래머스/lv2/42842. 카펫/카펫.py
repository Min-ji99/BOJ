import math

def solution(brown, yellow):
    answer = []
    
    S=brown+yellow
    b=(brown+4)/2
    answer=[(b+math.sqrt(b**2-4*S))/2, (b-math.sqrt(b**2-4*S))//2]
    return answer