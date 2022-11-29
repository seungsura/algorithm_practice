import sys
input = sys.stdin.readline

n = int(input())
matrix = []
visited = [0] * int(n+1)

#ans로 중간에 빠져나가기 & 최솟값처리 생각 못함
ans = 999999999

for i in range(n):
    matrix.append(list(map(int,input().split())))
    
def dfs(start, next, value, visited):
    global ans
    if value > ans:
        return
    
    if sum(visited) == n:
        if matrix[next][start]:
            ans = min(ans, value + matrix[next][start])
    
    for i in range(n):
        if matrix[next][i] != 0 and visited[i] == 0:
            visited[i] = 1
            dfs(start, i, value + matrix[next][i], visited)
            visited[i] = 0
            
for i in range(n):
    visited[i] = 1
    dfs(i,i,0,visited)
    visited[i] = 0
    
    
print(ans)