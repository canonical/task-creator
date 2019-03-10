from api import github, zenhub
import configparser


def bootstrap(config_file):
    github_token = input("Enter Github token: ")
    zenhub_token = input("Enter ZenHub token: ")
    github_repo = input("Enter GitHub repo (orga/repo): ")
    zenhub_pipeline = input(
        "Enter the pipeline where the issues should be created: "
    )

    try:
        repo_id = github.get_repo_id(github_repo)
    except Exception:
        print("Repository not found")
        exit(1)

    try:
        board = zenhub.get_board(repo_id)
    except Exception:
        print("Error when requesting zenhub api")
        exit(1)

    pipeline_id = None
    for pipeline in board["pipelines"]:
        if pipeline["name"].lower() == zenhub_pipeline.lower():
            pipeline_id = pipeline["id"]
            break

    if not pipeline_id:
        print("Pipeline not found")
        exit(1)

    config = configparser.ConfigParser()
    config.read(config_file)
    config["github"] = {}
    config["github"]["token"] = github_token
    config["github"]["repo"] = github_repo
    config["zenhub"] = {}
    config["zenhub"]["token"] = zenhub_token
    config["zenhub"]["pipeline_id"] = pipeline_id
    config["zenhub"]["repo_id"] = str(repo_id)

    with open(config_file, "w+") as configfile:
        config.write(configfile)
