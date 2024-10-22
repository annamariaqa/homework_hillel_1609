import unittest
from tests_functions import even_num_sum

class TestSumFunction(unittest.TestCase):
    def test_even_num_sum_1(self):
        actual_result = even_num_sum([1, 3, 5, 6, 8, 4])
        expected_result = 18
        self.assertEqual(actual_result, expected_result)

    def test_even_num_sum_2(self):
        actual_result = even_num_sum([2, 5, 7, 4])
        expected_result = 6
        self.assertEqual(actual_result, expected_result)
    
    def test_even_num_sum_3(self):
        actual_result = even_num_sum([3, 7, 9, 11])
        expected_result = 0
        self.assertEqual(actual_result, expected_result)

if __name__ == '__main__':
    unittest.main()



