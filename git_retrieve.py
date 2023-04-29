def get_user_info(github_client, username):
    user = github_client.get_user(username)
    print(f"Name: {user.name}")
    print(f"Bio: {user.bio}")
    print(f"Workplace: {user.company}")
    print(f"Location: {user.location}")
    return user


def get_user_repos(github_client, username):
    user = github_client.get_user(username)
    print(f"{username}'s Repositories:")
    for repo in user.get_repos():
        print(f"{repo.name} - {repo.description}")
