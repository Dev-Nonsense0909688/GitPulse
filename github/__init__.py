from concurrent.futures import ThreadPoolExecutor
from .fetch import fetch_user, fetch_repos, fetch_commit_dates
from .logic import calculate_streak, calculate_score, get_grade
from .cache import get_cached, set_cache
from test1 import get_total_commits_this_year
import requests
import base64

def get_github_data(user):
    cached = get_cached(user)
    if cached:
        return cached

    with ThreadPoolExecutor(max_workers=3) as ex:
        user_f = ex.submit(fetch_user, user)
        repos_f = ex.submit(fetch_repos, user)

        user_data = user_f.result()
        repos = repos_f.result()

    commit_dates = fetch_commit_dates(user, repos)
    commits = get_total_commits_this_year(user)

    stars = forks = watchers = prs = 0
    languages = {}

    for r in repos:
        stars += r.get("stargazers_count", 0)
        forks += r.get("forks_count", 0)
        watchers += r.get("watchers_count", 0)
        prs += r.get("open_issues_count", 0)

        if lang := r.get("language"):
            languages[lang] = languages.get(lang, 0) + 1

    avatar = user_data.get("avatar_url")

    try:
        img = requests.get(avatar, timeout=5).content
        b64 = base64.b64encode(img).decode()
        avatar = f"data:image/png;base64,{b64}"
    except:
        avatar = ""

    data = {
        "username": user_data.get("login"),
        "handle": user_data.get("login"),
        "avatar_url": avatar,
        "followers": user_data.get("followers", 0),
        "stars": stars,
        "repos": len(repos),
        "repo_count": len(repos),
        "commits": commits,
        "prs": prs,
        "streak": calculate_streak(commit_dates),
        "forks": forks,
        "watchers": watchers,
        "recent_activity": len(commit_dates),
        "top_languages": dict(
            sorted(languages.items(), key=lambda x: x[1], reverse=True)[:5]
        ),
        "extra": "Active Now.",
    }

    data["score"] = calculate_score(data)
    data["grade"] = get_grade(data["score"])

    set_cache(user, data)
    return data
