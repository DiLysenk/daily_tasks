"""Вам дано описание наследования классов в следующем формате.
<имя класса 1> : <имя класса 2> <имя класса 3> ... <имя класса k>
Это означает, что класс 1 отнаследован от класса 2, класса 3, и т. д.

Или эквивалентно записи:
class Class1(Class2, Class3 ... ClassK):
    pass
Класс A является прямым предком класса B, если B отнаследован от A:


class B(A):
    pass
Класс A является предком класса B, если
A = B;
A - прямой предок B
существует такой класс C, что C - прямой предок B и A - предок C

Например:
class B(A):
    pass
class C(B):
    pass

# A -- предок С
Вам необходимо отвечать на запросы, является ли один класс предком другого класса
Важное примечание:
Создавать классы не требуется.
Мы просим вас промоделировать этот процесс, и понять существует ли путь от одного класса до другого."""


names = {}
def searchParents(child, parent):
    parents = set()
    def func(child):
        if child not in names: return False
        prts = names[child]
        if len(prts):
            for parent in prts:
                parents.add(parent)
                func(parent)
        else:
            return False
    func(child)
    return parent in parents

for _ in range(int(input())):
    arr = input().split()
    names[arr[0]] = [] if len(arr) == 1 else arr[2:]
for _ in range(int(input())):
    parent, child = input().split()
    print('Yes' if (child == parent and parent in names) or searchParents(child, parent) else 'No')











