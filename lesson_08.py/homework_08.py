def sum_numbers(str_list):
    for str in str_list:
        try:
            int_list = [int(item) for item in str.split(',')]
            print(sum(int_list))
        except:
            print("Не можу це зробити")

sum_numbers(str_list=['1,2,3,4', '1,2,3,4,50', 'qwerty1,2,3'])

