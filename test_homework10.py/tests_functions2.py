def even_num_sum(numbers):
    even_numbers_list = []
    for num in numbers:
         if num % 2 == 0:
            even_numbers_list.append(num)
    result = sum(even_numbers_list)
    return result 

def only_str_list(lst1):
    str_list = []
    for element in lst1:
        if isinstance(element, str):
            str_list.append(element)
    
    return str_list