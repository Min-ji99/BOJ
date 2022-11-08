
import math, sys

x, y=map(int, input().split())
z=100*y//x
if z>=99:
    print(-1)
else:
    start=1
    end=sys.maxsize
    while start<=end:
        mid=(start+end)//2
        rate=100*(y+mid)//(x+mid)
        if z<rate:
            end=mid-1
        else :
            start=mid+1
    print(end+1)