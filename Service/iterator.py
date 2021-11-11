class Iterator:
    def __init__(self, iterable):
        self.iterable = iter(iterable)
        self.__has_next = None
        self.__next = None

    def next(self):
        if self.__has_next:
            result = self.__next
        else:
            result = next(self.iterable)
        self.__has_next = None
        return result

    def has_next(self):
        try:
            self.__next = next(self.iterable)
        except StopIteration:
            self.__has_next = False
        else:
            self.__has_next = True
        return self.__has_next

