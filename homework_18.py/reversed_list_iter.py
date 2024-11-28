class ReversedList:
    def __init__(self, list):
        self.list = list
        self.index = len(list)  

    def __iter__(self):
        return self

    def __next__(self):
        self.index -= 1
        if self.index >= 0:
            return self.list[self.index]
        else:
            raise StopIteration


my_list = ReversedList(['hello', 5, 4, 6, 'name', 'age', True])
for item in my_list:
    print(item)
