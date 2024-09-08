#!/usr/bin/env python3
"""
Unit test for utils.access_nested_map.
"""


import unittest
from unittest.mock import patch, Mock
from parameterized import parameterized
from utils import get_json, access_nested_map, memoize


class TestAccessNestedMap(unittest.TestCase):
    """Test case for the access_nested_map function"""

    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2)
        ])
    def test_access_nested_map(self, nested_map, path, expected):
        """Test access_nested_map with various inputs."""
        self.assertEqual(access_nested_map(nested_map, path), expected)

    @parameterized.expand([
        ({}, ("a",)),
        ({"a": 1}, ("a", "b"))
        ])
    def test_access_nested_map_exception(self, nested_map, path):
        """Test that KeyError is raised for invalid paths."""
        with self.assertRaises(KeyError) as context:
            access_nested_map(nested_map, path)
            self.assertEqual(str(context.exception), str(path[-1]))


class TestGetJson(unittest.TestCase):
    """Test case for the get_json function"""

    @parameterized.expand([
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False})
        ])

    @patch('utils.requests.get')
    def test_get_json(self, test_url, test_payload, mock_get):
        """Test get_json returns expected payload and mocks requests.get"""
        # Mock the response to return the test_payload
        mock_response = Mock()
        mock_response.json.return_value = test_payload
        mock_get.return_value = mock_response

        # Call the function with the test URL
        result = get_json(test_url)

        # Assert that requests.get was called once with the correct URL
        mock_get.assert_called_once_with(test_url)

        # Assert that the result from get_json matches the expected test_payload
        self.assertEqual(result, test_payload)


class TestMemoize(unittest.TestCase):
    """Test case for the memoize decorator"""

    class TestClass:
        """A test class to demonstrate the memoize decorator"""

        def a_method(self):
            """A method that returns 42"""
            return 42

        @memoize
        def a_property(self):
            """A memoized property that calls a_method"""
            return self.a_method()

    @patch.object(TestClass, 'a_method')
    def test_memoize(self, mock_a_method):
        """Test that memoize caches the result and only calls a_method once"""
        mock_a_method.return_value = 42  # Mock a_method to return 42

        # Create an instance of TestClass
        test_instance = self.TestClass()

        # Access a_property twice
        result1 = test_instance.a_property
        result2 = test_instance.a_property

        # Assert the results are correct
        self.assertEqual(result1, 42)
        self.assertEqual(result2, 42)

        # Assert a_method is only called once
        mock_a_method.assert_called_once()


if __name__ == '__main__':
    unittest.main()
