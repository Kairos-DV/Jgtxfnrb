# import pandas as pd

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


deck = FrenchDesk()
print(len(deck))
print(deck[0])

# def __getitem__(self, index):
#         return self.cards[index]

# print('Goodby-by')
# Left_Tabl: object = pd.read_excel('C:/PROJECT/Jgtxfnrb2/Excel_Data/Левый.xlsx')
# Right_Tabl: object = pd.read_excel('C:/PROJECT/Jgtxfnrb2/Excel_Data/Правый.xlsx')
# print(Left_Tabl.head(1))
# print(Right_Tabl.head(2))
# Left_Tabl.to_excel('C:/PROJECT/Jgtxfnrb2/Excel_Data/Левый2.xlsx')
# print(Left_Tabl.columns.to_list)
# print(Left_Tabl.columns.to_list)

beer_card = Card('7','черви')
print(beer_card)

