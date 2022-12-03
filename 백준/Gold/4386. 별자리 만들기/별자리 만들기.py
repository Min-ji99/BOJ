import sys, math

input=sys.stdin.readline
n=int(input())
stars=[list(map(float, input().split())) for _ in range(n)]

parent=[x for x in range(n+1)]
total_cost=0
graph=[]
for i in range(n-1) :
    for j in range(i, n) :
        cost=math.sqrt((stars[i][0]-stars[j][0])**2+(stars[i][1]-stars[j][1])**2)
        graph.append([cost, i, j])

def find(parent, node):
    if parent[node]!=node :
        parent[node]=find(parent, parent[node])
    return parent[node]

def union(parent, node_v, node_e):
    root1=find(parent, node_v)
    root2=find(parent, node_e)
    if root1<root2 :
        parent[root2]=root1
    else:
        parent[root1]=root2

graph.sort()
for i in graph :
    cost, a, b=i
    if find(parent, a)!=find(parent, b):
        union(parent,a, b)
        total_cost+=cost

print(round(total_cost, 2))