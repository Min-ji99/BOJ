def solution(order):
    answer = 0
    stack=[]
    i=1
    
    while i!=len(order)+1 :
        stack.append(i)
        while stack and stack[-1] == order[answer] :
            stack.pop()
            answer+=1
        i+=1
    return answer