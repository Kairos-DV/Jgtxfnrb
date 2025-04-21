import re
import sys
import requests

sys.stdin = open("date.txt", "r")



def find_all_href(href):
    pattern_a = r'<a href="([\w:/\.]+)">'
    pattern_href = r'"([\w:/\.]+)"'
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
                h = re.findall(pattern_href, a)
                # print('Ссылка: ', h)
                list_href.append(a)
            return list_href
        else:
            # print('Это не ссылка на HTTP', href)
            return list_href
    except requests.exceptions.RequestException as e:
        # print(f"Error making request: {e}")
        return list_href

href1 = input().rstrip().replace('stepic.org', 'stepik.org')
# print('Считана 1 строка: ',href1)
href2 = input().rstrip().replace('stepic.org', 'stepik.org')
# print('Считана 2 строка: ',href2)
list_href = find_all_href(href1)
print('Все найденные адреса на сайте(href1): ',href1, list_href)
res = 'No'
for h1 in list(list_href):
    h1 = h1.replace('stepic.org', 'stepik.org')
    # print('h1', h1)
    if h1 == href2:
        # print('Yes', h1)
        res = 'Yes'
        break
    else:
        list_href2 = find_all_href(h1)
        # print("Все найденные адреса на сайте(h1): ",h1, list_href2)
        for h2 in list(list_href2):
            h2 = h2.replace('stepic.org', 'stepik.org')
            # print('h2', h2)
            if h2 == href2:
                # print("Yes", h2)
                res = 'Yes'
                break
print(res)





# response = requests.get(content)
# content = response.text
# print(f"Processed line: {result}")
# print(conten)
# # n = 1
# for line in content:
#     print(line)
#     n += 1
#     print(n)
# Здесь можно обработать content с помощью регулярных выражений

