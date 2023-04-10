def solution(skill, skill_trees):
    answer = 0
    
    for skill_tree in skill_trees :
        pos=0
        flag=True
        for i in range(len(skill_tree)) :
            if skill_tree[i] in skill : #해당 스킬이 선행 스킬 순서에 포함되어있는지 확인
                if skill_tree[i] != skill[pos] :
                    flag=False
                    break
                else:
                    pos+=1
        if flag :
            answer+=1
    return answer