import sys
input=sys.stdin.readline

n, m=map(int, input().split())
universities=list(map(str, input().split()))
edges=[]
parent=[x for x in range(n+1)]
total=0
path_cnt=0
def find(parent, node) :
    if parent[node]!=node :
        parent[node]=find(parent, parent[node])
    return parent[node]

def union(parent, node_u, node_v) :
    root1=find(parent, node_v)
    root2=find(parent, node_u)
    if root1<root2 :
        parent[root2]=root1
    else:
        parent[root1]=root2

for _ in range(m) :
    u, v, d=map(int, input().split())
    edges.append([d, u, v])

edges.sort()
for edge in edges :
    cost, a, b=edge
    if find(parent, a)!=find(parent, b) and universities[a-1]!=universities[b-1]:
        path_cnt+=1
        total+=cost
        union(parent, a, b)
if path_cnt==n-1 :
    print(total)
else:
    print(-1)