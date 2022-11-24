a = [1,2,3,4,5]
b = [2,4,6,7]
c = [1,2,3]

d = list(set(a) - set(b))
d.sort(reverse= True)
c += d


print(c)