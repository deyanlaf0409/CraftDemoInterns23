import os
from github import Github


def get_user_info(github_client, username):
    user = github_client.get_user(username)
    print(f"Name: {user.name}")
    print(f"Bio: {user.bio}")



def get_user_repos(github_client, username):
    user = github_client.get_user(username)
    print(f"{username}'s Repositories:")
    for repo in user.get_repos():
        print(f"{repo.name} - {repo.description}")



personal_access_token = os.environ.get('AUTH_TOKEN')
github_client = Github(personal_access_token)
username = "deyanlaf0409"

get_user_info(github_client, username)
get_user_repos(github_client, username)
