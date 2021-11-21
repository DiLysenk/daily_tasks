"""
Реализуйте класс PositiveList, отнаследовав его от класса list, для хранения положительных целых чисел.
Также реализуйте новое исключение NonPositiveError.

В классе PositiveList переопределите метод append(self, x) таким образом,
чтобы при попытке добавить неположительное целое число бросалось исключение NonPositiveError и число не добавлялось,
а при попытке добавить положительное целое число, число добавлялось бы как в стандартный list.

В данной задаче гарантируется, что в качестве аргумента x метода append всегда будет передаваться целое число.

Примечание:
Положительными считаются числа, строго большие нуля.
"""
import simplecrypt
import urllib.request as urllib

class NonPositiveError(Exception):
    pass


class PositiveList(list):
    def append(self, x):
        if x <= 0:
            raise NonPositiveError
        super(PositiveList, self).append(x)




passwords = urllib.urlopen('https://stepik.org/media/attachments/lesson/24466/passwords.txt')

with open('encrypted.bin', 'rb') as inp:
    encrypted = inp.read()

for password in passwords:
    password = password[:-1]
    try:
        print(simplecrypt.decrypt(password, encrypted).decode('utf8'))
    except simplecrypt.DecryptionException:
        print(password, 'is wrong')
    else:
        print(password, 'is correct')