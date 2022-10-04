import sys

n = int(input())
timetable = [[0]*2 for i in range(n)]
for i in range(n) :
  s, f = map(int, sys.stdin.readline().split())
  timetable[i][0]=s
  timetable[i][1]=f

timetable.sort(key=lambda x:(x[1], x[0]))
cnt = 1
end_time = timetable[0][1]
for i in range(1, n) :
  if timetable[i][0] >= end_time :
    cnt+=1
    end_time=timetable[i][1]
print(cnt)