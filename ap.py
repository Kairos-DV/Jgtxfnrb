"""
5. Использование zip():

Даны два списка:
names = ["Alice", "Bob", "Charlie"]
ages = [25, 30, 35]

Объедините их с помощью zip().
Преобразуйте результат в список кортежей.
Выведите имя и возраст каждого человека в формате: "Alice is 25 years old.".
"""
names = ["Alice", "Bob", "Charlie"]
ages = [25, 30, 35]
people = zip(names, ages)
people_list = list(zip(*people))

print(people_list)
for name, age in zip(names, ages): #people_list:
    print(f"{name} is {age} years old")
i = 0

while i <= len(people_list):
    print(f"{people_list[0][i]} {people_list[1][i]} years old")
    i+=1
#
# names = ["Alice", "Bob", "Charlie"]
# ages = [25, 30, 35]
#
# for name, age in zip(names, ages):
#     print(f"{name} is {age} years old.")
#



"""
4. Операторы и условия:
Напишите программу, которая принимает от пользователя число и проверяет:

Если число положительное, выведите "Positive".

Если число отрицательное, выведите "Negative".

Если число равно нулю, выведите "Zero".

"""
# n=int(input("Введите число: "))
# if n == 0:
#     print('Zero')
# elif n < 0:
#     print("Negativ")
# else:
#     print("Positive")










"""
3. Функции:
Напишите функцию multiply(a, b), которая возвращает произведение двух чисел.

Напишите функцию is_even(n), которая возвращает True, если число чётное, и False — если нечётное.

Используйте эти функции в программе, чтобы проверить их работу.

"""
# def multiply(a, b):
#     return a * b
# print(multiply(2,2))
# def is_even(n):
#     return False if n % 2 else True
# n = input("Введите число для проверки его четности: ")
# print("Четное") if is_even(int(n)) else print('Нечетное')




"""
2. Работа со строками:
Дана строка: "Python is awesome!".

Преобразуйте строку в список слов.

Добавьте в конец списка слово "right?".

Объедините список обратно в строку с пробелами между словами.

Выведите результат.
"""
# string = 'Python is awesome!'
# str_as_list = string.split()
# print(str_as_list)
# str_as_list.append('right?')
# print(str_as_list)
# new_string = ' '.join(str_as_list)
# print(new_string)
#

"""
1. Работа со списками:
Создайте список из 10 чисел.

Добавьте в конец списка число 11.

Удалите второй элемент списка.

Найдите сумму всех элементов списка.

Выведите список в обратном порядке.
"""
# list = [1, 2, 3, 4, 5, 6, 7]
# list.append(11)
# list.pop(1)
# # sum=0
# # for elem in list:
# #     print(elem)
# #     sum+=int(elem)
# i=0
# sum=0
# while i < len(list):
#     # print(list[i])
#     sum+=list[i]
#     i+=1
#     print(list[len(list) - i])
#
# print(sum)
# list=list[::-1]
# list.reverse()
#
# print(list)
# #sum=summ(list)