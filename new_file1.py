'''Примає радіус кола, повертає довжину кола. Обробити випадки коли в радіус приходить не числом.'''
#
# import math
# def radius(r):
#
#     num = math.pi
#     try:
#         l = 2 * num * r
#         return l
#     except TypeError:
#         return "Введите числовое значение пожалуйста!"
#
#
# print(radius(7))
# print(radius('a'))


'''Примає радіус кола, повертає площу кола. Обробити випадки коли в радіус приходить не числом.'''

# import math
# def radius(r):
#
#     num = math.pi
#     try:
#         a = num * r ** 2
#         return a
#     except:
#         return "Введите числовое значение"
#
#
# print(radius(7))
# print(radius('a'))


'''Приймає число, повертає чи є число поліндромом.'''


# def palindrom(p):
#
#     pal = str(p)
#     p_reversed = pal[::-1]
#     if pal == p_reversed:
#         return f"{pal} - поліндром"
#     else:
#         return f"{pal} - не поліндром"
#
#
# print(palindrom(12321))
# print(palindrom(1321))


'''Функція приймає число n яке більше 0. За допомогою рекурсії виводить всі числа що менші n але більші 0.'''

# def recursion(n):
#
#     if n > 0:
#         if n == 1:
#             return 1
#         print(n)
#         return recursion(n - 1)
#
#     else:
#         return f"{n} <- sub 0. Or wrong data type\n"
#
#
# print(recursion(0))
# print(recursion(5))
# print(recursion(1))
# print(recursion(-1))


'''Написати функцію lambda що приймає x i y, а повертає x^2 + y^2'''

# n = lambda x, y: (x ** 2) + (y ** 2)
#
# print(n(5, 5))


'''Написать lambda функцию которая принимает слово и возвращает его длинну'''

# bd = lambda x: len(x)
#
# print(f"Кол-во символов -> {bd('Leila')}")
# print(f"Кол-во символов -> {bd('Steven')}")


'''Написати map що перетворює всі числа в списку на строку.'''

# lst = [1, 2, 3, 4, 5, 10, 20, 50, 100, 1000]
#
#
# def nts(l):
#     return str(l)
#
#
# lst_str = list(map(nts, lst))
# print(f"Number to string -> {lst_str}")


'''Написати filter що залишає в списку тільки числа > 10'''

# lst= [1, 2, 3, 4, 5, 6, 9, 12, 13, 14, 15, 16, 17, 20]
#
#
# def num(lst_10):
#     return lst_10 < 10
#
#
# l = list(filter(num, lst))
# print(f"After filter -> {l}")

'''Є список слів, за допомогою map видалити з кожного слова всі букви "а"'''
'''Вариант 1'''
# lst = ["acer", "asus", "audi", "toyota"]
#
# def rep(r):
#
#     some_word = ""
#     for i in r:
#         if i != "a":
#             some_word = some_word + i
#     return some_word
#
#
# done = list(map(rep, lst))
# print(done)

'''Вариант 2'''
# lst = ["acer", "asus", "audi", "toyota",]
# list = list(map(lambda x: x.replace("a", ""), lst))
# print(list)


'''Є список слів, за допомогою filter залишити тільки ті слова в яких к-ть букв більша ніж 4.'''

# lst = ["acer", "asus", "audi", "toyota"]

# def func(t):
#     return len(t) > 4
#
#
# done = list(filter(func, lst))
# print(done)


'''2 Вариант'''
# lst = ["acer", "asus", "audi", "toyota"]
#
# lst_done = list(filter(lambda x: len(x) > 4, lst))
#
# print(lst_done)