from github import Github


class GithubApi:
    def __init__(self):
        self.repo_name = ""
        self.g = None

    def set_env(self, token, repo_name):
        self.set_token(token)
        self.set_repository(repo_name)

    def set_token(self, token):
        self.g = Github(token)

    def set_repository(self, repo_name):
        self.repo_name = repo_name

    def create_issue(self, title):
        repo = self.g.get_repo(self.repo_name)
        issue = repo.create_issue(title=title)

        return issue

    def get_repo_id(self):
        repo = self.g.get_repo(self.repo_name)
        self.repo_id = repo.id
        return repo.id
