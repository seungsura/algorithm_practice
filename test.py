import sys
input = sys.stdin.readline

n = int(input())
a = []

for _ in range(n):
    a.append(list(map(int, input().split())))

a = sorted(a, key = lambda x: (x[0], x[1]))

end = 0
cnt = 1

for i in range(n):
    if a[i][0] >= end:
        cnt += 1
        end = a[i][1]
        
print(cnt)
