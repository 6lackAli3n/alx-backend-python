#!/usr/bin/env python3
"""
Unit tests for GithubOrgClient.
"""


import unittest
from unittest.mock import patch
from parameterized import parameterized
from client import GithubOrgClient


class TestGithubOrgClient(unittest.TestCase):
    """Test case for the GithubOrgClient class"""

    @parameterized.expand([
        ("google",),
        ("abc",)
    ])
    @patch('client.get_json')
    def test_org(self, org_name, mock_get_json):
        """Test that GithubOrgClient.org returns the correct organization data."""
        # Mocked return value for the get_json method
        mock_org_data = {"login": org_name}
        mock_get_json.return_value = mock_org_data

        # Create an instance of GithubOrgClient
        client = GithubOrgClient(org_name)

        # Call the org method and capture the result
        result = client.org

        # Ensure that get_json was called once with the correct URL
        mock_get_json.assert_called_once_with(f"https://api.github.com/orgs/{org_name}")

        # Ensure that the returned result matches the mocked organization data
        self.assertEqual(result, mock_org_data)


if __name__ == "__main__":
    unittest.main()
