import configparser


def get_configuration(config_file):
    config = configparser.ConfigParser()
    config.read(config_file)

    return config


def set_env_from_config(config, github_api, zenhub_api):
    github_api.set_env(config["github"]["token"], config["github"]["repo"])
    zenhub_api.set_env(
        config["zenhub"]["token"],
        config["zenhub"]["repo_id"],
        config["zenhub"]["pipeline_id"],
    )


def bootstrap(config_file, github_api, zenhub_api):
    github_token = input("Enter Github token: ")
    zenhub_token = input("Enter ZenHub token: ")
    github_repo = input("Enter GitHub repo (orga/repo): ")
    zenhub_pipeline = input(
        "Enter the pipeline where the issues should be created: "
    )

    try:
        github_api.set_env(github_token, github_repo)
        repo_id = github_api.get_repo_id()
    except Exception:
        print("Repository not found")
        exit(1)

    try:
        zenhub_api.set_env(zenhub_token, repo_id, zenhub_pipeline)
        board = zenhub_api.get_board()
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

    config = get_configuration(config_file)
    config["github"] = {}
    config["github"]["token"] = github_token
    config["github"]["repo"] = github_repo
    config["zenhub"] = {}
    config["zenhub"]["token"] = zenhub_token
    config["zenhub"]["pipeline_id"] = pipeline_id
    config["zenhub"]["repo_id"] = str(repo_id)

    with open(config_file, "w+") as configfile:
        config.write(configfile)

    return config
