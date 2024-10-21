import unittest
from tests_functions import longest_word

class TestWordFunction(unittest.TestCase):
    def test_longest_w_1(self):
        actual_result = longest_word(words=['Hello', 'how', 'are', 'you', 'feeling'])
        expected_result = 'feeling'
        self.assertEqual(actual_result, expected_result)

    def test_longest_w_2(self):
        actual_result = longest_word(words=['its', 'me', 'here'])
        expected_result = 'here'
        self.assertEqual(actual_result, expected_result)

    def test_longest_w_3(self):
        actual_result = longest_word(words=['nice', 'outside', 'now'])
        expected_result = 'outside'
        self.assertEqual(actual_result, expected_result)

    def test_longest_w_4(self):
        actual_result = longest_word(words=['maybe', 'tomorrow', 'we', 'meet'])
        expected_result = 'tomorrow'
        self.assertEqual(actual_result, expected_result)
        
if __name__ == '__main__':
    unittest.main()