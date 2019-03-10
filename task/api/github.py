import os

from github import Github

REPO = os.getenv("GITHUB_REPO")
GITHUB_TOKEN = os.getenv("GITHUB_TOKEN")

g = Github(GITHUB_TOKEN)


def create_issue(title):
    repo = g.get_repo(REPO)
    issue = repo.create_issue(title=title)

    return issue


def get_repo_id(repo_name):
    repo = g.get_repo(repo_name)

    return repo.id
