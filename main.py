import requests
import sys

def fetch(uname):
    headers = {
        "Accept": "application/vnd.github+json",
        "X-GitHub-Api-Version": "2022-11-28"
    }

    url = f"https://api.github.com/users/{uname}/events/public"

    try:
        resp = requests.get(url, headers=headers, timeout=10)
        resp.raise_for_status()
        return resp.json()

    except requests.exceptions.RequestException as e:
        print(f"Request failed: {e}")
        sys.exit(1)


map_eve = {
    "CreateEvent": "Created repository",
    "PushEvent": "Pushed commits to",
    "WatchEvent": "Starred",
    "IssueCommentEvent": "Commented on issue in",
    "PullRequestEvent": "Closed pull request in"
}


def main():
    # Accept username from CLI arg or prompt when double-clicked.
    uname = sys.argv[1] if len(sys.argv) >= 2 else input("Enter GitHub username: ").strip()
    if not uname:
        print("Usage: github-user-activity <username>")
        sys.exit(1)

    events = fetch(uname)

    if not events:
        print(f"No recent public events for {uname}.")
        return

    for e in events:
        t = e.get("type")
        if t in map_eve:
            print(f"- {map_eve[t]} {e.get('repo', {}).get('name')}")

    input("\nPress Enter to exit...")


if __name__ == "__main__":
    main()
