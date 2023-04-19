from itertools import combinations

def solution(relation):
    answer = []
    candidate_key=[]
    col=len(relation[0])
    row=len(relation)
    #유일성
    for i in range(1, col+1) :
        for comb in combinations(range(col), i) :
            tmp = [tuple(record[c] for c in comb) for record in relation]
            if len(set(tmp))==row : #최소성
                put=True
                for x in candidate_key :
                    if set(x).issubset(set(comb)) :
                        put=False
                        break
                if put :
                    candidate_key.append(comb)
    #candidate_key.sort()
    #print(candidate_key)
    
    #최소성
    '''
    for i in range(len(candidate_key)) :
        idx=i+1
        while idx<len(candidate_key) :
            if candidate_key[i][0]==candidate_key[idx][0] :
                candidate_key.pop(idx)
            else:
                break
    #print(candidate_key)
    '''
    return len(candidate_key)