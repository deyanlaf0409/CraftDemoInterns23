import os
import unittest
from github import Github
from unittest.mock import MagicMock
from git_retrieve import GitHubUser


class TestGitHubUser(unittest.TestCase):

    def setUp(self):
        github_access_token = os.environ.get('GITHUB_TOKEN')
        self.github_client = Github(github_access_token)
        self.username = "deyanlaf0409"
        self.github_user = GitHubUser(self.github_client, self.username)

    def test_get_contact_info(self):
        contact_info = self.github_user.get_contact_info()

        self.assertEqual(contact_info["name"], self.github_user.user.name)
        self.assertEqual(contact_info["description"], self.github_user.user.bio)
        self.assertEqual(contact_info["email"], self.github_user.user.email)
        self.assertEqual(contact_info["address"], self.github_user.user.location)
        self.assertEqual(contact_info["job_title"], self.github_user.user.company)
        self.assertEqual(contact_info["twitter_id"], self.github_user.user.twitter_username)
        self.assertEqual(contact_info["unique_external_id"], self.github_user.user.id)

    def test_print_info(self):
        self.github_user.get_contact_info = MagicMock(return_value={"name": "Test User", "description": "Test bio", "email": "test@example.com", "address": "Test address", "job_title": "Test company", "twitter_id": "testuser", "unique_external_id": 1234})
        self.github_user.print_info()
        self.assertTrue(self.github_user.get_contact_info.called)

    def test_print_repos(self):
        self.github_user.user.get_repos = MagicMock(return_value=[MagicMock(name="repo1", description="description1"), MagicMock(name="repo2", description="description2")])
        self.github_user.print_repos()
        self.assertTrue(self.github_user.user.get_repos.called)

