from llm.llm_router import route_query
from llm.presenter import present
from executor import execute_tool

def handle_query(user_input: str):

    routed = route_query(user_input)

    try:
        # If response of routed is of type tool
        if isinstance(routed, dict) and routed.get("type") == "tool":
            tool_result = execute_tool(routed)
            formatted = present(user_input, tool_result)
            return formatted.get("answer", "")

        response = routed

        # If response of routed is of type chat or out of scope
        if isinstance(routed, dict):
            return routed.get("content", str(routed))
        return str(routed)


    except Exception:
        return str("something went wrong in handling the query")