"""
Задание 6.

Реализовать функцию int_func(), принимающую слова из маленьких латинских букв
и возвращающую их же, но с прописной первой буквой. Например, print(int_func(‘text’)) -> Text.
"""
def int_func(word):
    listed_word = list(word)
    listed_word[0] = listed_word[0].upper()
    return ''.join(listed_word)


output = []

for word in input('Введите слова из маленьких латинских букв: ').split(' '):
    output.append(int_func(word))

print(f'Результат: {" ".join(output)}')
