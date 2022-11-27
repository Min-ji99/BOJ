from itertools import permutations
import math

def isPrime(n) :
    if n==0 or n==1 :
        return False
    for i in range(2, int(math.sqrt(n))+1):
        if n%i==0 :
            return False
    return True

def solution(numbers):
    answer=[]
    numbers=list(map(int, numbers))
    for i in range(1, len(numbers)+1) :
        nums=list(set(permutations(numbers, i)))

        for num in nums :
            number=int(''.join(map(str, num)))
            if isPrime(number) :
                answer.append(number)
    return len(set(answer))