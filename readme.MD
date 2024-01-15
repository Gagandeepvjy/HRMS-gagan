# Human Resource Management Serv

Human Management Serv

# Contributing To Human Resource Management Serv
​
There is a whole lot of work to do and it needs to be done in manner such that is easily manageable and understanable. This allows us to create a stable application.
Feel free to raise a pull request to [the main repository](https://github.com/Santhoshcv19/HRMS/pulls) . The maintainers would review your proposed modifications and, if appropriate, merge
your changes into our code. In case of some changes, we'll have a discussion and iron the code out.
​
## Getting Started
​
1. Create your own fork repository.
​
```bash
# Clone it
$ git clone [path_to_your_fork]
​
# Change directory
$ cd vpropel-v2
​
# Add the upstream repo
$ git remote add upstream git@github.com:Santhoshcv19/HRMS.git
```

2. Configuring Environment

Setting up development environment.

**Step 1**: Install make
 - windows (Run in power shell)
    ```bash
      winget install GnuWin32.Make
    ```
    Add ```C:\Program Files (x86)\GnuWin32\bin``` to path
 - Linux based system
    ```bash
    sudo apt-get -y install make
    ```
**Step 2**: Install poetry
  ```bash
  pip install poetry
  ```
**Step 3**: Install dependencies
  ```bash
  poetry install
  ```
**Step 4**: Run server
  ```bash
   make run-server
  ```
​
## Making Changes
​
1. Make all your changes in a `topic branch` created from your fork's `develop`. Here example of GraphQL is used for explanation purposes.
​
   `$ git fetch upstream && git checkout GraphQL && git rebase upstream/GraphQL`
   `$ git checkout GraphQL && git checkout -b <topic-branch-name>`
​
2. Make sure that your changes adhere to the current coding conventions used throughout the project, indentation, accurate comments, etc.
3. Lint your code regularly and ensure it passes prior to submitting a PR
4. Ensure existing tests pass and include test cases which fail without your change and succeed with it.
​
## Commit Message Naming Guidelines
​
1. Commit messages should be of the format `commit-type(Affected-Section): Description of the task that has been implemented.`
2. Commit Types can be from the following: `chore, feat, docs, style, fix, refactor, test`
​
An example can be: `docs(Guidelines): Added initial files for documentation`
​
## Submitting Changes
1. Run tests for dJango with the following command `python3 manage.py test`.
2. Before commiting a new change, make sure pre-commit hooks are installed.
```bash
    make setup-hooks
```
3. Commit your changes. When making a new commit, `pre-commit` will run linters on all staged files as for django. Resolve any remaining issues reported by the linters, stage the changed files and attempt to commit again until resolution.
4. Locally merge (or rebase) the upstream branch into your topic branch: `$ git checkout <topic-branch-name> && git fetch upstream && git rebase upstream/GraphQL <topic-branch-name>`. The topic branch name should follow this convention of `<Jira Ticket Number> - <Title of the subtask>`. For eg say the ticket number is HRMS-12 and the subtask title is `Initializing the repository`. The branch name should be `HRMS-12-initializing-the-repository`. Note all the subtask title should all be in lowercase. Only the ticket number should be specified in the way it is.
5. Push your topic branch up to your fork: `$ git push origin <topic-branch-name>`.
6. Open a Pull Request with a clear title and description.
​
Note: All the migration files associated with the backend changes will be ignored.
​
## After your PR is merged
​
1. You may choose to delete the topic branch.
2. Update your local copy's `GraphQL` branch with the `upstream`'s updated `GraphQL`:
​
   `$ git fetch upstream && git checkout GraphQL && git rebase upstream/GraphQL`
​
3. Push the updated GraphQL branch to `origin`:
​
   `$ git push origin GraphQL`
​
You will be all updated and ready to make new changes now
​
If you have any questions about contributing, feel free to reach out the repository maintainers.
