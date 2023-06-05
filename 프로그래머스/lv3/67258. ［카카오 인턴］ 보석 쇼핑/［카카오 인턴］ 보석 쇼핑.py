def solution(gems):
    answer=[1, len(gems)]
        
    kinds=len(set(gems)) #보석 종류 개수
    n=len(gems)
    start, end=0, 0
    windows={gems[0]:1} # 구간 내의 보석 종류 count
    
    while start<n and end<n :
        if len(windows)== kinds:
            if end-start<answer[1]-answer[0]:
                answer=[start+1, end+1]
            else:
                windows[gems[start]]-=1
                if windows[gems[start]]==0 :
                    del windows[gems[start]]
                start+=1
        else:
            end+=1
            if end==n:
                break
            windows[gems[end]]=windows.get(gems[end], 0)+1
    return answer