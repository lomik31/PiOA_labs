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
    list = noName(countValues(generateList(15)))
    if list == []: print("Нет повторяющихся значений")
    else: print(max(list))
if __name__ == "__main__":
    main()