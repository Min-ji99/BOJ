import sys
input=sys.stdin.readline

n=int(input())
numbers=[input().strip() for _ in range(n)]

def sum_of_num(num):
    result=0
    for i in num:
        if i.isdigit():
            result+=int(i)
    return result

numbers.sort(key=lambda x:(len(x), sum_of_num(x), x)) #길이 순으로 정렬

print(*numbers)