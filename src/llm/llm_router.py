from llm.llm_client import _llm
from langchain_core.messages import SystemMessage, HumanMessage
import json
from typing import Dict, Any
from llm.router_prompt import SYSTEM_PROMPT

def route_query(user_input: str) -> Dict[str, Any]:
    user_input = (user_input or "").strip()

    if not user_input:
        return {
            "type": "chat",
            "content": "Say something like: 'get team 254' or 'get matches for 2023ontor'."
        }

    resp = _llm.invoke([
        SystemMessage(content=SYSTEM_PROMPT),
        HumanMessage(content=user_input),
    ])

    raw = (resp.content or "").strip()

    print("=== ROUTER RAW OUTPUT ===")
    print(raw)
    print("=========================")

    return json.loads(raw)
