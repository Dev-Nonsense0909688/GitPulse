import json, os, time
from .config import CACHE_FILE, CACHE_TTL


def load_cache():
    if not os.path.exists(CACHE_FILE):
        return {}
    try:
        with open(CACHE_FILE, "r") as f:
            return json.load(f)
    except:
        return {}


def save_cache(cache):
    with open(CACHE_FILE, "w") as f:
        json.dump(cache, f)


def get_cached(user):
    cache = load_cache()
    if user in cache:
        entry = cache[user]
        if time.time() - entry["time"] < CACHE_TTL:
            return entry["data"]
    return None


def set_cache(user, data):
    cache = load_cache()
    cache[user] = {"time": time.time(), "data": data}
    save_cache(cache)
