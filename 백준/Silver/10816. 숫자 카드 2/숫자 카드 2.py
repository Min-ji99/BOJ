import sys
input=sys.stdin.readline

n=int(input())
cards=list(map(int, input().split()))
m=int(input())
findCards=list(map(int, input().split()))
cards.sort()

cnt_dict={}
for card in cards:
    if card in cnt_dict:
        cnt_dict[card]+=1
    else:
        cnt_dict[card]=1

def binarySearch(start, end, target, arr):
    if start>end:
        return 0
    mid=(start+end)//2
    if target==arr[mid]:
        return cnt_dict[target]
    elif target>arr[mid] :
        return binarySearch(mid+1, end, target, arr)
    else:
        return binarySearch(start, mid-1, target, arr)

for target in findCards:
    print(binarySearch(0, len(cards)-1, target, cards), end=' ')
