import sys
input = sys.stdin.readline

x, y = 0, 0
ans = 0

for i in range(9):
    a = list(map(int, input().split()))
    b = max(a)
    if b > ans:
        ans = b
        x = i
        y = a.index(b)

print(ans)
print(x+1, y+1)