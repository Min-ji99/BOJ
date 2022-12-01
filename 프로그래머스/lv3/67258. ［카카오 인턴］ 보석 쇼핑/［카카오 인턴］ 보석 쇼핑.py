def solution(gems) :
    answer=[0, len(gems)-1]
    gem_cnt=len(set(gems))
    gem_dic={gems[0]:1}
    start, end=0, 0
    while start<len(gems) and end<len(gems) :
        if len(gem_dic)==gem_cnt :
            if (end-start)<answer[1]-answer[0] :
                answer=[start, end]
            if gem_dic[gems[start]]==1 :
                del gem_dic[gems[start]]
            else:
                gem_dic[gems[start]]-=1
            start+=1
        else:
            end+=1
            if end==len(gems):
                break
            gem_dic[gems[end]]=gem_dic.get(gems[end], 0)+1
    answer[0]+=1
    answer[1]+=1
    return answer