from math import sqrt;
def distance(x1, y1, x2, y2):
    return sqrt((x1 - x2)**2 + (y1 - y2)**2);

def main():
    print(distance(0.0, 0.0, 1.0, 1.0)) 
if __name__ == "__main__":
    main()