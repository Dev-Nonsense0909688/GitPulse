import math
from datetime import datetime, timedelta


def calculate_streak(dates):
    today = datetime.utcnow().date()
    d = today if today.isoformat() in dates else today - timedelta(days=1)

    streak = 0
    while d.isoformat() in dates:
        streak += 1
        d -= timedelta(days=1)
    return streak


def calculate_score(data):
    return int(
        math.log1p(data["stars"]) * 20
        + math.log1p(data["forks"]) * 18
        + math.log1p(data["followers"]) * 25
        + math.log1p(data["repos"]) * 12
        + math.sqrt(data["recent_activity"]) * 15
        + math.log1p(data["stars"] / (data["repos"] + 1)) * 30
    )


def get_grade(score):
    if score >= 900:
        return "A+"
    if score >= 800:
        return "A"
    if score >= 700:
        return "B"
    if score >= 600:
        return "C"
    if score >= 500:
        return "D"
    return "F"
