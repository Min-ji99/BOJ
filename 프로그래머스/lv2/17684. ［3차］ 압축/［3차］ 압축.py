from collections import defaultdict
def solution(msg):
    answer = []
    dictionary=defaultdict(int)
    
    for i in range(26) :
        dictionary[chr(i+65)]=i+1
    
    
    tmp=''
    idx=0
    while idx<len(msg) :
        tmp+=msg[idx]
        if tmp not in dictionary :
            dictionary[tmp]=len(dictionary)+1
            answer.append(dictionary[tmp[:-1]])
            tmp=''
        else:
            idx+=1
            
    answer.append(dictionary[tmp])    
    return answer