class EvenNumbersIterator:
    def __init__(self, n):
        self.n = n
        self.current = 0

    def __iter__(self):
        return self 

    def __next__(self):
        if self.current > self.n:
            raise StopIteration 
        result = self.current
        self.current += 2
        return result


even_numbers = EvenNumbersIterator(10)


print(next(even_numbers))  
print(next(even_numbers))  
print(next(even_numbers))  

try:
    while True:
        print(next(even_numbers))
except StopIteration:
    print("StopIteration: Ітератор закінчився")
