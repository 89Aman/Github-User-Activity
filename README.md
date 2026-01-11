# GitHub User Activity

A CLI tool to fetch and display GitHub user activity.

## Download

- Grab the latest `github-user-activity.exe` from the project’s GitHub Releases page and run it directly—no Python needed.

## Run (prebuilt binary)

- From terminal: `github-user-activity.exe <username>`
- Double-click: a prompt appears asking for the GitHub username; after activity prints, press Enter to close the window.

## Run from source (Python)

```bash
uv add requests
python main.py <username>
```

## Build a release binary yourself (Windows)

```bash
pip install pyinstaller
pyinstaller --name github-user-activity --onefile main.py
# output: dist/github-user-activity.exe
```
