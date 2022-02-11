import datetime
class WORKER:
    def __init__(self, SN_INITs: str, post: str, YAW: int) -> None:
        self.fullName = SN_INITs;
        self.post = post;
        self.year = YAW;
        return;
ls = []
def atl():
    global ls;
    for _ in range(0,10):
        ls.append(WORKER(input("Введите Фамилию ИО: "), input("Введите занимаемую должность: "), int(input("Введите год начала работы: "))))
def main():
    global ls;
    atl();
    print(ls);
    year = datetime.date.today().year - int(input("Введите стаж работы: "));
    for i in ls:
        if year > i.year: print(i.fullName)
if __name__ == "__main__":
    main();