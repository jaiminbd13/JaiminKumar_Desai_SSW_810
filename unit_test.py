import unittest
import dictionary
import wordle
import ui


class Test_wordle(unittest.TestCase):

        def test_get_word(self):
            result = dictionary.get_word()
            self.assertEqual(result)

        def test_check_if_entered_word_is_valid(self):
            result = dictionary.check_if_entered_word_is_valid()
            self.assertEqual(result)

        def test_get_user_input(self):
            result = dictionary.has_user_guessed_the_right_word()
            self.assertEqual(result)

        def test_check_valid_word(self):
            result = dictionary.check_if_entered_word_is_valid()
            self.assertEqual(result)

         def test_user_guessed_the_right_word(self):
            result = dictionary.has_user_guessed_the_right_word()
            self.assertEqual(result)

        def test_get_spot_name(self):
            result = dictionary.get_spot_name()
            self.assertEqual(result)

        if __name__ == '__main__':
            unittest.main()