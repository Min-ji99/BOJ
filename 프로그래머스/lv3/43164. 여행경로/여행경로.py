from collections import deque
from collections import defaultdict

def solution(tickets):
    answer=[]
    #tickets.sort(key = lambda x:(x[1], x[0]))
    #print(tickets)
    graph=defaultdict(list)
    for ticket in tickets :
        graph[ticket[0]].append(ticket[1])
    for ticket in graph.keys():
        graph[ticket].sort(reverse=True)
    def dfs():
        stack=["ICN"]
        while stack :
            start=stack[-1]
            if not graph[start] :
                answer.append(stack.pop())
            else :
                stack.append(graph[start].pop())
    dfs()
    return answer[::-1]