import re


def get_user_info(github_client, username):
    user = github_client.get_user(username)
    other_emails = []

    # Check if user.blog is a valid email address and add it to other_emails
    if re.match(r"[^@]+@[^@]+\.[^@]+", user.blog):
        other_emails.append(user.blog)

    # Set other_emails field in contact_info if other_emails is not empty
    if other_emails:
        contact_info = {
            "name": user.name,
            "description": user.bio,
            "email": user.email if user.email else None,
            "address": user.location,
            "job_title": user.company,
            "twitter_id": user.twitter_username,
            "other_emails": other_emails
        }
    else:
        contact_info = {
            "name": user.name,
            "description": user.bio,
            "email": user.email if user.email else None,
            "address": user.location,
            "job_title": user.company,
            "twitter_id": user.twitter_username,
            "unique_external_id": user.id
        }

    # Print user information
    print(f"Name: {user.name}")
    print(f"Bio: {user.bio}")
    print(f"Workplace: {user.company}")
    print(f"Location: {user.location}")
    print(f"Email: {user.email}")
    print(f"Twitter: {user.twitter_username}")
    print(f"Blog: {user.blog}")
    print(f"ID: {user.id}")

    return contact_info


def get_user_repos(github_client, username):
    user = github_client.get_user(username)
    print(f"{username}'s Repositories:")
    for repo in user.get_repos():
        print(f"{repo.name} - {repo.description}")
