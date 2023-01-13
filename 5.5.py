"""
Создать (программно) текстовый файл, записать в него программно набор чисел, разделённых пробелами.
Программа должна подсчитывать сумму чисел в файле и выводить её на экран.
"""

import random

i = 0
lst = []
while i<10:
    number = random.randint(0, 101) # число от 0 до 100
    lst = lst + [number]
    i = i+1

print("lst = ", lst)

f = open('file.txt', 'wt')
s = str(len(lst)) # Конвертировать целое число в строку
f.write(s + '\n') # Записать строку
for i in lst:
    s = str(i) # конвертировать элемент списка в строку
    f.write(s + ' ') # записать число в строку
with open("file.txt") as read_file:
    read_line = read_file.readline()
    print("\t" + read_line)
    for str_number in read_line.split():
        res_sum += int(str_number)
    print(f"\tСумма: {res_sum}\n")

