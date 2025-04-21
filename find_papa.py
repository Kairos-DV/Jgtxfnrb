import sys
sys.stdin = open("date.txt", "r")

def find_papa(ded, son, D):
    # print(ded, son)
    if ded == son:
        return True
    else:
        papa = False

    for P in D[son]:
        # print(P, son, D[son])
        if P == ded:
            papa = True
            break
        elif find_papa(ded, P, D):
            papa = True
            break
        else:
            papa = False
    else:
        papa = False
    return papa

i = 0
j = 0
cl = []
qe = []
dcl = dict()
n = int(input())
while i < n:
    cl.append(input().split())
    dcl_i = {cl[i][0]:cl[i][2:]}
    dcl.update(dcl_i)
    i += 1
n = int(input())
while j < n:
    qe.append(input().split())
    if find_papa(qe[j][0],qe[j][1], dcl):
        print('Yes')
    else:
        print('No')
    j += 1


"""
Вам дано описание наследования классов исключений в следующем формате.
<имя исключения 1> : <имя исключения 2> <имя исключения 3> ... <имя исключения k>
Это означает, что исключение 1 наследуется от исключения 2, исключения 3, и т. д.

Или эквивалентно записи:
class Error1(Error2, Error3 ... ErrorK):
    pass

Антон написал код, который выглядит следующим образом.

try:
   foo()
except <имя 1>:
   print("<имя 1>")
except <имя 2>:
   print("<имя 2>")
...
Костя посмотрел на этот код и указал Антону на то, что некоторые исключения можно не ловить,
так как ранее в коде будет пойман их предок. Но Антон не помнит какие исключения наследуются от каких.
Помогите ему выйти из неловкого положения и напишите программу, которая будет определять обработку каких
исключений можно удалить из кода.
"""

import sys
sys.stdin = open("date.txt", "r")

def find_papa(possible_father, son, D):
    # print("Папа? -", possible_father, 'Сын -', son, 'Словарь', D)
    if possible_father == son:
        return True
    else:
        papa = False
    for P in D[son]:
        # print(P, son, D[son])
        if P == possible_father:
            papa = True
            break
        elif find_papa(possible_father, P, D):
            papa = True
            break
        else:
            papa = False
    else:
        papa = False
    return papa

i = 0
# j = 0
cl = []
qe = []
dcl = dict()
n = int(input()) #count classes except
# print('Число классов', n)
while i < n:
    cl.append(input().split())
    dcl_i = {cl[i][0]:cl[i][2:]}
    dcl.update(dcl_i)
    # print('Словарь класса № ', i, dcl_i)
    i += 1
# print('Список всех словарей классов', dcl)
n = int(input()) #count except
# print('Число заявленных исключений', n)
i = 0
cl = []
while i < n:
    qe.append(''.join(input().split()))
    i += 1
# print('Все исключения в порядке объявления', qe)
i = 0
while i < n: # Обходим список с конца
    i += 1
    son = qe[-i]
    # print('Сын', son)
    # papas = qe[0:-i]
    for possible_father in qe[0:-i]:
        # print('Проверяем на отцовство класс', possible_father)
        if find_papa(possible_father, son, dcl):
            # qe.remove(son)
            # while possible_father in papas:
            #     papas.remove(possible_father)
            # while possible_father in qe:
            #     qe.remove(possible_father)
            # n = n - 1
            cl.append(son)
            break
            # qe = [x for x in qe if x == possible_father]
            # qe.remove(possible_father)
            # print(papas)
st = '\n'.join(cl[::-1])
print(st)

# if find_papa(qe[j][0],qe[j][1], dcl):
#     print('Yes')
# else:
#     print('No')



# ArithmeticError
# ZeroDivisionError : ArithmeticError
# OSError
# FileNotFoundError : OSError
# 4
# ZeroDivisionError
# OSError
# ArithmeticError
# FileNotFoundError
