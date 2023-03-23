'''
동일한 가짓수의 토핑
'''
def solution(topping):
    answer = 0
    A_dict={}
    B_dict={}
    A_dict[topping[0]]=1
    
    if len(topping)==1 : return answer

    for t in topping[1:] :
        B_dict[t]=B_dict.get(t, 0)+1
    
    if len(B_dict)==len(A_dict) :
            answer+=1
            
    for i in range(1, len(topping)) :
        if B_dict[topping[i]]>1 :
            B_dict[topping[i]]-=1
        elif B_dict[topping[i]]==1 :
            del B_dict[topping[i]]
        A_dict[topping[i]]=A_dict.get(topping[i], 0)+1
        if len(B_dict)==len(A_dict) :
            answer+=1
        
        
    return answer