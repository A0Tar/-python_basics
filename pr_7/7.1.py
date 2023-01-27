"""
Реализовать класс Matrix (матрица). Обеспечить перегрузку конструктора класса (метод __init__()),
который должен принимать данные (список списков) для формирования матрицы.

Следующий шаг — реализовать перегрузку метода __str__() для вывода матрицы в привычном виде.
Далее реализовать перегрузку метода __add__() для реализации операции сложения
двух объектов класса Matrix (двух матриц). Результатом сложения должна быть новая матрица.

"""

class Matrix:
    def __init__(self, my_list):
        self.my_list = my_list

    def __str__(self, my_list):
        for row in self.my_list:
            for i in row:
                print(f"{i:4}", end="")
            print()
        return ''



    def __str__(self):
       return '\n'.join(map(str, self.my_list))



    def __add__(self, other):
        for i in range(len(self.my_list)):
            for i_2 in range(len(other.my_list[i])):
                self.my_list[i][i_2] = self.my_list[i][i_2] + other.my_list[i][i_2]
        return Matrix.__str__(self)


m = Matrix([[1, 2, 3], [-1, 4, 1], [0, 1, -1], [1, 1, -1]])
new_m = Matrix([[1, 0, 3], [2, 3, 4], [0, 2, -4], [0, 2, -5]])
print(m.__add__(new_m))


