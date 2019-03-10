from github import Github
import os

REPO = os.getenv("GITHUB_REPO")
GITHUB_TOKEN = os.getenv("GITHUB_TOKEN")

g = Github(GITHUB_TOKEN)


def create_issue(title):
    repo = g.get_repo(REPO)
    issue = repo.create_issue(title=title)

    return issue
