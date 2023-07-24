import math

abValues = []

def checkRepeat(a, b, arr):
    for s in arr:
        if s == a or s == b:
            return False
    return True

for i in range(1, 10):
    for j in range(1, 10):
        if i != j and ((10*i)+j) < 40:
            abValues.append([i,j])

for a,b in abValues:
    available = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    used = []
    mulavailable = []
    tempused = []

    used.append(a)
    used.append(b)
    available.remove(a)
    available.remove(b)

    for i in range(0,len(available)):
        mulavailable.append(available[i])

    for i in range(0,len(used)):
        tempused.append(used[i])

    for c in mulavailable:
        mulNum = ((10*a)+b) * c
        num = mulNum

        if c != 1 and mulNum < 98 and mulNum % 10 != 0:
            l = mulNum % 10
            mulNum = math.floor(mulNum / 10)
            k = mulNum % 10

            if k != l and checkRepeat(k, l, used) and k != c and l != c:
                used.append(c)
                used.append(k)
                used.append(l)
                available.remove(l)
                available.remove(k)
                available.remove(c)
                mnValues = []

                for i in range(0, len(available)):
                    for j in range(0, len(available)):
                        if available[i] != available[j]:
                            mnValues.append([available[i], available[j]])

                for m,n in mnValues:
                    addNum = num + ((10*m) + n)

                    if addNum < 98 and addNum % 10 != 0:
                        y = addNum % 10
                        addNum = math.floor(addNum / 10)
                        x = addNum % 10
                        if x != y and checkRepeat(x, y, used) and x != m and y != m and x != n and y != n:
                            print(" ",a,b)
                            print(" ","x", c)
                            print(" ",k,l)
                            print(" ",m,n)
                            print(" ",x,y)
                            used.append(m)
                            used.append(n)
                            used.append(x)
                            used.append(y)
                            available.remove(m)
                            available.remove(n)
                            available.remove(x)
                            available.remove(y)
                            print(used)
                            print(available)
                            print("")

                used = []
                available = []

                for i in range(0, len(mulavailable)):
                    available.append(mulavailable[i])

                for i in range(0, len(tempused)):
                    used.append(tempused[i])

## sdfhasldj
