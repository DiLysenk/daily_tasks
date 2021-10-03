"""
Вам дается последовательность целых чисел и вам нужно ее обработать и вывести на экран сумму первой пятерки чисел из
 этой последовательности, затем сумму второй пятерки, и т. д.

Но последовательность не дается вам сразу целиком. С течением времени к вам поступают её последовательные части.
Например, сначала первые три элемента, потом следующие шесть, потом следующие два и т. д.

Реализуйте класс Buffer, который будет накапливать в себе элементы последовательности и выводить сумму пятерок
 последовательных элементов по мере их накопления.

Одним из требований к классу является то, что он не должен хранить в себе больше элементов, чем ему действительно
необходимо, т. е. он не должен хранить элементы, которые уже вошли в пятерку, для которой была выведена сумма.


"""
import pytest


class Buffer:

    def __init__(self):
        self.buffer_1 = []

    def add(self, *input_data):
        for i in input_data:
            self.buffer_1.append(i)
        for i in range(len(self.buffer_1) // 5):
            if len(self.buffer_1) >= 5:
                print(sum(self.buffer_1[:5]))
                self.buffer_1 = self.buffer_1[5:]

    def get_current_part(self):
        print(self.buffer_1)


# вернуть сохраненные в текущий момент элементы последовательности в порядке, в котором они были
# добавлены


@pytest.fixture
def buffer():
    program = Buffer()
    return program


@pytest.mark.parametrize('a, b, c, v, result', [(1, 3, 4, 6, 14)])
def test_buffer(buffer, a, b, c, v, result):
    assert buffer.add(a, b, c, v) == result
