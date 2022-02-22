import unittest
import HW05_Jdesai_Wordle

class wordle_test(unittest.TestCase):

    def test1_get_word(self):
            result = HW05_Jdesai_Wordle.get_word()
            self.assertEqual(result)

    def test2_get_user_input(self):
            result = HW05_Jdesai_Wordle.get_user_input()
            self.assertEqual(result)

    def test3_get_if_entered_word_is_valid(self):
            result = HW05_Jdesai_Wordle.get_if_entered_word_is_valid()
            self.assertEqual(result)

    def test4_get_user_guessed_right_word(self):
            result = HW05_Jdesai_Wordle.get_user_guessed_right_word()
            self.assertEqual(result)

    def test5_get_check_valid_word(self):
            result = HW05_Jdesai_Wordle.get_check_valid_word()
            self.assertEqual(result)

    def test6_get_spot_name(self):
            result = HW05_Jdesai_Wordle.get_spot_name()
            self.assertEqual(result)

    def test7_get_check_word_in_dictionary(self):
            result = HW05_Jdesai_Wordle.get_check_if_word_in_dictionary()
            self.assertEqual(result)

    def test8_get_position_check_for_letters(self):
            result = HW05_Jdesai_Wordle.get_position_check_for_letters()
            self.assertEqual(result)

    def test9_validate_letter_position(self):
            result = HW05_Jdesai_Wordle.validate_letter_position()
            self.assertEqual(result)

if __name__ == '__main__':
            unittest.main()