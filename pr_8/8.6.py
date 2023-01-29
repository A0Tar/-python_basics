"""
Продолжить работу над вторым заданием. Реализуйте механизм валидации вводимых пользователем данных.
Например, для указания количества принтеров, отправленных на склад, нельзя использовать строковый тип данных.
Подсказка: постарайтесь реализовать в проекте «Склад оргтехники» максимум возможностей, изученных на уроках по ООП.
"""
class (Exception):
    def __init__(self, text):
        self.text = text

    def __str__(self):
        return self.text


class AcceptStorehouseError(AppError):
    def __init__(self, text):
        self.text = f"Невозможно добавить товар на склад:\n {text}"


class (AppError):
    def __init__(self, text):
        self.text = f"Ошибка прередачи оборудования:\n {text}"


AddStorehouseError = AcceptStorehouseError


class (AppError):
    pass


class Storehouse:
    def __init__(self):
        self.__storehouse = []

    def add(self, equipments):
        if not all([isinstance(equipment, OfficeEquipment) for equipment in equipments]):
            raise AddStorehouseError(f"Элемент не является оргтехникой")

        self.__storehouse.extend(equipments)

    def transfer(self, idx: int, department: str):
        if not isinstance(idx, int):
            raise TransferStorehouseError(f"Недопустимый тип '{type(item)}'")

        item: OfficeEquipment = self.__storehouse[idx]

        if item.department:
            raise TransferStorehouseError(f"Оборудование {item} уже закреплено за отделом {item.department}")

        item.department = department

    def filter_by(self, **kwargs):
        for id_, item in enumerate(self):
            if all([item.__getattribute__(key) == kwargs[key] for key in kwargs]):
                yield id_, item

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
    __required_props = ("eq_type", "seller", "model")

    def __init__(self, eq_type: str = None, seller: str = "", model: str = ""):
        self.type = eq_type
        self.seller = seller
        self.model = model

        self.department = None

    def __setattr__(self, key, value):
        if key in self.__required_props and not value:
            raise AttributeError(f"'{key}' должен иметь значение отличное от false")

        object.__setattr__(self, key, value)

    def __str__(self):
        return f"{self.type} {self.seller} {self.model}"

    @staticmethod
    def validate(cnt):
        if not isinstance(cnt, int):
            ValidateEquipmentError(f"'{type(cnt)}'; количество инстансов должен быть типа 'int'")

    @classmethod
    def create(cls, cnt, **properties):
        cls.validate(cnt)
        return [cls(**properties) for _ in range(cnt)]


class Printer(OfficeEquipment):
    def __init__(self, **kwargs):
        super().__init__(eq_type='Принтер', **kwargs)


class Scanner(OfficeEquipment):
    def __init__(self, **kwargs):
        super().__init__(eq_type='Сканер', **kwargs)


class Xerox(OfficeEquipment):
    def __init__(self, **kwargs):
        super().__init__(eq_type='МФУ', **kwargs)


if __name__ == '__main__':
    storehouse = Storehouse()
    storehouse.add(Printer.create(4, seller="HP", model="Laser 107a"))
    storehouse.add(Scanner.create(3, seller="Epson", model="Perfection V19"))
    storehouse.add(Scanner.create(2, seller="Canon", model="LiDE 400"))
    storehouse.add(Xerox.create(6, seller="Pantum", model="M6502W"))
    print(storehouse)

    for idx, itm in storehouse.filter_by(department=None, seller="Epson", model="Perfection V19"):
        print(f"Резервируем {itm} в 'Отдел 1'")
        storehouse.transfer(idx, 'Отдел 1')

    for idx, itm in storehouse.filter_by(department=None):
        print(idx, f"{itm} не распределены по отделам")

    print(storehouse)
    print("Списываем 1 устройство")
    del storehouse[0]
    print(storehouse)



