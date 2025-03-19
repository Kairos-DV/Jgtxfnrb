import collections

Card = collections.namedtuple('Card',['rank','sulit'])

class FrenchDesk:
    ranks = [str(n) for n in range(2,11)]+list('JQKA')
    suits = 'пики крести буби черви'.split()

    def __init__(self):
        self._cards = [Card(rank,suit)
                       for suit in self.suits
                       for rank in self.ranks]

    def __len__(self):
        return len(self._cards)

    def __getitem__(self, position):
        return self._cards[position]
    # def __repr__(self):
    #     return f"{self.ranks} of {self.suits}"

# beer_card = Card('7','черви')   #Создаем элемент Card и присваеваем ему значение
# print(beer_card)                #Выводим на экран

deck = FrenchDesk() #Создаем объект класса FrenchDesk
for card in deck: print(card)
# print(len(deck))    #Выводим длину
# print("Первая карта: ", deck[0])      #Выводим первый элемент
# print(deck[-1])     #Выводим последний элемент
# print(deck[12::13])
#
# Выбираем случайную карту из колоды с помощью стандартной функции random.choice
from random import choice
print(choice(deck))
print(choice(deck))




