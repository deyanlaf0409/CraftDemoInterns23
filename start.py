import os
from github import Github
from parse_user_input import parse_arguments
from git_retrieve import get_user_info, get_user_repos
from freshdesk_transfer import freshdesk_dump

if __name__ == "__main__":
    username, domain = parse_arguments()

    github_access_token = os.environ.get('GITHUB_TOKEN')
    github_client = Github(github_access_token)

    user = get_user_info(github_client, username)
    get_user_repos(github_client, username)

    freshdesk_api_key = os.environ.get('FRESHDESK_API')
    password = "x"
    contact_info = {"name": user.name, "email": "api_v2_user6@example.com"}
    headers = {"Content-Type": "application/json"}

    freshdesk_dump(domain, freshdesk_api_key, password, contact_info, headers)

