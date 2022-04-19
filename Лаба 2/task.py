from collections import Counter
from random import randint
def generateList(len):
    ls = []
    for _ in range(0, len):
        ls.append(randint(-15, 15))
    return ls
def countValues(list):
    counter = dict(Counter(list))
    return counter
def noName(dict):
    list = []
    for i in dict.keys():
        if dict[i] > 1:
            list.append(i)
    return list
def main():
    ls = generateList(15)
    list = noName(countValues(ls))
    if list == []: print(f"Вектор: {ls}\nНет повторяющихся значений")
    else: print(f"Вектор: {ls}\n{max(ls)}")
if __name__ == "__main__":
    main()