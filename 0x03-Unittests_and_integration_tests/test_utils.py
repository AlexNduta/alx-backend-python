#!/usr/bin/env python3
""" test for the utils.access_nested_map function"""
from parameterized import parameterized
import utils
from typing import Mapping, Sequence, Any
import unittest


class TestAccessNestedMap(unittest.TestCase):
    """"test method"""
    
    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2),
    ])
    def test_access_nested_map(self, nested_map: Mapping, path: Sequence, expected):
        """Check if the required output is given"""
        self.assertEqual(utils.access_nested_map(nested_map, path), expected)

