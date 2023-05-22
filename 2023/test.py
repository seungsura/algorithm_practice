import sys
from collections import deque
input = sys.stdin.readline

# N * M
N, M = map(int, input().split())

# 미로 맵
Map = []

# 미로 입력받기
for i in range(N):
    Map.append([int(j) for j in input().rstrip()])

# 동서남북, 인접한 위치로 이동
dx = [0, 0, 1, -1]
dy = [-1, 1, 0, 0]

# 너비 우선 탐색
def bfs(x, y):
    queue = deque()
    queue.append([x, y])

    while queue:
        [x, y] = queue.popleft()
        # 이동
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            # 범위 안에 있고, 이동할 수 있는 칸일 때
            if 0 <= nx < N and 0 <= ny < M and Map[nx][ny] == 1:
                Map[nx][ny] += Map[x][y]
                # queue에 추가
                queue.append([nx, ny])

bfs(0, 0)
print(Map[N-1][M-1])