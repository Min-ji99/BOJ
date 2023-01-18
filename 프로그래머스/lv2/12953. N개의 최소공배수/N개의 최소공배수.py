from math import gcd  #최대공약수
def lcm(a,b):
    return (a*b)//gcd(a,b)
def solution(arr):
    answer = 0
    while len(arr)>1:
        arr.append(lcm(arr.pop(0),arr.pop(0)))
    return arr[0]