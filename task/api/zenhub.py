import requests
import os

ZENHUB_API = "https://api.zenhub.io"

ZENHUB_TOKEN = os.getenv("ZENHUB_TOKEN")
BASE_SQUAD_REPO_ID = os.getenv("BASE_SQUAD_REPO_ID")
PIPELINE_ID = os.getenv("PIPELINE_ID")

ESTIMATE_ISSUE = "".join(
    [ZENHUB_API, "/p1/repositories/{repo_id}/issues/{issue_id}/estimate"]
)

UPDATE_ISSUE_EPIC = "".join(
    [ZENHUB_API, "/p1/repositories/{repo_id}/epics/{epic_id}/update_issues"]
)

MOVE_TO_PIPELINE = "".join(
    [ZENHUB_API, "/p1/repositories/{repo_id}/issues/{issue_id}/moves"]
)

HEADERS = {"X-Authentication-Token": ZENHUB_TOKEN}

session = requests.Session()


def move_issue_to_epic(epic_id, issue_id):
    json = {
        "add_issues": [
            {"repo_id": BASE_SQUAD_REPO_ID, "issue_number": issue_id}
        ]
    }

    response = session.post(
        url=UPDATE_ISSUE_EPIC.format(
            repo_id=BASE_SQUAD_REPO_ID, epic_id=epic_id
        ),
        headers=HEADERS,
        json=json,
    )

    return response


def estimate_issue(issue_id, estimate):
    json = {"estimate": estimate}

    response = session.put(
        url=ESTIMATE_ISSUE.format(
            repo_id=BASE_SQUAD_REPO_ID, issue_id=issue_id
        ),
        headers=HEADERS,
        json=json,
    )

    return response


def move_to_in_progress(issue_id):
    json = {pipeline: PIPELINE_ID, position: "top"}
    response = session.post(
        url=MOVE_TO_PIPELINE.format(
            repo_id=BASE_SQUAD_REPO_ID, issue_id=issue_id
        ),
        headers=HEADERS,
        json=json,
    )

    return response
