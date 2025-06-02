#!/usr/bin/env python3

from unittest.mock import patch
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
        # specify what data we should be expecting
        # the call to the mock function 
        #expected_payload = {"name": org_name}
        #mock_get_json.return_value = expected_payload

        # create an instance of our class so that
        # we can be able to use the org() method
        #client = GithubOrgClient(org_name)
        #result = client.org
        #self.assertEqual(result, expected_payload)
        #expected_url = f"https://api.github.com/orgs/{org_name}"
        # check if our mock method was called once 
        #mock_get_json.assert_called_once(expected_url)
        with patch('client.get_json' ) as mock_get_json:
            mock_get_json.return_value = expected_payload
            client = GithubOrgClient(org_name)
            result = client.org

            self.assertEqual(result, expected_payload)
            expected_url = f"https://api.github.com/orgs/{org_name}"

            mock_get_json.assert_called_once()



if __name__ == '__main__':
    unittest.main()

