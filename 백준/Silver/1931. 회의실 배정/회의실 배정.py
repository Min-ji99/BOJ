import sys
input=sys.stdin.readline
n=int(input())

timetables=[list(map(int, input().split())) for _ in range(n)]
timetables.sort(key=lambda x:(x[1], x[0]))
ans=1
end_time=timetables[0][1]
for i in range(1, len(timetables)) :
    if timetables[i][0]>=end_time:
        ans+=1
        end_time=timetables[i][1]
print(ans)