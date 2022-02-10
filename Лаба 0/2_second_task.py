from random import randint
s = [[],[],[],[],[]]
x = [[],[],[],[],[]]
a_s, a_x = None, None;
def generateList(ls: list): # заполняет массив размерами [n][5], где n - длина передаваемого массива
    for i in range(0, len(ls)):
        for _ in range(0,5):
            x = randint(-999, 1000);
            x /= 100;
            ls[i].append(x);
    return ls;
def checkList(ls: list): # сравнивает количество положительных и отрицательных чисел в массиве
    positive = 0;
    negative = 0;
    for i in ls:
        for j in i:
            if j < 0: negative += 1;
            else: positive += 1;
    if positive > negative: a = 1;
    else: a = 0;
    return a;
def main():
    global s, x, a_s, a_x;
    s = generateList(s);
    x = generateList(x);
    a_s = checkList(s);
    a_x = checkList(x);
    print(f"S[5][5] = {s}\n\nX[5][5] = {x}\n\na_s = {a_s}\n\na_x = {a_x}")

if __name__ == "__main__":
    main();