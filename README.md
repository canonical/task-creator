# Task

**This project is a work in progress.**

A cool CLI tool to create an issue on GitHub, add it to a Zenhub epic, estimate it and move it to the Zenhub pipeline "In progress".

## Usage

```
usage: task.py [-h] epic-id estimate title

A CLI tool to add issues in an epic

positional arguments:
  epic-id     This is the epic where the issue will be added
  estimate    Estimation of the epic (fibonacci)
  title       Title of the issue to create

optional arguments:
  -h, --help  show this help message and exit
```

## Install

- Generate a new token on [Github](https://github.com/settings/tokens) with repos scope.
- Generate a new token on [Zenhub](https://app.zenhub.com/dashboard/tokens). **Be sure about this task, it will delete all existing tokens of the dashboard.**
- Add these environment variables:

```bash
export ZENHUB_TOKEN=TOKEN
export REPO_ID=REPO_ID
export PIPELINE_ID=PIPELINE
export GITHUB_REPO="REPO/NAME"
export GITHUB_TOKEN=TOKEN
```

- Now run `python task/task.py EPIC_NUMBER ESTIMATE "Title Of the issue"`
- On you board the issue should be added under the epic EPIC_NUMBER with an estimate ESTIMATE and with the correct title.


## Todo

- [ ] Simplier installation
  - [ ] Alternative to environment variable (file `~/.taskrc` ?)
  - [ ] Installer bootstrap on first run
- [ ] Generic code
  - [ ] Get PIPELINE_ID from API calls instead of harcoded (to do on bootstrap?)
  - [ ] Get REPO_ID  from API calls instead of harcoded (to do on bootstrap?)
- [ ] Add issue to current iteration
- [ ] Features ideas
  - [ ] Save epic-id to avoid rewriting it when every time
  - [ ] Add close argument that should close the last issue created
- [ ] Push to pypi
- [ ] Create snap
