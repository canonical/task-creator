import requests

ZENHUB_API = "https://api.zenhub.io"

ESTIMATE_ISSUE = "".join(
    [ZENHUB_API, "/p1/repositories/{repo_id}/issues/{issue_id}/estimate"]
)

UPDATE_ISSUE_EPIC = "".join(
    [ZENHUB_API, "/p1/repositories/{repo_id}/epics/{epic_id}/update_issues"]
)

MOVE_TO_PIPELINE = "".join(
    [ZENHUB_API, "/p1/repositories/{repo_id}/issues/{issue_id}/moves"]
)

REPOSITORY_BOARD = "".join([ZENHUB_API, "/p1/repositories/{repo_id}/board"])


class ZenhubApi:
    def __init__(self):
        self.session = requests.Session()

    def set_env(self, token, repo_id, pipeline_id):
        self.headers = {"X-Authentication-Token": token}
        self.repo_id = repo_id
        self.pipeline_id = pipeline_id

    def move_issue_to_epic(self, epic_id, issue_id):
        json = {
            "add_issues": [
                {"repo_id": int(self.repo_id), "issue_number": issue_id}
            ]
        }

        url = UPDATE_ISSUE_EPIC.format(repo_id=self.repo_id, epic_id=epic_id)
        response = self.session.post(url=url, headers=self.headers, json=json)

        return response

    def estimate_issue(self, issue_id, estimate):
        json = {"estimate": estimate}

        response = self.session.put(
            url=ESTIMATE_ISSUE.format(repo_id=self.repo_id, issue_id=issue_id),
            headers=self.headers,
            json=json,
        )

        return response

    def move_to_in_progress(self, issue_id):
        json = {"pipeline_id": self.pipeline_id, "position": "top"}
        response = self.session.post(
            url=MOVE_TO_PIPELINE.format(
                repo_id=self.repo_id, issue_id=issue_id
            ),
            headers=self.headers,
            json=json,
        )

        return response

    def get_board(self):
        response = self.session.get(
            url=REPOSITORY_BOARD.format(repo_id=self.repo_id),
            headers=self.headers,
        )

        return response.json()
