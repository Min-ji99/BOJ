import math
import sys


input=sys.stdin.readline

N=int(input())
ranks=[int(input()) for _ in range(N)]

ranks.sort()
ans=0
for i in range(N-1, -1, -1) :
    ans+=abs(ranks[i]-(i+1))

print(ans)
