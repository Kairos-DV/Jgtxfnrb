import time

class Loggable:
    def log(self, msg):
        print(str(time.ctime()) + ": " + str(msg))

class LoggableList(Loggable, list):
    def append(self, item):
        super().append(item)  # Вызываем родительский append
        self.log(item)

# class ExtendedStack(list):
#     def sum(self):
#         # операция сложения
#         a = self.pop()
#         b = self.pop()
#         self.append(a + b)
#
#
#     def sub(self):
#         # операция вычитания
#         a = self.pop()
#         b = self.pop()
#         self.append(a - b)
#
#     def mul(self):
#         # операция умножения
#         a = self.pop()
#         b = self.pop()
#         self.append(a * b)
#
#     def div(self):
#         # операция целочисленного деления
#         a = self.pop()
#         b = self.pop()
#         self.append(a // b)
