import json
from llm.llm_client import _llm
from langchain_core.messages import SystemMessage, HumanMessage

_PRESENTER_SYSTEM_PROMPT = """
You are a response formatter for an FRC assistant.

Rules:
- Answer using ONLY the provided data.
- Do NOT invent values.
- If the data does not contain the answer, say so.

Output ONLY valid JSON:
{
  "answer": "string",
  "format": "paragraph|bullets|table|mixed",
  "highlights": [],
  "followups": []
}
""".strip()

def present(question: str, tool_result: dict) -> dict:
    payload = {
        "question": question,
        "tool": tool_result.get("tool"),
        "data": tool_result.get("content"),
    }

    resp = _llm.invoke([
        SystemMessage(content=_PRESENTER_SYSTEM_PROMPT),
        HumanMessage(content=json.dumps(payload)),
    ])

    text = resp.content.strip()

    try:
        out = json.loads(text)
    except json.JSONDecodeError:
        return {
            "answer": "Unable to format response from data.",
            "format": "paragraph",
            "highlights": [],
            "followups": [],
        }

    return out