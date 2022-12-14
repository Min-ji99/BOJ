from itertools import permutations

n, m=map(int, input().split())
nums=[x+1 for x in range(n)]
lists=permutations(nums, m)

for idx, lst in enumerate(lists) :
    print(*lst)