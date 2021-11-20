import time


class Loggable:
    def log(self, msg):
        print(str(time.ctime()) + ": " + str(msg))


"""
У него есть ровно один метод log, который позволяет выводить в лог (в данном случае в stdout) какое-то сообщение, добавляя при этом текущее время.
Реализуйте класс LoggableList, отнаследовав его от классов list и Loggable таким образом, чтобы при добавлении элемента в список посредством метода append в лог отправлялось сообщение, состоящее из только что добавленного элемента.

Примечание
Ваша программа не должна содержать класс Loggable. При проверке вашей программе будет доступен этот класс, и он будет содержать метод log, описанный выше.

"""


class LoggableList(list, Loggable):

    def append(self, y):
        super(LoggableList, self).append(y)
        self.log(y)


if __name__ == "__main__":
    test = LoggableList()
    test.append(2)  # Tue Nov  9 22:22:22 2021: 2
    test.append(3)  # Tue Nov  9 22:22:22 2021: 3
    print(test)  # [2, 3]
