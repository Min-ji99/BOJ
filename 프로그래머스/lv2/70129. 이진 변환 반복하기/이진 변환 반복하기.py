def solution(s):
    answer = []
    
    cnt=0
    zero=0
    
    if s=='1' :
        return [0, 0]
    
    while True:
        cnt+=1
        zero+=s.count('0')
        s=s.replace('0', '')
        s=bin(len(s))[2:]
        if s=='1':
            break
    return [cnt, zero]