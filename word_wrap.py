# Written by Blaine Luszcak
import unittest


class Wrapper:

    def wrap(self, text, col_max):
        if text:  # checking if word exists or not
            if len(text) <= col_max:
                return text
            else:
                return text[0:col_max] + '\n' + self.wrap(text[col_max:], col_max)
        else:
            print("No text entered")


if __name__ == '__main__':

    wrapTest = Wrapper()
    test_blank = wrapTest.wrap('', 2)  # what happens when we don't enter text
    test = wrapTest.wrap('Hi my name is Blaine', 3)  # what happens when we enter text but more than col_max
