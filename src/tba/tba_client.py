import os
import requests
from dotenv import load_dotenv

#loads .env file
load_dotenv()

TBA_AUTH_KEY = os.getenv("TBA_AUTH_KEY")
BASE_URL = "https://www.thebluealliance.com/api/v3"

if not TBA_AUTH_KEY:
    raise RuntimeError("TBA_AUTH_KEY not found in environment")

HEADERS = {"X-TBA-Auth-Key": TBA_AUTH_KEY}


def tba_get(path: str, params: dict | None = None):
    if not path.startswith("/"):
        path = "/" + path

    url = BASE_URL + path
    resp = requests.get(url, headers=HEADERS, params=params, timeout=10)

    if resp.status_code != 200:
        raise RuntimeError(f"TBA request failed {resp.status_code}: {resp.text}")

    return resp.json()


def get_team(team_number: int):
    return tba_get(f"/team/frc{team_number}")
