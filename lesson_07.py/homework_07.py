# task 1
""" Задача - надрукувати табличку множення на задане число, але
лише до максимального значення для добутку - 25.
Код майже готовий, треба знайти помилки та випраавити\доповнити.
"""
def multiplication_table(number):
    
    multiplier = 1

    while multiplier and number:
        result = number * multiplier

        if  result > 25:
            break
        
        print(str(number) + "x" + str(multiplier) + "=" + str(result))

        multiplier += 1

multiplication_table(3)


# task 2
"""  Написати функцію, яка обчислює суму двох чисел.
"""
def add(a, b):
    return a + b

result = add(6, 7)
print(result)

# task 3
"""  Написати функцію, яка розрахує середнє арифметичне списку чисел.
"""
def average_number():
    numbers = [x for x in range(10)]
    print(numbers)
    num_sum = sum(numbers)
    print(num_sum)
    average = num_sum / len(numbers)
    print(f"The avarage of the list of numbers is {average}")
    
average_number()


# task 4
"""  Написати функцію, яка приймає рядок та повертає його у зворотному порядку.
"""
def reverse_num_list(str):
    reverse_str = str[::-1]
    print(f"Reversed string: {reverse_str}")

reverse_num_list(str='Hello how are you') 

# task 5
"""  Написати функцію, яка приймає список слів та повертає найдовше слово у списку.
"""
def longest_word(words):
    x = ''
    for word in words:
        print(len(word))
        if len(word) > len(x):
            x = word

    return x

result = longest_word(words=['Hello', 'how', 'are', 'you', 'feeling'])
print('RESULT:', result)

# task 6
"""  Написати функцію, яка приймає два рядки та повертає індекс першого входження другого рядка
у перший рядок, якщо другий рядок є підрядком першого рядка, та -1, якщо другий рядок
не є підрядком першого рядка."""
def find_substring(str1, str2):

    return str1.find(str2)

str1 = "Hello, world!"
str2 = "world"
print(find_substring(str1, str2)) # поверне 7

str1 = "The quick brown fox jumps over the lazy dog"
str2 = "cat"
print(find_substring(str1, str2)) # поверне -1

# task 7
# task 8
# task 9
# task 10
"""  Оберіть будь-які 4 таски з попередніх домашніх робіт та
перетворіть їх у 4 функції, що отримують значення та повертають результат.
Обоязково документуйте функції та дайте зрозумілі імена змінним.
"""
#task 7
# задача з дз 6.4

def even_num_sum(numbers):
    even_numbers_list = []
    for num in numbers:
         if num % 2 == 0:
            even_numbers_list.append(num)
    result = sum(even_numbers_list)
    return result 

print(even_num_sum(numbers = [1, 3, 5, 6, 8, 4]))

#task 8 
# задача з дз 6.3

def only_str_list(lst1):
    str_list = []
    for element in lst1:
        if isinstance(element, str):
            str_list.append(element)
    
    return str_list

print(only_str_list(lst1=['1', '2', 3, True, 'False', 5, '6', 7, 8, 'Python', 9, 0, 'Lorem Ipsum']))

#task 9 
#задача з дз 6.2
# не впевнена що краще тут передавати як kwargs щоб це мало сенс, зараз здається це не дуже має сенсу

def only_H_and_h_accept(result_1, result_2):
    
    while result_1 <= -1 and result_2 <= -1:
        user_input = input("Type in the string with letter 'H' or 'h': ")
        result_2 = user_input.find('H')
        result_1 = user_input.find('h') 
    return user_input

print(only_H_and_h_accept(result_1= -1, result_2= -1))

#task 10
# задача з дз 6.1
# тут так само як і в попередньому, не впевнена що краще передавати як kwarg
def more_or_equal_10_unique_symbols(user_input):
    my_set_len = len(set(user_input))
    if my_set_len >= 10:
        print(True)
    else:
        print(False)

    return my_set_len 
print(more_or_equal_10_unique_symbols(user_input = input("Input smth: ")))
