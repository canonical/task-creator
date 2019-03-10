import argparse
import sys

from api import github, zenhub


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
    arguments = parse_arguments(system_arguments)

    issue = github.create_issue(arguments["title"])

    zenhub.move_issue_to_epic(arguments["epic-id"], issue.number)
    zenhub.estimate_issue(issue.number, arguments["estimate"])
    zenhub.move_to_in_progress(issue.number)

    print("Issue created")


if __name__ == "__main__":
    main(sys.argv[1:])
