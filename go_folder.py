import os

folder_path = r'C:\PROJECT\Jgtxfnrb2\main'

res = ''
sres = []
res2 = ''
for root, dirs, files in os.walk(folder_path):
    for filename in files:
        file_path = os.path.join(root, filename)
        # print(file_path)  # полный путь к файлу
        file_py = file_path.split('\\')
        # print(file_py)
        sres2 = []
        res2 = ''
        if file_py[-1][-3::] == '.py':
            print(file_py[-1])
            sres2.extend(file_py[3:-1])
            res2 = '/'.join(sres2) + '\n'
            print(res2)
            if res2 not in sres:
                sres.append(res2)

sres.sort()
res = ''.join(sres)

with open('res.txt', 'w') as file_res:
    file_res.write(res)


