N = int(input())
m1 = [x for x in input("").split()]
m2 = [x for x in input("").split()]
l1 = []
l2 = []
for i in range(1, len(m1)):
    h = m1[i]
    l1.append(int(h))
for j in range(1, len(m2)):
    h = m2[i]
    l2.append(int(h))
print(l1)
print(l2)
for i1 in l1:
    for j1 in l2:
        a = (i1+j1) / 2
    print("{h2:1.2f}".format(h2=a), end=" ")
