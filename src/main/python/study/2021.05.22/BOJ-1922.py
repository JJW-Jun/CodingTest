
import sys
input = sys.stdin.readline


N = int(input())
M = int(input())
graph = []
parent =[0]*(N+1)

for i in range(1, N+1) :
    parent[i] = i

for i in range(1, M+1) :
    a, b, cost = map(int, input().split())
    graph.append((cost, a, b))

def find_parent(parent, x) :
    if parent[x] != x :
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

def union_parent(parent, x, y) :
    a = find_parent(parent, x)
    b = find_parent(parent, y)

    if a < b :
        parent[b] =a
    else :
        parent[a] =b


graph.sort()
result = 0
for edge in graph :
    cost, a, b = edge
    if find_parent(parent, a) != find_parent(parent, b) :
        union_parent(parent, a, b)
        result += cost
print(result)

# 유니온을 덮어서 할 수 도 있다.
# 두 정점 사이에 간선이 하나라고 가정을 한다.
# 간선이 여러개일 때를 검증 안 했다.
