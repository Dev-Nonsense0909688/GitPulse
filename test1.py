from github.config import TOKEN
import requests
from datetime import datetime
import time

HEADERS = {
    "User-Agent": "livegit",
    "Authorization": f"Bearer {TOKEN}",
    "Accept": "application/vnd.github.cloak-preview", 
}


def get_total_commits_this_year(username):
    year = datetime.utcnow().year
    query = f"author:{username} committer-date:{year}-01-01..{year}-12-31"

    url = f"https://api.github.com/search/commits?q={query}&per_page=1"
    res = requests.get(url, headers=HEADERS).json()

    return res.get("total_count", 0)

if __name__ == "__main__":
    start_time = time.time()
    print(get_total_commits_this_year("Dev-Nonsense0909688"))
    end_time = time.time() - start_time
    print(end_time)
