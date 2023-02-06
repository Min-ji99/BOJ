import math

def isPrime(num):
    if(num==1 or num==0) : return False

    for i in range(2, int(math.sqrt(num))+1):
        if(num%i==0) : return False

    return True
def solution(n, k):
    answer=0
    strs=''

    #n을 k진수 문자열로 변환
    while (n!=0) :
        strs=str(n%k)+strs
        n=n//k

    #0을 기준으로 split
    strs=strs.split("0")
    for s in strs :
        if(len(s)==0) : continue
        num=int(s)
        if(isPrime(num)) :
            answer+=1

    return answer