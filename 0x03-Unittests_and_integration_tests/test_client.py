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

    @patch('client.GithubOrgClient.org', new_callable=property)
    def test_public_repos_url(self, mock_org):
        """Test the _public_repos_url property."""
        # Define the mocked payload for org
        mock_org.return_value = {"repos_url": "https://api.github.com/orgs/test-org/repos"}
        client = GithubOrgClient("test-org")
        self.assertEqual(client._public_repos_url, "https://api.github.com/orgs/test-org/repos")
        mock_org.assert_called_once()

    @patch('client.get_json')
    def test_public_repos(self, mock_get_json):
        """Test the public_repos method"""
        # Mocked payload to be returned by get_json
        mock_get_json.return_value = [
                {"name": "repo1", "license": {"key": "mit"}},
                {"name": "repo2", "license": {"key": "apache-2.0"}},
                {"name": "repo3", "license": {"key": "mit"}}
                ]

        # Mock _public_repos_url property to return a fake URL
        with patch('client.GithubOrgClient._public_repos_url', new_callable=property) as mock_public_repos_url:
            mock_public_repos_url.return_value = "https://api.github.com/orgs/test-org/repos"

            # Create an instance of GithubOrgClient
            client = GithubOrgClient("test-org")

            # Call public_repos method
            repos = client.public_repos()

            # Test if public_repos returns the correct list of repo names
            self.assertEqual(repos, ["repo1", "repo2", "repo3"])

            # Ensure _public_repos_url was called once
            mock_public_repos_url.assert_called_once()

            # Ensure get_json was called once with the mocked URL
            mock_get_json.assert_called_once_with("https://api.github.com/orgs/test-org/repos")

    @parameterized.expand([
        ({"license": {"key": "my_license"}}, "my_license", True),
        ({"license": {"key": "other_license"}}, "my_license", False),
        ({"license": None}, "my_license", False),  # Edge case where license is None
        ({}, "my_license", False),  # Edge case where license is missing
        ])

    def test_has_license(self, repo, license_key, expected):
        """Test the has_license method with different repo data and license keys"""
        client = GithubOrgClient("test-org")
        result = client.has_license(repo, license_key)
        self.assertEqual(result, expected)


if __name__ == "__main__":
    unittest.main()
