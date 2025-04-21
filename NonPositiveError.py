class NonPositiveError(Exception):
    pass

class PositiveList(list):
    def append(self, item):
        if item > 0:
            super().append(item)  # Вызываем родительский append
        else:
            raise NonPositiveError