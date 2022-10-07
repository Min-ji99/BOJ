import sys
input=sys.stdin.readline
n=int(input())
crains=list(map(int, input().split()))
m=int(input())
boxs=list(map(int, input().split()))

crains.sort(reverse=True)
boxs.sort(reverse=True)
ans=0

if crains[0]<boxs[0]: #무게가 제일 많이 나가는 박스 무게가 크레인이 가능한 무게보다 큰 경우
    print(-1)
    exit()
else:
    while len(boxs)>0 :
        for crain in crains:
            for box in boxs:
                if crain>=box :
                    boxs.remove(box)
                    break
        ans+=1
    print(ans)



