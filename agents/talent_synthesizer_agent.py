from crewai import Agent

TALENT_STRUCTURE = """
## 🌟 Recommended Advisors (top 5, ranked by fit)
## 💼 Board Prospects (top 3 per seat type)
## 👤 Executive Hire Candidates (top 3 per open role)
## 🏥 Clinical Champions (health system contacts for pilot conversations)
## 🔗 Warm Path Notes (how to get introduced to each person)
"""

talent_synthesizer = Agent(
    role="Talent & Advisor Briefing Synthesizer",
    goal="Synthesize all talent and advisor signals into a prioritized monthly briefing with warm path introductions for each recommendation.",
    backstory="You are a network strategist who knows that the right introduction changes everything. You don't just surface names — you map the warm path.",
    tools=[], verbose=True, allow_delegation=False,
)
TALENT_PROMPT = TALENT_STRUCTURE
