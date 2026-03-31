import requests
from requests.adapters import HTTPAdapter
from urllib3.util.retry import Retry
from .config import TOKEN 

session = requests.Session()
session.headers.update(
    {
        "User-Agent": "livegit",
        "Authorization": f"Bearer {TOKEN}",
        "Accept": "application/vnd.github+json",
    }
)

retry = Retry(total=3, backoff_factor=0.3)
adapter = HTTPAdapter(max_retries=retry)
session.mount("https://", adapter)


class GitHubAPIError(Exception):
    pass


def _get(url):
    res = session.get(url, timeout=8)

    if res.status_code == 404:
        raise GitHubAPIError("User not found")

    if not res.ok:
        raise GitHubAPIError(f"{res.status_code}: {url}")

    return res.json()
