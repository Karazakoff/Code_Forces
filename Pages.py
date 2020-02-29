n, p, k = map(int, input().split())
mas = []
for i in range(p , p - k - 1,-1):
    if i == 1:
        mas.append(i)
        break
    else:
        mas.append(i)
mas.reverse()
if mas[-1] != n:    
    for i in range(p + 1, p + k + 1):
        if i == n:
            mas.append(i)
            break
        else:
            mas.append(i)



if mas[0] != 1:
    print("<<", end = " ")

for i in mas:
    if i == p:
        print("({})".format(i), end = " ")
    else:
        print(i, end = " ")

if mas[-1] != n:
    print(">>")
