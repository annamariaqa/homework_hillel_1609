import unittest
from tests_functions import only_str_list

class TestStrFunction(unittest.TestCase):
    def test_only_str_1(self):
        actual_result = only_str_list(lst1=['1', '2', 3, True, 'False', 5, '6', 7, 8, 'Python', 9, 0, 'Lorem Ipsum'])
        expected_result = ['1', '2', 'False', '6', 'Python', 'Lorem Ipsum']
        self.assertEqual(actual_result, expected_result)

    def test_only_str_2(self):
        actual_result = only_str_list(lst1=[7, 8, 9, None])
        expected_result = []
        self.assertEqual(actual_result, expected_result)

if __name__ == '__main__':
    unittest.main()