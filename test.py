import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**7)

t = int(input())

def dfs(now):
    visited[now] = 1
    next = arr[now]
    if visited[now] == 0:
        dfs(next)
        
for i in range(t):
    ans = 0
    n = int(input())
    arr = [0] + list(map(int, input().split()))
    visited = [0] * (n+1)
    
    for i in range(1, n+1):
        if visited[i] == 0:
            dfs(i)
            ans += 1
            
    pinrt(ans)
    