#!/usr/bin/env python3
"""
     This file tests for all cases of the utils methods in the utils.py file
"""
from typing import Dict, List, Any, Sequence
from utils import access_nested_map, get_json
import unittest
from unittest.mock import patch
from parameterized import parameterized

class TestAccessNestedMap(unittest.TestCase):
    """
    This class houses the test methods that test all testcases of the acces_nested_map

    The class inherits form unittest class and used the TestCase methods

    """

    @parameterized.expand([
        ({"a":1}, ["a"], 1),
        ({"a":{"b": 2}}, ["a", "b"], 2),
        ({"a":{"b":2}}, ["a", "b"], 2),
        ])
    def test_access_nested_map(self, nested_map: Dict, path: Sequence, expected_result: Any) -> None:
        """
        test if the path can traverse the nested map and give expected results
        """

        self.assertEqual(access_nested_map(nested_map, path), expected_result)

    @parameterized.expand([
        ({}, ["a"], 'a'),
        ({"a":1}, ["a", "b"], 'b')
        ])
    def test_access_nested_map_exception(self, nested_map: Dict, path: Sequence, expected_result):
        """
        test if keyError is raised for the passed parameters 
        """
        with self.assertRaises(KeyError) as cm:
            access_nested_map(nested_map, path)
        self.assertEqual(f"'{expected_result}'", str(cm.exception) )


class TestGetJson(unittest.TestCase):
    """
    test The get_json() method to any calls
    our primary goal is to avoid making any external HTTP network calls and thus, we will be using mocks
    """

    @parameterized.expand([
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False})
        ])
    def test_get_json(self, test_url, test_payload):
        """
        Make network calls using mocks to test if get_json works as expected
        """
        with patch('utils.requests.get') as mock_get:
            mock_get.return_value.json.return_value= test_payload

            result = get_json(test_url)

            self.assertEqual(result, test_payload)










if __name__=='__main__':
    unittest.main()
