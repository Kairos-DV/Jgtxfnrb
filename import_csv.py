"""
Вашей программе на вход подается ссылка на HTML файл.
Вам необходимо скачать этот файл, затем найти в нем все ссылки вида <a ... href="..." ... > и вывести список сайтов, на которые есть ссылка.

Сайтом в данной задаче будем называть имя домена вместе с именами поддоменов. То есть, это последовательность символов, которая следует сразу после символов протокола, если он есть, до символов порта или пути, если они есть, за исключением случаев с относительными ссылками вида
<a href="../some_path/index.html">.

Сайты следует выводить в алфавитном порядке.

Пример HTML файла:

<a href="http://stepik.org/courses">
<a href='https://stepik.org'>
<a href='http://neerc.ifmo.ru:1345'>
<a href="ftp://mail.ru/distib" >
<a href="ya.ru">
<a href="www.ya.ru">
<a href="../skip_relative_links">

Пример ответа:

mail.ru
neerc.ifmo.ru
stepik.org
www.ya.ru
ya.ru
"""

"""
import re
import sys
import requests

sys.stdin = open("date.txt", "r")


def domen_name(string):
    pattern = r'(?:https?://)?([a-zA-Z0-9-]+\.[a-zA-Z0-9-]+\.[a-zA-Z0-9-]+|[a-zA-Z0-9-]+\.[a-zA-Z0-9-]+)(?=/|$)'
    href = re.search(pattern, string)
    if href == None:
        return None
    # print('href',href)
    # print('href.group(0)',href.group(1))
    return href.group(1)

#(?:https?://)?([a-zA-Z0-9-]+\.[a-zA-Z0-9-]+\.[a-zA-Z0-9-]+|[a-zA-Z0-9-]+\.[a-zA-Z0-9-]+)(?=/|$)
#([\w]+\.([\w])+\.([\w])+)\.([\w])+|([\w]+\.([\w])+\.([\w])+)|([\w]+\.([\w])+)
# r'(-\w]+\.([-\w])+\.([-\w])+)\.([\w])+|([-\w]+\.([-\w])+\.([\w])+)|([-\w]+\.([\w])+)'

def find_all_href(href):
    pattern_a = r'(?:https?://)?([a-zA-Z0-9-]+\.[a-zA-Z0-9-]+\.[a-zA-Z0-9-]+|[a-zA-Z0-9-]+\.[a-zA-Z0-9-]+)(?=/|$)'
    # r'"([\w:/\.]+)"'
    list_href = []
    try:
        # Делаем HTTP-запрос (если это URL)
        if href.startswith(('http://', 'https://')):
            response = requests.get(href)
            # print(f"HTTP status code: {response.status_code}")  # Исправлено: status_code, а не status.code
            # Обрабатываем содержимое страницы, если нужно
            content = response.text
            # print('Считанная строка',content)
            href_all = re.findall(pattern_a, content)
            # print("Все найденные href: ", href_all)
            for a in href_all:
                # print("Ссылка: ", a)
                h = re.findall(pattern_a, a)
                # print('Ссылка: ', h)
                list_href.append(a)
            return list_href
        else:
            # print('Это не ссылка на HTTP', href)
            return list_href
    except requests.exceptions.RequestException as e:
        # print(f"Error making request: {e}")
        return list_href


site = input().rstrip()
all_url = find_all_href(site)
# print('Все найденные адреса на сайте(href1): ',site, all_url)
# print(len(all_url))
all_url.sort()
#Удаление дублей
new_url = []
for u in list(all_url):
    x = domen_name(u)
    if x == None:
        pass
    elif x not in new_url:
        new_url.append(x)
        print(x)
# print(len(new_url))


"""

import csv


def count_crimes(filename):
    crime_counts = {}  # Словарь для хранения количества преступлений

    with open(filename) as f:
        reader = csv.reader(f)
        header = next(reader)  # Пропускаем заголовок

        for row in reader:
            date = row[2]  # Предполагаем, что дата в третьем столбце
            crime_type = row[5]  # Тип преступления в шестом столбце

            if '2015' in date:
                # Увеличиваем счетчик для данного типа преступления
                crime_counts[crime_type] = crime_counts.get(crime_type, 0) + 1

    return crime_counts


# Использование функции
crime_stats = count_crimes("Crimes.csv")

# Находим тип преступления с максимальным количеством случаев
most_common_crime = max(crime_stats.items(), key=lambda x: x[1])

print(f"Самый частый тип преступления в 2015: {most_common_crime[0]} ({most_common_crime[1]} случаев)")