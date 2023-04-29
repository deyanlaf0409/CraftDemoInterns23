import argparse
import os
from github import Github
from git_retrieve import get_user_info, get_user_repos
from freshdesk_transfer import freshdesk_dump

if __name__ == "__main__":
    # Parse command line arguments
    parser = argparse.ArgumentParser(description='Retrieve information of a GitHub User')
    parser.add_argument('username', type=str, help='GitHub username')
    args = parser.parse_args()
    username = args.username


    github_access_token = os.environ.get('AUTH_TOKEN')
    github_client = Github(github_access_token)

    user = get_user_info(github_client, username)
    get_user_repos(github_client, username)


    #freshdesk_api_key = "m63d39XmdjEJuMNKvYi"
    domain = "none8662"  # to get from user
    password = "x"
    contact_info = {"name": user.name, "email": "api_v2_user5@example.com"}
    headers = {"Content-Type": "application/json"}

    freshdesk_dump(domain, 'FRESHDESK_KEY', password, contact_info, headers)
