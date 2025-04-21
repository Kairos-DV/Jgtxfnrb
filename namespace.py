
cmd, namesp, arg = 'add', 'global', 'a'
# add global a
# create foo global
# add foo b
# get foo a
# get foo c
# create bar foo
# add bar a
# get bar a
# get bar b
def fun_create (namesp, arg,D):
    D.update({namesp:[arg]}) #Первый элемент - родительское пространство
    return D

def fun_add(namesp,arg,D):
    if namesp in D.keys():
        L = D[namesp]
        L.append(arg)
    else:
        print("Error. Dont namesp")
    return D

def fun_get (namesp, arg,D):
    if namesp in D.keys():
        L = D[namesp]
        if arg in L[1:]:
            print(namesp)
        elif L[0] == 'None':
            print('None')
        else:
            fun_get(L[0],arg,D)
    return D

#cmd, namesp, arg = input().split()
glob = {'global':['None']}
with open('date.txt', encoding='utf-8') as file:
    n = file.readline().split()
    n = int(n[0])
    print(n)
    i = 0
    while i < n:
        i += 1
        cmd, namesp, arg = file.readline().split()
        # print(cmd, namesp, arg)
        if cmd == 'create':
            glob = fun_create(namesp, arg, glob)
        elif cmd == 'add':
            glob = fun_add(namesp, arg, glob)
        elif cmd == 'get':
            # print(cmd, namesp, arg, glob)
            glob = fun_get(namesp, arg, glob)
        else:
            print('error')
# print(glob)
 # cmd, namesp, arg = file.readline().split()
# cmd, namesp, arg = 'add', 'global', 'a'
# # print(cmd, namesp, arg)
# glob = {'global':[]}
# print(glob)
# if cmd == 'add':
#     glob = fun_add(namesp, arg, glob)
#
# print(glob)
