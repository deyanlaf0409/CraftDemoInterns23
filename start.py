import os
from github import Github
from git_retrieve import *
from parse_user_input import parse_arguments
from freshdesk_transfer import freshdesk_dump


def launch(username=None, domain=None):
    if username is None and domain is None:
        username, domain = parse_arguments()

    github_access_token = os.environ.get('GITHUB_TOKEN')
    github_client = Github(github_access_token)

    user = GitHubUser(github_client, username)
    contact = user.get_contact_info()
    user.print_info()

    # freshdesk_api_key = os.environ.get('FRESHDESK_TOKEN')
    # print(freshdesk_api_key)
    freshdesk_api_key = 'N5UzLMgWOBRaYONW2qZ'
    password = "x"
    headers = {"Content-Type": "application/json"}

    freshdesk_dump(domain, freshdesk_api_key, password, contact, headers)

if __name__ == "__main__":
    launch()
