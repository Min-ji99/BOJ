N=10*3
class Node :
    delete = False
    def __init__(self, p, n) :
        self.prev=p if p>=0 else None
        self.next=n if n<N else None
        
def solution(n, k, cmd):
    answer = ''
    global N
    N=n
    now=k
    stack=[] #삭제된 행
    table=[]
    
    for i in range(n) :
        table.append(Node(i-1, i+1))
        
    for c in cmd :
        if c[0]=="C":
            table[now].delete=True
            stack.append(now)
            prev, next=table[now].prev, table[now].next
            
            if prev!=None  :
                table[prev].next=next
            
            if next!=None :
                table[next].prev=prev
                
            if next !=None:
                now=next
            else:
                now=prev
        elif c[0]=="Z":
            tmp=stack.pop()
            table[tmp].delete=False
            
            prev, next=table[tmp].prev, table[tmp].next
            
            if prev != None:
                table[prev].next=tmp
            
            if next != None:
                table[next].prev=tmp
        else:
            command, num=c.split()
            if command=="D" :
                for _ in range(int(num)):
                    now=table[now].next
            else:
                for _ in range(int(num)):
                    now=table[now].prev
    
    for i in range(n):
        if not table[i].delete :
            answer+='O'
        else:
            answer+='X'
    
    return answer