"""
Начните работу над проектом «Склад оргтехники». Создайте класс, описывающий склад. А также класс «Оргтехника»,
который будет базовым для классов-наследников. Эти классы — конкретные типы оргтехники (принтер, сканер, ксерокс).
В базовом классе определите параметры, общие для приведённых типов. В классах-наследниках реализуйте параметры,
уникальные для каждого типа оргтехники.
"""
class Storehouse:
    pass


class OfficeEquipment:
    vat = 0.13
    added_value = 2.0
    retail_rate = 1.3

    def __init__(
            self,
            eq_type: str,
            seller: str,
            model: str,
            color: str,
            cost: float,
    ):
        self.type = eq_type
        self.seller = seller
        self.model = model
        self.color = color

        self.cost = cost

        self.printable = True if self.type in ("printer", "xerox") else False
        self.scannable = True if self.type in ("scanner", "xerox") else False

    @property
    def retail_price(self):
        return self.wholesale_price * self.retail_rate

    @property
    def wholesale_price(self):
        return self.cost * (1 + self.vat) * (1 + self.added_value)

    def __str__(self):
        return f"{self.type} {self.seller} {self.model} ({self.color})"


class Printer(OfficeEquipment):
    printable = True
    scannable = False

    def __init__(self, *args):
        super().__init__('Принтер', *args)


class Scanner(OfficeEquipment):
    printable = False
    scannable = True

    def __init__(self, *args):
        super().__init__('Сканер', *args)


class Xerox(OfficeEquipment):
    printable = True
    scannable = True

    def __init__(self, *args):
        super().__init__('МФУ', *args)


if __name__ == '__main__':
    p1 = Printer("HP", "Laser 107a", "white", 11499)
    print(p1)
    p2=Xerox("Pantum", "M6502W", "black", 12499)
    print(p2)
    p3 = Scanner("Epson", "Perfection V19", "black", 14795)
    print(p3)


