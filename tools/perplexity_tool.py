import httpx
from config.settings import settings

def research_talent(query: str) -> str:
    headers = {"Authorization": f"Bearer {settings.perplexity_api_key}", "Content-Type": "application/json"}
    payload = {
        "model": "sonar",
        "messages": [
            {"role": "system", "content": "You are a talent and advisor researcher for women's health tech startups. Surface: clinical advisors with women's health expertise, potential board members, key executive hires (CMO, VP Clinical, Head of Growth), and clinical champions at health systems. For each person return: name, current role, organization, relevant expertise, why they are a fit, and LinkedIn URL if available."},
            {"role": "user", "content": query},
        ],
    }
    resp = httpx.post("https://api.perplexity.ai/chat/completions", json=payload, headers=headers, timeout=30)
    resp.raise_for_status()
    return resp.json()["choices"][0]["message"]["content"]
