import argparse
import os
from pathlib import Path

from task_creator import config
from task_creator.api.github import GithubApi
from task_creator.api.zenhub import ZenhubApi


def parse_arguments(arguments):
    parser = argparse.ArgumentParser(
        description=("A CLI tool to add issues in an epic")
    )

    parser.add_argument(
        "epic-id",
        type=int,
        help=("This is the epic where the issue will be added"),
    )

    parser.add_argument(
        "estimate", type=int, help=("Estimation of the epic (fibonacci)")
    )

    parser.add_argument(
        "title", type=str, help=("Title of the issue to create")
    )

    arguments = vars(parser.parse_args(arguments))

    return {name: value for name, value in arguments.items() if value}


def main(system_arguments):
    github_api = GithubApi()
    zenhub_api = ZenhubApi()
    config_file = str(Path.home()) + "/.task-creator.ini"
    if not os.path.isfile(config_file):
        configparser = config.bootstrap(config_file, github_api, zenhub_api)
    else:
        configparser = config.get_configuration(config_file)
        config.set_env_from_config(configparser, github_api, zenhub_api)

    arguments = parse_arguments(system_arguments)

    issue = github_api.create_issue(arguments["title"])

    zenhub_api.move_issue_to_epic(arguments["epic-id"], issue.number)
    zenhub_api.estimate_issue(issue.number, arguments["estimate"])
    zenhub_api.move_to_in_progress(issue.number)

    print("Issue created")
