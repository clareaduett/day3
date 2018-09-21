import unittest

from find_number import find_number


class test_sort_list(unittest.TestCase):
    def test_find_missing(self):
        self.assertEqual(find_number([1, 2, 3, 5, 6, 7, 9]), [4, 8])
        self.assertEqual(find_number([1, 2, 3, 5, 6, 7, 9]), [4, 8])

    def test_list(self):
        self.assertRaises(TypeError, find_number,'123')
        self.assertRaises(TypeError, find_number, '123')