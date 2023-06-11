def solution(elements):
    answer = set()
    cycle=elements+elements
    
    for i in range(len(elements)) :
        for j in range(len(elements)) :
            answer.add(sum(cycle[i:i+j]))
            
    return len(answer)