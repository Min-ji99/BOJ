'''
누적합
'''
import sys

input=sys.stdin.readline
n=int(input())
weights=list(map(int, input().split()))
weights.sort()

target=1
for weight in weights:
    if target<weight:
        break
    target+=weight
print(target)
