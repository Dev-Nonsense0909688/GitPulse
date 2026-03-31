import os
from datetime import datetime, timedelta

BASE_URL = "https://api.github.com"
SINCE_DATE = (datetime.utcnow() - timedelta(days=365)).isoformat() + "Z"
TOKEN = os.getenv("GITHUB_TOKEN")
CACHE_FILE = "cache.json"
CACHE_TTL = 3600

if not TOKEN:
    raise RuntimeError("GITHUB_TOKEN not set")
