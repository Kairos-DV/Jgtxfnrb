"""
Реализуйте функцию mod_checker(x, mod=0), которая будет генерировать лямбда функцию от одного аргумента y,
которая будет возвращать True, если остаток от деления y на x равен mod, и False иначе.

Пример использования:

mod_3 = mod_checker(3)

print(mod_3(3)) # True
print(mod_3(4)) # False

mod_3_1 = mod_checker(3, 1)
print(mod_3_1(4)) # True
"""
# def mod_checker(x, mod=0):
#     return lambda y: y % x == mod
#
# mod_3 = mod_checker(3)
#
# print(mod_3(3)) # True
# print(mod_3(4)) # False
#
# mod_3_1 = mod_checker(3, 1)
# print(mod_3_1(4)) # True

"""
Вашей программе на вход подаются три строки s, a, b, состоящие из строчных латинских букв.
За одну операцию вы можете заменить все вхождения строки a в строку s на строку b.

Например, s = "abab", a = "ab", b = "ba", тогда после выполнения одной операции строка s перейдет в строку "baba", 
после выполнения двух и операций – в строку "bbaa", и дальнейшие операции не будут изменять строку s.

Необходимо узнать, после какого минимального количества операций в строке s не останется вхождений строки a. 
Если операций потребуется более 1000, выведите Impossible.

Выведите одно число – минимальное число операций, после применения которых в строке s не останется вхождений строки a, 
или Impossible, если операций потребуется более 1000.
"""
# import sys
# sys.stdin = open("date.txt", "r")
#
# s = input().strip()
# a = input().strip()
# b = input().strip()
#
# # print(s, a, b)
#
# i = 0
# n = 0
# while s.find(a) > -1:
#     # print(s.find(b))
#     # print(s)
#     i += 1
#     if i == 1000:
#         n = -1
#         break
#     s = s.replace(a, b)
#     n = n + 1
# if n == -1:
#     print('Impossible')
# else:
#     print(n)
"""
Вашей программе на вход подаются две строки s и t, состоящие из строчных латинских букв.

Выведите одно число – количество вхождений строки t в строку s.

Пример:
s = "abababa"
t = "aba"

Вхождения строки t в строку s:
abababa
abababa
abababa
"""

import sys
sys.stdin = open("date.txt", "r")

def find2(s, t):
    i = s.find(t)
    if i == -1:
        return 0
    else:
        return 1 + find2(s[i+1:], t)

s = input().strip()
t = input().strip()
print(s,t)
print(find2(s, t))



# i = 0
# n = 0
#
# if s.find(t) == -1
#     return 0
#
# while s.find(a) > -1:
#     # print(s.find(b))
#     # print(s)
#     i += 1
#     if i == 1000:
#         n = -1
#         break
#     s = s.replace(a, b)
#     n = n + 1
# if n == -1:
#     print('Impossible')
# else:
#     print(n)
