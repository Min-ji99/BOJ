'''
1. 순열 이용
-> 효율성 문제
2. factorial 이용
'''
from math import factorial

def solution(n, k):
    nums=[i for i in range(1, n+1)]
    stack=[]

    while n!=0:
        num=k//factorial(n-1)
        k=k%factorial(n-1)
        if k==0 :
            stack.append(nums.pop(num-1))
        else:
            stack.append(nums.pop(num))
        n-=1

    return stack