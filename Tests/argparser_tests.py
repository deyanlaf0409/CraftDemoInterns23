import unittest
import argparse
from unittest.mock import patch
from parse_user_input import parse_arguments


class TestParseArguments(unittest.TestCase):

    @patch('argparse.ArgumentParser.parse_args', return_value=argparse.Namespace(username='testuser', domain='testdomain.freshdesk.com'))
    def test_parse_arguments(self, mock_args):
        username, domain = parse_arguments()
        self.assertEqual(username, 'testuser')
        self.assertEqual(domain, 'testdomain.freshdesk.com')
