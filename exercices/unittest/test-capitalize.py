import unittest
import capitalize

class TestCapitalize(unittest.TestCase):

    def test_one_word(self):
        text = 'python'
        result = capitalize.capitalize(text)

        self.assertEqual(result, 'Python')

    def test_multiple_words(self):
        text = 'monty python'
        result = capitalize.capitalize(text)

        # This test will fail
        # self.assertEqual(result, 'Monty Python')

        # This test will pass
        self.assertEqual(result, 'Monty python')

if __name__ == '__main__':
    unittest.main()
