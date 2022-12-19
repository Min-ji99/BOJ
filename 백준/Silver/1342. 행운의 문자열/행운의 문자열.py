s=input().rstrip()
alphabets={}

for ch in s:
    alphabets[ch]=alphabets.get(ch, 0)+1

def dfs(str) :
    if len(str)==len(s) : return 1
    answer=0
    for key in alphabets.keys() :
        if len(str)>0 and str[-1] ==key :
            continue

        if alphabets[key]==0 :
            continue
        alphabets[key]-=1
        answer+=dfs(str+key)
        alphabets[key]+=1
    return answer

answer=dfs('')
print(answer)