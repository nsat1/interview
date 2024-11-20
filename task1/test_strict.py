import unittest

from solution import sum_two


class TestStrictDecorator(unittest.TestCase):

    def test_valid_arg(self):
        result = sum_two(1, 2)
        self.assertEqual(result, 3)

    def test_invalid_arg(self):
        with self.assertRaises(TypeError):
            sum_two(1, 2.4)

        with self.assertRaises(TypeError):
            sum_two('1', 2)

        with self.assertRaises(TypeError):
            sum_two(1, '2')

    def test_empty_arg(self):
        with self.assertRaises(TypeError):
            sum_two()


if __name__ == '__main__':
    unittest.main()
