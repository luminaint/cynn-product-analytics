# Glossary

Plain language first, then the technical term.

| Term | Plain meaning |
|---|---|
| Grain | What one row in a table represents, e.g. "one row per user per day". Know it before joining. |
| Right-censoring | A user hasn't had enough time yet for us to know the outcome. Exclude them from the denominator. |
| PATH | The list of folders Windows searches when you type a command. First match wins. |
| Virtual environment (venv) | A private copy of Python plus packages for one project, like a separate toolbox. |
| Package | Code someone else wrote that you install and reuse, e.g. duckdb. |
| pip | Python's package installer. Use `python -m pip` so it matches the active Python. |
| Dependency | A package that another package needs; pip installs it automatically. |
| Pinning | Writing exact versions (`==`) so every install gets the same toolbox. |
| Git | A tool that saves snapshots (history) of your project. |
| Repository (repo) | A folder whose history Git tracks. |
| Commit | One saved snapshot, with a message describing what changed. |
| .gitignore | A list of files and folders Git should never save. |
| Untracked | A file Git can see but isn't saving history for yet. |
| Staging area | The files you've picked (`git add`) to go into the next commit. |

