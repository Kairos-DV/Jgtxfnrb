class Buffer:
    def __init__(self):
        # конструктор без аргументов
        self.buff = []

    def add(self, *a):
        # добавить следующую часть последовательности
        self.buff.extend(a)
        print('После add ', a, ' длина стала=', len(self.buff))
        while len(self.buff) >= 5:
            print('summa', sum(self.buff[0:5]))
            self.buff = self.buff[5:]

    def get_current_part(self):
        # вернуть сохраненные в текущий момент элементы последовательности в порядке, в котором они были добавлены
        print('Вызываю get', self.buff)


B = Buffer()
B.add(1, 1, 1, 1)
Buffer.get_current_part(B)
B.add(1, 2, 3, 4)
Buffer.get_current_part(B)
B.add(1, 2, 3, 4)
Buffer.get_current_part(B)
B.add(1, 2, 3, 4)
Buffer.get_current_part(B)
B.add(1, 2, 3, 4)
Buffer.get_current_part(B)
