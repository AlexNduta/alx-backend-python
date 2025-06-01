#!/usr/bin/env python3
"""
     This file tests for all cases of the utils methods in the utils.py file
"""
from typing import Dict, List, Any, Sequence
from utils import access_nested_map
import unittest
from parameterized import parameterized

class TestAccessNestedMap(unittest.TestCase):
    """
    This class houses the test methods that test all testcases of the acces_nested_map

    The class inherits form unittest class and used the TestCase methods

    """

    @parameterized.expand([
        ({"a":1}, ["a"], 1),
        ({"a":{"b": 2}}, ["a", "b"], 2),
        ({"a":{"b":{"c":1}}}, ["a", "b", "c"], 1),
        ({"a":{"b":2}}, ["a", "b"], 2),
        ({"x":{"y":{"z":20}}}, ["x", "y", "z"], 20),
        ])

    def test_access_nested_map(self, nested_map: Dict, path: Sequence, expected_result: Any) -> None:
        """
        test if the path can traverse the nested map and give expected results
        """

        self.assertEqual(access_nested_map(nested_map, path), expected_result)

if __name__=='__main__':
    unittest.main()
