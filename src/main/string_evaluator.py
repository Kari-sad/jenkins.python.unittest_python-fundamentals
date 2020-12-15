# Created by Leon Hunter at 3:57 PM 10/23/2020
class StringManipulator(object):
    def get_hello_world(self):
            return "Hello World"

    def concatenate(self, value_to_be_added_to, value_to_add):
            return str(value_to_be_added_to) + str(value_to_add)

    def substring_inclusive(self , string_to_fetch_from, starting_index, ending_index):
        string_to_fetch_from = str(string_to_fetch_from)
        start = int(starting_index)
        end = int(ending_index) + 1
        s = string_to_fetch_from[start:end]
        return s

    def substring_exclusive(self, string_to_fetch_from, starting_index, ending_index):
        string_to_fetch_from = str(string_to_fetch_from)
        start = int(starting_index)+1
        end = int(ending_index)
        s = string_to_fetch_from[start:end]
        return s

    def compare(self, first_value, second_value):
        if str(first_value) in ("None", "False"):
            first_value = 0
        elif str(first_value) == ("True"):
            first_value = 1
        elif str(second_value) in ("None", "False"):
            second_value = 0
        elif str(second_value) == ("True"):
            second_value = 1

        is_equal = (str(first_value) == str(second_value))
        return is_equal

    def get_middle_character(self, string_to_fetch_from):
            return string_to_fetch_from[len(string_to_fetch_from) / 2]  # Round?

    def get_first_word(self, string_to_fetch_from):
            return string_to_fetch_from.split()[0]

    def get_second_word(self, string_to_fetch_from):
            return string_to_fetch_from.split()[1]

    def reverse(self, string_to_be_reversed):
            return string_to_be_reversed[::-1]
