"""
Создайте собственный класс-исключение, обрабатывающий ситуацию деления на ноль.
Проверьте его работу на данных, вводимых пользователем. При вводе нуля в качестве делителя программа должна
корректно обработать эту ситуацию и не завершиться с ошибкой.
"""

class DivisionByNull:
    def __init__(self, dividend, denominator):
        self.dividend = dividend
        self.denominator = denominator

    @staticmethod
    def divide_by_null(dividend, denominator):
        try:
            return (dividend / denominator)
        except ZeroDivisionError:
            return (f"На 0 делить нельзя")


div = DivisionByNull(10, 100)
print(DivisionByNull.divide_by_null(10, 0))
print(DivisionByNull.divide_by_null(10, 0.2))
print(div.divide_by_null(100, 0))

