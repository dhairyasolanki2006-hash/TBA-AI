from tba.tba_client import get_team
from tba.semantics_tools import event_info

def execute_tool(decision: dict):

    tool = decision.get("tool")
    args = decision.get("args", {})

    if tool == "get_team":
        return {"type": "tool_result", "tool": tool, "content": get_team(**args)}

    if tool == "event_info":
        return {"type": "tool_result", "tool": tool, "content": event_info(**args)}

    return {"message": "No tool executed"}

