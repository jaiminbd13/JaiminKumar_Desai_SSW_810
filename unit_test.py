import unittest
import dictionary

class Test_wordle(unittest.TestCase):
    def test_check_if_entered_word_is_valid(self):
        result = dictionary.check_if_entered_word_is_valid()
        self.assertEqual(result)


if __name__ == '__main__':
    unittest.main()