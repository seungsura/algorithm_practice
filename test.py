import sys
input = sys.stdin.readline
from collections import defaultdict

n, m = map(int, input().split())
list1 = []
list2 = []
dict_list = defaultdict(list)

for i in range(n+m):
    list1.append(str(input()))

for i in list1:
    if i in dict_list:
        dict_list[i] += 1
    else:
        dict_list[i] = 1
        
    if dict_list[i] >= 2:
        list2.append(i)
        
list2.sort()
print(len(list2))
print(''.join(list2), end= '')

