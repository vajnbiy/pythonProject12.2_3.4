import unittest

from unittest_proj.utils import arrs


class TestUtils(unittest.TestCase):
    def test_get(self):
        self.assertEqual(arrs.get([1, 2, 3], 1, "tests"), 2)
        self.assertEqual(arrs.get([], -1, "tests"), "tests")

    def test_slice(self):
        self.assertEqual(arrs.my_slice([1, 2, 3, 4], 1, 3), [2, 3])
        self.assertEqual(arrs.my_slice([1, 2, 3], 1), [2, 3])
        self.assertEqual(arrs.my_slice([1, 2, 3], -5), [1, 2, 3])
        self.assertEqual(arrs.my_slice([], -5), [])
        self.assertEqual(arrs.my_slice([1, 2, 3], -2), [2, 3])
