import argparse
import os
from github import Github
from git_retrieve import get_user_info, get_user_repos

if __name__ == "__main__":
    # Parse command line arguments
    parser = argparse.ArgumentParser(description='Retrieve information of a GitHub User')
    parser.add_argument('username', type=str, help='GitHub username')
    args = parser.parse_args()
    username = args.username

    personal_access_token = os.environ.get('AUTH_TOKEN')
    github_client = Github(personal_access_token)

    get_user_info(github_client, username)
    get_user_repos(github_client, username)

