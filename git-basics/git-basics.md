# Git Basics and Cheat Sheet

## Introduction
Git is a distributed version control system widely used for source code management in software development. It helps in tracking changes, collaboration, and maintaining project history efficiently.

---

## Installation Guide

### On Linux
```bash
sudo apt update
sudo apt install git
```

### On macOS
Using Homebrew:
```bash
brew install git
```

### On Windows
1. Download Git for Windows from [git-scm.com](https://git-scm.com/).
2. Run the installer and follow the setup wizard.
3. Use Git Bash or any terminal to access Git.

---

## Configuration
After installation, configure Git with your username and email:

```bash
git config --global user.name "hodi zoubi"
git config --global user.email hozu96@proton.me
git config --global core.editor "code --wait" # we need vscode in order to this works
git config --global core.autocrlf input # MAC, linux
git config --global core.autocrlf true # Windows
```

### Viewing Configuration
To see the current configuration:
```bash
git config --list
```
or
```bash
git config --global -e
```

### Setting Up Default Editor
Set your preferred editor for Git (e.g., VSCode):
```bash
git config --global core.editor "code --wait"
```

---

## Basic Commands Cheat Sheet

### Repository Management
| Command                          | Description                          |
|----------------------------------|--------------------------------------|
| `git init`                       | Initialize a new Git repository      |
| `git clone <repo-url>`           | Clone an existing repository         |
| `git status`                     | Show current branch and changes      |
| `git log`                        | View commit history                  |
| `git show <commit-hash>`         | Show details of a specific commit    |

### Working with Branches
| Command                          | Description                          |
|----------------------------------|--------------------------------------|
| `git branch`                     | List branches                        |
| `git branch <branch-name>`       | Create a new branch                  |
| `git checkout <branch-name>`     | Switch to another branch             |
| `git checkout -b <branch-name>`  | Create and switch to a new branch    |
| `git merge <branch-name>`        | Merge a branch into the current one  |
| `git branch -d <branch-name>`    | Delete a branch                      |

### Staging and Committing
| Command                          | Description                          |
|----------------------------------|--------------------------------------|
| `git add <file>`                 | Stage a file                         |
| `git add .`                      | Stage all changes                    |
| `git commit -m "message"`        | Commit staged changes with a message |
| `git commit -am "message"`       | Stage and commit in one command      |

### Pulling and Pushing
| Command                          | Description                          |
|----------------------------------|--------------------------------------|
| `git pull`                       | Fetch and merge changes from remote  |
| `git push`                       | Push changes to remote repository    |

### Undoing Changes
| Command                          | Description                          |
|----------------------------------|--------------------------------------|
| `git restore <file>`             | Discard changes in a file            |
| `git reset <file>`               | Unstage a file                       |
| `git revert <commit-hash>`       | Revert a commit                      |

---

## Git Workflow

1. Clone the repository:
    ```bash
    git clone <repo-url>
    ```
2. Make changes and stage them:
    ```bash
    git add <file>
    ```
3. Commit your changes:
    ```bash
    git commit -m "Commit message"
    ```
4. Push the branch to the remote repository:
    ```bash
    git push origin <branch-name>
    ```
5. Create a pull request for review.

---

## Diagrams

### Git Commit Lifecycle
```plaintext
Working Directory → Staging Area → Repository
                  |              |
              (git add)     (git commit)
```
---

## Additional Tips

1. Use `.gitignore` to exclude files from version control.
   Example `.gitignore`:
   ```
   node_modules/
   *.log
   .env
   ```

3. Clean up local branches:
   ```bash
   git branch -d <branch-name>
   ```

4. Use aliases for frequent commands:
   ```bash
   git config --global alias.st status
   git config --global alias.co checkout
   ```

---

## Resources
- [Git Documentation](https://git-scm.com/doc)
- [Git Cheat Sheet](https://education.github.com/git-cheat-sheet-education.pdf)
