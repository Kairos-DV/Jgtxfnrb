
import simplecrypt


# Зашифрованные данные (в формате bytes)
with open("encrypted.bin", "rb") as inp:
    encrypted = inp.read()
# with open("passwords.txt") as pas:
#     password = pas.readline()
#     plaintext = simplecrypt.decrypt(password, encrypted) # Расшифровка
#     print(plaintext.decode('utf-8'))  # преобразуем bytes в строку


password = 'RVrF2qdMpoq6Lib'
plaintext = simplecrypt.decrypt(password, encrypted)
print(plaintext.decode('utf-8'))  # преобразуем bytes в строку