import sys
input = sys.stdin.readline

n, m = map(int, input().split())
li1 = []
li2 = []

for i in range(n):
    a = list(map(int, input().split()))
    li1.append(a)

for i in range(n):
    a = list(map(int, input().split()))
    li2.append(a)

for i in range(n):
    for j in range(m):
        print(li1[i][j] + li2[i][j], end=' ')
    print(' ')