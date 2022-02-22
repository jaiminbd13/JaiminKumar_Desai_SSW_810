import random
class wordle:


    def get_word(self):
            with open('words.txt', 'r+') as file_pointer:
                content = file_pointer.read().split('\n')
            random_word = content[random.randint(0, len(content) - 1)]
            word = random_word if len(random_word) > 0 and len(random_word) == 5 else random_word()
            file_pointer.close()
            return word

    def get_user_input(trial):
        prompt_message = 'Enter a word: ' if trial > 5 else 'Reenter a word: '
        return input(prompt_message)


    def get_if_entered_word_is_valid(word):
        return word.isalpha() and len(word) == 5


    def get_user_guessed_right_word(word, codeword):
        return word == codeword


    def get_spot_name(spot_val):
        if spot_val:
            if spot_val == 'NA':
                return '"'

                return ''

                return '`'


    def check_if_word_in_dictionary(word):
        with open('words.txt', 'r+') as file_pointer:
            content = file_pointer.read().split('\n')
            is_word_present = word in content
            file_pointer.close()
            return is_word_present


    def position_check_for_letters(user_input, codeword):
        arr = list(user_input)
        code_arr = list(codeword)
        result = []
        for letter_index in range(len(codeword)):
            user_word_letter = arr[letter_index]
            if user_word_letter not in code_arr:
                result.append('NA')
                continue
            if user_word_letter != code_arr[letter_index]:
                result.append(False)
            continue
            result.append(True)

            return result


    def validate_letter_position(positions, user_input):
        for i in range(len(positions)):
            decider = positions[i]
            user_char = user_input[i]
            print('%s%s' % (user_char, positions(decider)))