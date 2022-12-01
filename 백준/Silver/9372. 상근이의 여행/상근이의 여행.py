import sys
input=sys.stdin.readline

t=int(input())
def find(parent, node):
    if parent[node]!=node :
        parent[node]=find(parent, parent[node])
    return parent[node]

def union(parent, node_v, node_e) :
    root1 = find(parent, node_v)
    root2 = find(parent, node_e)
    if root1 < root2:
        parent[root2] = root1
    else:
        parent[root1] = root2

for _ in range(t) :
    n, m=map(int, input().split())
    parent=[x for x in range(n+1)]
    total_cost=0
    edges=[list(map(int, input().split())) for _ in range(m)]

    for i in range(m) :
        a, b=edges[i]
        if find(parent, a)!=find(parent, b) :
            union(parent, a, b)
            total_cost+=1
    print(total_cost)
