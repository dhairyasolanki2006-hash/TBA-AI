from tba.tba_client import tba_get
from tba.TBA_api_endpoints import _EVENT_KIND_TO_PATH

EVENT_KIND_TO_PATH = _EVENT_KIND_TO_PATH

def event_info(event_key: str, kind: str):
    kind = (kind or "").strip().lower()

    if kind not in EVENT_KIND_TO_PATH:
        raise ValueError("kind must be one of: matches, teams, rankings, awards, general")

    try:
        path = EVENT_KIND_TO_PATH[kind].format(event_key=event_key)
        data = tba_get(path)

        # No relevant data cases
        if data is None:
            return {"_no_data": True}

        if isinstance(data, (list, dict)) and len(data) == 0:
            return {"_no_data": True}

        return data

    except Exception:
        return {"_no_data": True}