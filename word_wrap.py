# Written by Blaine Luszcak
import unittest


class Wrapper:

    def wrap(self, text, col_max):
        text = text.rstrip()
        if text:
            final_space = text[0:col_max].rfind(' ')

            if len(text) <= col_max:
                return text

            if final_space > 0:  # if there ARE spaces in the string
                return text[0:final_space] + '\n' + self.wrap(text[final_space+1:], col_max)
            elif text[col_max] == " ":
                return text[0:col_max] + '\n' + self.wrap(text[col_max+1:], col_max)
            else:
                return text[0:col_max] + '\n' + self.wrap(text[col_max:], col_max)
        else:
            return "No text entered"


# Test class for Wrapper
class WrapTest(unittest.TestCase):

    def setUp(self):
        print("In method: ", self._testMethodName, self._)

    def test_empty(self):
        wrapTest = Wrapper()
        self.assertEqual(wrapTest.wrap('', 2), "No text entered")

    def test_blank_on_col_max(self):
        wrapTest = Wrapper()
        self.assertEqual(wrapTest.wrap('Testing col blank', 7), 'Testing\ncol\nblank')

    def test_blank_after_col(self):
        wrapTest = Wrapper()
        self.assertEqual(wrapTest.wrap('Testing col blank after col_max', 6), 'Testin\ng col\nblank\nafter\ncol_ma\nx')

    def test_blank_before_col(self):
        wrapTest = Wrapper()
        self.assertEqual(wrapTest.wrap('Testing col blank before col_max', 8), 'Testing\ncol\nblank\nbefore\ncol_max')

    def test_end_blank(self):
        wrapTest = Wrapper()
        self.assertEqual(wrapTest.wrap('Ends in a blank ', 3), 'End\ns\nin\na\nbla\nnk')

if __name__ == '__main__':
    unittest.main()

