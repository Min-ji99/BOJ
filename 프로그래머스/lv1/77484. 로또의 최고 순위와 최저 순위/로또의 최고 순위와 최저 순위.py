def solution(lottos, win_nums):
    answer = []

    zero=lottos.count(0)
    correct=0
    for lottos in lottos :
        if lottos in win_nums :
            correct+=1
    
    worst=7-correct
    best=7-correct-zero
    if best>6:
        best=6
    elif best<1:
        best=1
        
    if worst>6 :
        worst=6
    elif worst<1:
        worst=1
    return [best, worst]