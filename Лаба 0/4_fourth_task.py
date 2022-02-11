import json
class BOOK:
    def __init__(self, SN_INITs: str, name: str, publisher: str, year: int,
    pagesCount: int, chaptersCount: int, topic: str):
        self.name = name;
        self.topic = topic;
        self.authorName = SN_INITs;
        self.publisher = publisher;
        self.year = year;
        self.pages = pagesCount;
        self.chapters = chaptersCount;
def readFile():
    with open("Лаба 0/files/test.json", encoding="utf-8") as doc:
        doc = json.load(doc);
    return doc;
def writeFile(toWrite):
    with open('Лаба 0/files/test.json', 'w', encoding="utf-8") as outfile:
        json.dump(toWrite, outfile, ensure_ascii=False, indent=4)
def generateFile():
    bks = [];
    bks.append(BOOK("ldn", "svr", "lkvnfv", 1932, 144, 5, "lrnf"));
    bks.append(BOOK("kfj", "ewf", "sdv", 2007, 561, 1, "sklnc"));
    bks.append(BOOK("jkbsvk", "aef", "sdvsdv", 2001, 311, 2, "kjsdnf"));
    bks.append(BOOK("ksdjbvf", "sdm v", "sdvm", 1816, 680, 1, "lrnf"));
    bks.append(BOOK("kjsndv", "sd dcmk", "sdvsv", 1986, 421, 3, "eklfnj"));
    bks.append(BOOK("ksjdbvn", "ssdklc", "sdklvn", 1998, 767, 1, "kjsdnf"));
    bks.append(BOOK("ksjdv", "lkvns", "wqof", 1912, 30, 1, "kenf"));
    bks.append(BOOK("ksdv", "kldms", "lkvnfv", 2015, 1024, 2, "sleknf"));
    doc = [];
    for i in bks:
        doc.append(eval(json.dumps(i.__dict__)))
    writeFile(doc);
def printAllFile():
    file = readFile();
    for i in file:
        print(i);
def findBooks(file, pages: int, chapters: int) -> list:
    b = [];
    for i in file:
        if i["pages"] >= pages and i["chapters"] >= chapters:
            b.append(i);
    return b;
def printFoundBooks(list: list):
    message = f"Найдено {len(list)} подходящих книг, вот их список:";
    for i in list:
        message += f"\n{i}";
    print(message);
def main():
    printAllFile();
    printFoundBooks(findBooks(readFile(), int(input("Введите минимальное число страниц для поиска: ")),
    int(input("Введите минимальное число глав для поиска: "))));

if __name__ == "__main__":
    main();