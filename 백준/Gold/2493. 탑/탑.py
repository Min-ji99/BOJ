import sys

input=sys.stdin.readline

n=int(input())
heights=list(map(int, input().split()))

ans=[0]*n
stack=[] #탑의 index 저장
for i in range(n) :
    cur_height=heights[i] #현재 높이
    while stack :
        if heights[stack[-1]]<cur_height : #현재 탑에서 발사된 레이저가 안닿으면
            stack.pop()
        else:
            break
    if stack:
        ans[i]=stack[-1]+1
    stack.append(i)

print(' '.join(map(str, ans)))