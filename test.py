
from collections import deque
q = deque()

n, m = map(int, input().split())

miro = []
cnt = 0

for i in range(n):
    a = list(map(int, str(input())))
    miro.append(a)
    
    #왼 오 위 아래
dx = [-1, 1, 0, 0]
dy = [0, 0, 1, -1]

#for i in range(n):
#    for j in range(m):
#        if miro[i][j] == 1:
#            q.append([i,j])
q.append([0,0])

while q:
    [x, y] = q.popleft()
    for i in range(4):
        mx = x + dx[i]
        my = y + dy[i]
        
        if mx < 0 or mx >= n or my < 0 or my >= m:
            continue
        
        if miro[mx][my] == 0:
            continue
        
        if miro[mx][my] == 1:
            miro[mx][my] = miro[x][y] + 1
            q.append([mx, my])
                

print(miro[n-1][m-1])