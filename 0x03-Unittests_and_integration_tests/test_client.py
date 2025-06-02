#!/usr/bin/env python3

from unittest.mock import patch, PropertyMock
import unittest
from client import GithubOrgClient
from parameterized import parameterized
from typing import Dict


class TestGithubOrgClient(unittest.TestCase):
    """
    - Test the GithubOrgClient class and methods

    """
   # @patch('client.get_json')
    @parameterized.expand([
        ("google", {"name": "google"}),
        ("abc", {"name": "abc"}),
        ])
    def test_org(self, org_name, expected_payload):
        """
        - test for the function that makes network calls and
        return json data with the organisation name
        - confirm that get_jon is called once
        - Use mocks to make sure that no external HTTP calls are made
        """
        # create the mock object 'mock_get_json' that will replace the get_json()
        with patch('client.get_json' ) as mock_get_json:
            # specify what to expect when our patch module is called
            mock_get_json.return_value = expected_payload
            # call the main class and pass the orgaisation name
            client = GithubOrgClient(org_name)
            result = client.org

            # confirm that the output given is the same as the expected payload
            self.assertEqual(result, expected_payload)
            expected_url = f"https://api.github.com/orgs/{org_name}"
            # confirm that our mocked function is called once
            mock_get_json.assert_called_once()

    def test_public_repos_url(self):
        """
        - tests that the org() returns the correct output
        - we wil be using context managers
        """
        with patch.object(GithubOrgClient, 'org', new_callable=PropertyMock) as mock_org:
            known_payload = {"repos_url": "https://api.github.com/my_org/repos"}
            mock_org.return_value = known_payload

            client = GithubOrgClient('my_org')
            result = client._public_repos_url

            self.assertEqual(result, known_payload['repos_url'])


if __name__ == '__main__':
    unittest.main()

