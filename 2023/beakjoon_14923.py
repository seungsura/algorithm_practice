import sys
input = sys.stdin.readline
from collections import deque

q = deque()

n, m = map(int, input().split())

miro = []

#상하좌우
dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]

for i in range(n):
    a = list(map(int, input().strip()))
    miro.append(a)

def bfs(miro, x, y):
    
    q.append((x, y))
    
    while q:
        x, y = q.popleft()
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue

            if miro[nx][ny] == 0:
                continue

            if miro[nx][ny] == 1:
                miro[nx][ny] = miro[x][y] + 1
                q.append((nx, ny))
                
    return miro[n-1][m-1]

print(bfs(miro, 0, 0))