class Student:
    def __init__(self, number:int, lastName: str, marks: dict) -> None:
        self.number = number
        self.lastName = lastName
        self.marks = marks
def readFile(path):
    file = open(path, "r")
    f = file.read()
    file.close()
    f = f.split("\n")
    return f
def generateDict(file):
    students = []
    for i in file:
        students.append(Student(i[:2], i[3:22].replace(" ", ""), [int(i[23:24]), int(i[25:26]), int(i[27:28]), int(i[29:30])]))
    return students
def calcMidValue(dict):
    midMark = 0
    n = 0
    for i in dict:
        for j in i.marks:
            n += 1
            midMark += j
    return midMark / n
def writeMidMark(midMark, path):
    file = open(path, "w")
    file.write(str(midMark))
    file.close()
def main():
    writeMidMark(calcMidValue(generateDict(readFile("files/Task4.in"))), "files/Task4.out")
if __name__ == "__main__":
    main()