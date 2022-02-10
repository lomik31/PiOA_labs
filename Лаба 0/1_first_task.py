from random import randint
c = [[],[],[],[],[]]
d = []
s = 0
def generateList(): # заполняет массив размерами [n][6], где n - длина передаваемого массива
    for i in range(0, len(c)):
        for _ in range(0,6):
            x = randint(99, 1000)
            if x == 99: x = 0
            x /= 100
            c[i].append(x)
def main():
    global c, d, s;
    generateList();
    for i in c:
        if i[5] > 0:
            for j in i:
                s += j
        elif i[5] == 0:
            s = 0
        d.append(round(s, 3))
        s = 0
    print(f"C[5][6] = {c}\n\nD[5] = {d}")
if __name__ == "__main__":
    main();