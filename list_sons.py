import json
import sys

sys.stdin = open("date.txt", "r")

def count_parents(son,class_dict, parents):
    count = 0
    if class_dict[son] == []:
        return 0
    else:
        for parent in class_dict[son]:
            if parent not in parents: # Еще не посчитанный родитель
                parents.append(parent)
                count = 1 + count + count_parents(parent, class_dict, parents)
    return count

def list_sons(class_x, class_list):
    sons_list = []
    for elem in class_list:
        if class_x['name'] in elem['parents']:
            sons_list.append(elem)
    if sons_list:
        for son in sons_list:
            vnuki = list_sons(son, class_list)
            for vnuk in vnuki:
                if vnuk not in sons_list:
                    sons_list.append(vnuk)

    return sons_list


class_list = json.loads(input())
# print(class_list)
class_dict = {}
for son in class_list:
    class_dict[son['name']] = len(list_sons(son, class_list)) + 1
    # print(son, list_sons(son, class_list))

# print(class_dict)

sorted_by_key = dict(sorted(class_dict.items()))
for elem in sorted_by_key:
    print("{} : {}".format(elem,sorted_by_key[elem]))

# class_count = {}
# for elem in class_list:
#     class_count[elem['name']] =
#     if elem['name']
#
#
# class_count = {}


# for elem in class_dict:
#     class_count[elem] = count_parents(elem, class_dict, [])
# sorted_by_key = dict(sorted(class_count.items()))
# for elem in sorted_by_key:
#     print("{} : {}".format(elem,sorted_by_key[elem]))


# Создаём словарь с проверкой наличия ключей
# class_dict = {
#     item['name']: item.get('parents', [])  # Используем get() для защиты от отсутствия ключа
#     for item in class_list
#     if 'name' in item  # Пропускаем элементы без имени
# }
# print(class_dict)


{
 "text": "31 is a repdigit in base 5 (111), and base 2 (11111).",
 "number": 31,
 "found": true,
 "type": "math"
}