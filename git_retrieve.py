import re


class GitHubUser:
    def __init__(self, github_client, username):
        self.user = github_client.get_user(username)
        self.created_at_str = self.user.created_at.strftime('%Y-%m-%d')

    def get_contact_info(self):
        other_emails = []

        # Check if user.blog is a valid email address and add it to other_emails
        if re.match(r"[^@]+@[^@]+\.[^@]+", self.user.blog):
            other_emails.append(self.user.blog)

        # Set other_emails field in contact_info if other_emails is not empty
        if other_emails:
            contact_info = {
                "name": self.user.name,
                "description": self.user.bio,
                "email": self.user.email if self.user.email else None,
                "address": self.user.location,
                "job_title": self.user.company,
                "twitter_id": self.user.twitter_username,
                "other_emails": other_emails,
                "unique_external_id": self.user.id
            }
        else:
            contact_info = {
                "name": self.user.name,
                "description": self.user.bio,
                "email": self.user.email if self.user.email else None,
                "address": self.user.location,
                "job_title": self.user.company,
                "twitter_id": self.user.twitter_username,
                "unique_external_id": self.user.id
            }

        return contact_info

    def print_info(self):
        contact_info = self.get_contact_info()

        print(f"Name: {contact_info['name']}")
        print(f"Bio: {contact_info['description']}")
        print(f"Workplace: {contact_info['job_title']}")
        print(f"Location: {contact_info['address']}")
        print(f"Email: {contact_info['email']}")
        print(f"Twitter: {contact_info['twitter_id']}")
        print(f"Blog: {self.user.blog}")
        print(f"ID: {self.user.id}")
        print(f"Created At: {self.created_at_str}")

    def print_repos(self):
        print(f"{self.user.login}'s Repositories:")
        for repo in self.user.get_repos():
            print(f"{repo.name} - {repo.description}")
