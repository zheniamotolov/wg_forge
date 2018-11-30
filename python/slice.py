﻿# Срезы
import networkx as nx
import pygraphviz as pgv
# Заполните код преведенных ниже функций. Функция main() уже настроена
# для вызова функций с несколькими различными параметрами,
# и выводит 'OK' в случае, если вызов функции корректен.
# Начальный код каждой функции содержит 'return'
# и является просто заготовкой для вашего кода.

# Справвка
# Оператор получения среза имеет три формы записи: 
# seq[start]
# seq[start:end]
# seq[start:end:step]
# Шаг может быть отрицательным, в этом случае элементы последовательности
# вернутся в обратном порядке.


# A. Четные
# Дана строка, состоящая из символов и/или последовательностей символов, 
# разделенных пробелами.
# Нужно вернуть строку, содержащую только четные элементы из исходной строки.
# Например, из 'a b c d e f' получится 'b d f'
# Решите задачу в одну строчку используя срезы.
def even(s):
    nx.draw()
    A = pgv.AGraph()
    A.node_attr['shape'] = 'circle'
    A.node_attr['style'] = 'filled'
    A.node_attr['fontsize'] = '1'
    s = s.split(' ')
    return ' '.join(s[1::2])


# B. Наоборот
# Дана строка, состоящая из символов и/или последовательностей символов,
# разделенных пробелами.
# Нужно вернуть строку, содержащую элементы исходной строки в обратном порядке.
# Например, из 'a b c d e' получится 'e d c b a'
# Решите задачу в одну строчку используя срезы.
def reverse(s):
    s = s.split(' ')
    return ' '.join(s[::-1])


# C. Сдвиг
# Дана строка, состоящая из символов и/или последовательностей символов, 
# разделенных пробелами.
# Нужно вернуть строку, в которой последний элемент находится на первом месте.
# Например, из 'a b c d e f' получится 'f a b c d e'
# Решите задачу в две строки используя срезы.
def shift(s):
    s = s.split(' ')
    return ' '.join(s[-1:] + s[:-1])


# D. Палиндром
# Дано число.
# Нужно определить является ли оно палиндромом.
# Число является палиндромом если оно одинаково читающееся в обоих направлениях.
# Решите задачу в одну строку используя срезы.
def palindrome(d):
    return str(d) == str(d)[::-1]


# E. Внутри
# Дана строка, состоящая из четного количества символов и/или последовательностей символов,
# разделенных пробелами.
# Верните строку, в которой первый и последний элементы поставлены в середину 
# исходной строки. Например, из 'a b c d e f' получится 'b c a f d e'.
# Решите задачу в три строки используя срезы.
def inside(s):
    s = s.split(' ')
    n = len(s)
    return ' '.join(s[1:n // 2] + s[:1] + s[n-1:] + s[n // 2:n - 1])


# Простая функция test() используется в main() для вывода
# сравнения того, что возвращает с функция с тем, что она должна возвращать.
def test(got, expected):
    if got == expected:
        prefix = ' OK '
    else:
        prefix = '  X '
    print(u'%s Получено: %s | Ожидалось: %s' % (prefix, repr(got), repr(expected)))


# Вызывает фунции выше с тестовыми параметрами.
def main():
    print(u'Четные')
    test(even('a b c d e f'), 'b d f')  # 0 - четное число !!!
    test(even('w ee rt fff xyz'), 'ee fff')

    print()
    print(u'Наоборот')
    test(reverse('a b c d e f'), 'f e d c b a')
    test(reverse('w ee rt fff xyz'), 'xyz fff rt ee w')

    print()
    print(u'Сдвиг')
    test(shift('a b c d e f'), 'f a b c d e')
    test(shift('w ee rt fff xyz'), 'xyz w ee rt fff')

    print()
    print(u'Палиндром')
    test(palindrome(12321), True)
    test(palindrome(12345), False)

    print()
    print(u'Внутри')
    test(inside('a b c d e f'), 'b c a f d e')
    test(inside('w ee rt fff'), 'ee w fff rt')


if __name__ == '__main__':
    main()
