#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """unittest class for max_integer"""
    def test_module_docstring(self):
        """Test for module docstring"""
        m = __import__('6-max_integer').__doc__
        self.assertTrue(len(m) > 1)
    
    def test_function_docstring(self):
        """Test for function docstring"""
        f =  __import__('6-max_integer').max_integer.__doc__
        self.assertTrue(len(f) > 1)

    def test_empty_list(self):
        """Test for passing an empty list"""
        list = []
        self.assertIsNone(max_integer(list))

    def test_no_args(self):
        """Test for passing no arguments"""
        self.assertIsNone(max_integer())

    def test_one_element_in_list(self):
        """Test for only 1 element in the list"""
        list = [5]
        self.assertEqual(max_integer(list), 5)

    def test_regular_list(self):
        """Tests for max at different positions in the list"""
        list1 = [1, 4, 15, 2, 47, 98]
        list2 = [45, 10, 5, 14]
        list3 = [20, 12, 45, 125, 71, 45, 60]
        self.assertEqual(max_integer(list1), 98)
        self.assertEqual(max_integer(list2), 45)
        self.assertEqual(max_integer(list3), 125)

    def test_list_with_negative_elements(self):
        """Tests for lists containing negative numbers"""
        list1 = [1, 4, -15, -2, -47, -98]
        list2 = [-45, -10, -5, -14]
        list3 = [-20, 12, 45, -125, -71, -45, -60]
        self.assertEqual(max_integer(list1), 4)
        self.assertEqual(max_integer(list2), -5)
        self.assertEqual(max_integer(list3), 45)

    def test_none(self):
        """Test for passing None as an argument"""
        with self.assertRaises(TypeError):
            max_integer(None)

    def test_non_int(self):
        """Test for list with non-int type elements"""
        list = [2, 5, "goat", True, 45]
        with self.assertRaises(TypeError):
            max_integer(list)

if __name__ == "__main__":
    unittest.main()
