"""
1. Базовые операции (чтение/запись)
Задача:
Создай файл notes.txt, запиши в него строку "Hello, файлы!", затем прочитай и выведи его содержимое.

python
Copy
# Запись в файл
with open('notes.txt', 'w', encoding='utf-8') as file:
    file.write("Hello, файлы!\n")

# Чтение из файла
with open('notes.txt', 'r', encoding='utf-8') as file:
    content = file.read()
print(content)
Пояснения:

'w' — режим записи (перезаписывает файл, если он существует).

'utf-8' — кодировка для поддержки кириллицы.

with — контекстный менеджер (автоматически закрывает файл).
📝 2. Обработка данных из файла
Задача:
В файле data.txt хранятся числа (каждое с новой строки). Напиши код, который:

Читает числа из файла.

Вычисляет их сумму и среднее арифметическое.

3. Поиск и замена в файле
Задача:
Замени все вхождения слова "яблоко" на "апельсин" в файле fruits.txt и сохрани результат в новый файл updated_fruits.txt.

"""

# with open('notes.txt', 'w', encoding='utf-8') as file:
#      file.write('Hello, i`m begin work with files\n')
with open('date.txt', encoding='utf-8') as file:
    text = list(file.readlines())
print(text) # test
N = len(text)
Sum = 0
print(N) # test
for num in text:
    Sum += int(num)
    print(Sum) # test
# numbers =

print("Сумма: {0}, Среднее: {1:.4}".format(Sum, Sum/N))