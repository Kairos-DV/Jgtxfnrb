
dictionary = {'key' : 'value', 'key1': 'value1'}    #Работа со словарем
print(dictionary.keys())

string = 'this is a string'
print(string[::-1]) #Перевернули строку

my_list = [1, 2, 3]
my_list[0:2:1] = [1.5, 1.75]  # Вставляем элементы на позицию с индексом 1
print(my_list)  # [1, 1.5, 1.75, 2, 3]

import copy

original = [1, 2, [3, 4], 5]
#
# another_list = original #Простое присваивание (another_list = original) создаёт новую ссылку на тот же объект, а не копию.
# another_list[0] = 100
# print("Original после простого присваивания:",original)

# #Глубокая копия
# deep_copy = copy.deepcopy(original)
# deep_copy[2][0] = 100
# print("Original после глубокой копии:", original)  # [1, 2, [99, 4]]
# print("Глубокая копия:", deep_copy)  # [100, 2, [100, 4]]

# Разные копии
original = [1, 2, 3, 4, 5]#[1, 2, [3, 4], 5]

shallow_copy = original.copy() # original    [ copy.copy(original) == original.copy() ]  copy.deepcopy(original)

print("Сравнение копий: ", shallow_copy == original)
print("Original до изменения копии:", original)  # [100, 2, [99, 4]]
shallow_copy[2] = 99 #shallow_copy[2][0] = 99
shallow_copy[3] = 99
print("Original после изменения копии:", original)  # [100, 2, [99, 4]]
print("shallow_copy после изменения копии:", shallow_copy)  # [100, 2, [99, 4]]

print("Сравнение копий: ", shallow_copy == original)

"""  Вывод 
При простом присваивании создается ссылка на тот же объект. На ту же область памяти
При создании поверхностной копии, создаются копии ссылок первого уровня на вложенные объекты. Если вложены списки, 
то при их изменении через копию будет менятся и оригинал, т.к. обе копии сылаются на одну и ту же область памяти.
если изменить неизменяемый объект, то создастся новый объект в новом участке памяти и изменения не затронут оригинал. 2 vle)
another_list[0] = 100
print(list_example)



#Пример глубокой копии
# original = [1,2,3,4,5]
#Создание глубокой копии с помощью атрибута .copy
# One_list = original.copy()
# Two_list = copy.copy(original)
# print("Original до изменения копий:", original)
# One_list[3] = 100
# Two_list[1] = 100
# print("One_list после изменения:",One_list)
# print("Two_list после изменения:",Two_list)
# print("Original после изменения копий:",original)

# #Пример глубокой копии
# list_example = [1,2,3,4,5]
# #Создание глубокой копии с помощью атрибута .copy
# another_list = list_example.copy()
# another_list[0] = 100
# print(list_example)
