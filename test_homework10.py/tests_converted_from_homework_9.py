import pytest
from tests_functions2 import even_num_sum

@pytest.mark.parametrize("even_num_sum_list, expected", [  
        ([1, 3, 5, 6, 8, 4], 18),  
        ([0, 0, 0], 0),  
        ([-1, -2, -3], -2)  
], ids=['positive numbers', 'zeros', 'negative numbers'])  
def test_even_num_sum(even_num_sum_list, expected):
    assert even_num_sum(even_num_sum_list) == expected

#наступний тест
from tests_functions2 import only_str_list

@pytest.mark.parametrize("initial_list, expected2", [
        (['1', '2', 3, True, 'False', 5, '6', 7, 8, 'Python', 9, 0, 'Lorem Ipsum'], ['1', '2', 'False', '6', 'Python', 'Lorem Ipsum'])
])
def test_only_str(initial_list, expected2):
    assert only_str_list(initial_list) == expected2

