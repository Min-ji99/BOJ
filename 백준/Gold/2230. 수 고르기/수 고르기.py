import sys

n, m=map(int, input().split())

arr=[int(input()) for _ in range(n)]
arr.sort()

start=0
end=1
ans=sys.maxsize
while end<len(arr):
    diff=arr[end]-arr[start]
    if diff==m :
        ans=diff
        break
    if diff<m :
        end+=1
        continue
    start+=1
    ans=min(ans, diff)
print(ans)