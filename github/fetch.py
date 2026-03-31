from concurrent.futures import ThreadPoolExecutor, as_completed
from .api import _get
from .config import BASE_URL, SINCE_DATE


def fetch_user(user):
    return _get(f"{BASE_URL}/users/{user}")


def fetch_repos(user, max_pages=10):
    repos = []
    for page in range(1, max_pages + 1):
        batch = _get(f"{BASE_URL}/users/{user}/repos?per_page=100&page={page}")
        if not batch:
            break
        repos.extend(batch)
    return repos


def fetch_commit_dates(user, repos):
    dates = set()
    repos = sorted(repos, key=lambda r: r["stargazers_count"], reverse=True)[:10]

    def get_dates(repo):
        try:
            commits = _get(
                f"{BASE_URL}/repos/{user}/{repo}/commits"
                f"?author={user}&since={SINCE_DATE}&per_page=100"
            )
            return {
                c["commit"]["author"]["date"][:10] for c in commits if c.get("commit")
            }
        except:
            return set()

    with ThreadPoolExecutor(max_workers=12) as ex:
        futures = [ex.submit(get_dates, r["name"]) for r in repos]
        for f in as_completed(futures):
            dates |= f.result()

    return dates
