from bisect import bisect_left
import sys
input=sys.stdin.readline

n=int(input())
arr=list(map(int, input().split()))
dp=[1]*n

#dp + 이진 탐색
x=[arr[0]]
for i in range(n):
    if x[-1]<arr[i]:
        x.append(arr[i])
        dp.append(dp[-1]+1)
    else:
        index=bisect_left(x, arr[i])
        x[index]=arr[i]
print(dp[-1])

