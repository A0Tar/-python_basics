"""
Продолжить работу над первым заданием. Разработайте методы, которые отвечают за приём оргтехники на склад и передачу
в определённое подразделение компании. Для хранения данных о наименовании и количестве единиц оргтехники,
а также других данных, можно использовать любую подходящую структуру (например, словарь).
"""

class StorehouseError(Exception):
    def __init__(self, text):
        self.text = text

    def __str__(self):
        return self.text


class AddStorehouseError(StorehouseError):
    def __init__(self, text):
        self.text = f"Невозможно добавить товар на склад:\n {text}"


class TransferStorehouseError(StorehouseError):
    def __init__(self, text):
        self.text = f"Ошибка прередачи оборудования:\n {text}"


class Storehouse:
    def __init__(self):
        self.__storehouse = []

    def add(self, item: "OfficeEquipment"):
        if not isinstance(item, OfficeEquipment):
            raise AddStorehouseError(f"{item} не оргтехника")

        self.__storehouse.append(item)

    def transfer(self, idx: int, department: str):
        if not isinstance(idx, int):
            raise TransferStorehouseError(f"Недопустимый тип '{type(item)}'")

        item: OfficeEquipment = self.__storehouse[idx]

        if item.department:
            raise TransferStorehouseError(f"Оборудование {item} уже закреплено за отделом {item.department}")

        item.department = department

    def filter_by(self, **kwargs):
        for idx, item in enumerate(self):
            a: OfficeEquipment = item
            if all([a.__getattribute__(key) == kwargs[key] for key in kwargs]):
                yield idx, item

    def __getitem__(self, key):
        if not isinstance(key, int):
            raise TypeError

        return self.__storehouse[key]

    def __delitem__(self, key):
        if not isinstance(key, int):
            raise TypeError

        del self.__storehouse[key]

    def __iter__(self):
        return self.__storehouse.__iter__()

    def __str__(self):
        return f"На складе сейчас {len(self.__storehouse)} устройств"


class OfficeEquipment:
    def __init__(
            self,
            eq_type: str,
            seller: str,
            model: str,
    ):
        self.type = eq_type
        self.seller = seller
        self.model = model

        self.department = None

    def __getattribute__(self, name):
        return object.__getattribute__(self, name)

    def __str__(self):
        return f"{self.type} {self.seller} {self.model}"


class Printer(OfficeEquipment):
    def __init__(self, *args):
        super().__init__('Принтер', *args)


class Scanner(OfficeEquipment):
    def __init__(self, *args):
        super().__init__('Сканер', *args)


class Xerox(OfficeEquipment):
    def __init__(self, *args):
        super().__init__('МФУ', *args)


if __name__ == '__main__':
    storehouse = Storehouse()
    storehouse.add(Printer("HP", "Laser 107a"))
    storehouse.add(Scanner("Epson", "Perfection V19"))
    storehouse.add(Xerox("Pantum", "M6502W"))
    print(storehouse)

    last_idx = None
    for idx, itm in storehouse.filter_by(department=None):
        print(idx, itm)
        last_idx = idx

    print("Передаем 1 устройство")
    storehouse.transfer(last_idx, 'Отдел 1')

    for idx, itm in storehouse.filter_by(department=None):
        print(idx, itm)

    print(storehouse)
    print("Удаляем 1 устройство")
    del storehouse[last_idx]
    print(storehouse)


