from crewai import Agent
from tools.perplexity_tool import research_talent

board_agent = Agent(
    role="Board Prospect Researcher",
    goal="Identify board member prospects for women's health tech companies: healthcare investors who join boards, health system executives who advise startups, and patient advocates with governance experience.",
    backstory="Board composition is a fundraising signal. You find board prospects who add credibility with payers, investors, and health systems simultaneously.",
    tools=[research_talent], verbose=True, allow_delegation=False,
)
