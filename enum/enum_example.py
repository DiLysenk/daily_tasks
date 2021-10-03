# exampl
from enum import Enum, auto, unique


class Pi(Enum):

    add_locator = (0, "Добавили")
    save_locator = (1, "сохранили")
    cancel_locator = (2, "отменили")
    locator = auto()



class Mi(Enum, Pi):

    @staticmethod
    def show_enum(locator):
        print(locator)




Mi.show_enum(Pi.add_locator)



print(Pi.add_locator.value)
print(Pi.save_locator.name)
print(Pi.locator.value)
print(Pi.locator.name)



i = "hfqwiluefhqliwef"

i.split()

