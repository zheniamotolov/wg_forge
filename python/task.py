import datetime


# Заполните код преведенных ниже функций. Функция main() уже настроена
# для вызова функций с несколькими различными параметрами,
# и выводит 'OK' в случае, если вызов функции корректен.
# Начальный код каждой функции содержит 'return'
# и является просто заготовкой для вашего кода.


# A. Простейшие арифметические операции
# Написать функцию arithmetic, принимающую 3 аргумента:
# первые 2 - числа, третий - операция, которая должна быть произведена над ними.
# Если третий аргумент +, сложить их;
# если —, то вычесть;
# * — умножить;
# / — разделить (первое на второе).
# В остальных случаях вернуть строку "unknown".
def arithmetic(arg1, arg2, op):
    if op == '+':
        return arg1 + arg2
    elif op == '-':
        return arg1 - arg2
    elif op == '*':
        return arg1 * arg2
    elif op == '/':
        return arg1 / arg2
    else:
        return 'unknown'


# B. Високосный год
# Написать функцию is_is_year_leap_leap,
# принимающую 1 аргумент — год, и возвращающую True, если год високосный, и False иначе.
def is_year_leap(year):
    if year % 400 == 0:
        return True
    if year % 100 == 0:
        return False
    if year % 4 == 0:
        return True
    else:
        return False


# C. Квадрат 
# Написать функцию square, принимающую 1 аргумент — сторону квадрата, 
# и возвращающую 3 значения (с помощью кортежа):
# периметр квадрата, площадь квадрата и диагональ квадрата.
def square(a):
    return 4 * a, a ** 2, a ** 0.5


# D. Времена года
# Написать функцию season,
# принимающую 1 аргумент — номер месяца (от 1 до 12), 
# и возвращающую время года, которому этот месяц принадлежит ('winter', 'spring', 'summer', 'autumn').
def season(month):
    return {
        1: 'winter',
        2: 'winter',
        3: 'spring',
        4: 'spring',
        5: 'spring',
        6: 'summer',
        7: 'summer',
        8: 'summer',
        9: 'autumn',
        10: 'autumn',
        11: 'autumn',
        12: 'winter',
    }[month]


# E. Банковский вклад
# Пользователь делает вклад в размере money рублей сроком на years лет под 10% годовых
# (каждый год размер его вклада увеличивается на 10%.
# Эти деньги прибавляются к сумме вклада, и на них в следующем году тоже будут проценты).
# Написать функцию deposit, принимающая аргументы money и years, и возвращающую сумму,
# которая будет на счету пользователя.
def deposit(money, years):
    for i in range(years):
        money += money * 0.1
    return round(money, 4)


# F. Простые числа
# Написать функцию is_prime, принимающую 1 аргумент — число от 0 до 1000,
# и возвращающую True, если оно простое, и False - иначе
def is_prime(num):
    if num < 2:
        return False
    if num == 2:
        return True
    if num % 2 == 0:
        return False
    for i in range(3, num // 2, 2):
        if num % i == 0:
            return False
    return True


# G. Правильная дата
# Написать функцию date, принимающую 3 аргумента — день, месяц и год.
# Вернуть True, если такая дата есть в нашем календаре, и False иначе.
def date(day, month, year):
    try:
        datetime.datetime(year, month, day)
        return True
    except ValueError:
        return False


# H. XOR-шифрование
# Написать функцию XOR_cipher, принимающая 2 аргумента: строку,
# которую нужно зашифровать, и ключ шифрования, которая возвращает строку,
# зашифрованную путем применения функции XOR (^) над символами строки с ключом.
# Написать также функцию XOR_uncipher, которая по зашифрованной строке и ключу восстанавливает исходную строку.
def XOR_cipher(str, key):
    result_string = ''
    for i in range(len(str)):
        current_sumbol = str[i]
        result_string += chr(ord(current_sumbol) ^ ord(key[i % len(key)]))
    return result_string


def XOR_uncipher(str, key):
    return XOR_cipher(str, key)


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
    print(u'Арифметические операции')
    test(arithmetic(3, 4, '+'), 7)
    test(arithmetic(3, 4, '-'), -1)
    test(arithmetic(3, 4, '*'), 12)
    test(arithmetic(3, 4, '/'), 3 / 4)
    test(arithmetic(3, 4, '.'), 'unknown')

    print(u'\nВисокосный год')
    for year in (2000, 2016, 1916):
        test(is_year_leap(year), True)
    for year in (1900, 2014, 2001):
        test(is_year_leap(year), False)

    print(u'\nКвадрат')
    for a in range(10):
        test(square(a), (4 * a, a ** 2, a ** 0.5))

    print(u'\nВремена года')
    seasons = [
        None, 'winter', 'winter', 'spring', 'spring', 'spring', 'summer', 'summer', 'summer', 'autumn', 'autumn',
        'autumn', 'winter'
    ]
    for month in range(1, 13):
        test(season(month), seasons[month])

    print(u'\nБанковский вклад')
    test(deposit(10000, 1), 11000)
    test(deposit(1234, 3), 1642.454)
    test(deposit(2345, 4), 3433.3145)
    test(deposit(10000, 1), 11000)
    for years in range(1, 10):
        test(deposit(0, years), 0)
    test(deposit(200, 0), 200)

    print(u'\nПростые числа')
    primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]
    for number in range(1, 101):
        test(is_prime(number), number in primes)
    big_primes = [947, 953, 967, 971, 977, 983, 991, 997]  # 941 - простое
    for number in range(940, 1000):
        test(is_prime(number), number in big_primes)

    print(u'\nПравильная дата')
    test(date(1, 1, 1900), True)
    test(date(1, 1, 1), True)
    test(date(31, 1, 2000), True)
    test(date(31, 12, 1900), True)
    test(date(1, 13, 1900), False)
    test(date(2, 14, 2003), False)
    test(date(30, 2, 1900), False)
    test(date(32, 13, 1900), False)

    print(u'\nXOR-шифрование')
    test(XOR_cipher('Hello', '1'), 'yT]]^')
    test(XOR_uncipher('yT]]^', '1'), 'Hello')
    string, key = 'Python', 'World'
    test(XOR_uncipher(XOR_cipher(string, key), key), string)
    string = 'ABCDFF'
    test(XOR_cipher(string, string), '\0' * len(string))


if __name__ == '__main__':
    main()
