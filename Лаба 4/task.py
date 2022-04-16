file = open("Лаба 4/files/Task8.in", "r")
f = file.read()
file.close()
f = [v for v in f.replace("\t", " ").replace("\n", " ").split(" ") if v]
print(f)