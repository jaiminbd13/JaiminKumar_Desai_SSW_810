import unittest
import Hw09_Wordle

class wordle_test(unittest.TestCase):

    def test_get_init(self):
            result = Hw09_Wordle.get_init()
            self.assertEqual(result)

    def test_get_word(self):
            result = Hw09_Wordle.get_word()
            self.assertEqual(result)

    def test_get_user_input(self):
            result = Hw09_Wordle.get_user_input()
            self.assertEqual(result)

    def test_check_if_entered_word_is_valid(self):
            result = Hw09_Wordle.check_if_entered_word_is_valid()
            self.assertEqual(result)

    def test_user_guessed_the_right_word(self):
            result = Hw09_Wordle.user_guessed_the_right_word()
            self.assertEqual(result)

    def test_check_valid_word(self):
            result = Hw09_Wordle.check_valid_word()
            self.assertEqual(result)

    def test_get_spot_name(self):
            result = Hw09_Wordle.get_spot_name()
            self.assertEqual(result)

    def test_check_word_in_dictionary(self):
            result = Hw09_Wordlee.check_word_in_dictionary()
            self.assertEqual(result)

    def test_get_final(self):
            result = Hw09_Wordle.get_final()
            self.assertEqual(result)

    def test_find_words(self):
            result = Hw09_Wordle.get_find_words()
            self.assertEqual(result)

    def test_match_word_alphabets(self):
            result = Hw09_Wordle.get_matched_word_alphabets()
            self.assertEqual(result)

    def test_solve(self):
            result = Hw09_Wordle.get_solve()
            self.assertEqual(result)

    def __init__(self):
        result = Hw09_Wordle.__init__()
        self.assertEqual(result)

    def test_get_words(self):
        result = Hw09_Wordle.get_words()
        self.assertEqual(result)

    def test_set_words(self):
        result = Hw09_Wordle.set_words()
        self.assertEqual(result)

    def __str__(self):
        result = Hw09_Wordle.__str__()
        self.assertEqual(result)


if __name__ == '__main__':
            unittest.main()
