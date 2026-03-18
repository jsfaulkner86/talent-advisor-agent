from crewai import Crew, Task
from agents.advisor_agent import advisor_agent
from agents.board_agent import board_agent
from agents.hiring_agent import hiring_agent
from agents.talent_synthesizer_agent import talent_synthesizer, TALENT_PROMPT
from delivery.email_digest import send_talent_digest
from delivery.notion_push import push_to_notion
from db.supabase_client import save_digest
from profiles.founder_profiles import FOUNDER_PROFILES
from datetime import datetime

def run_pipeline():
    month = datetime.now().strftime("%B %Y")
    for profile in FOUNDER_PROFILES:
        tasks = [
            Task(description=f"Find advisors for {profile['indication']} {profile['stage']} company. Advisor needs: {profile['advisor_needs']}", agent=advisor_agent, expected_output="List of advisors with name, role, org, fit rationale, LinkedIn."),
            Task(description=f"Find board prospects. Board needs: {profile['board_needs']}", agent=board_agent, expected_output="List of board prospects with name, role, expertise, fit rationale."),
            Task(description=f"Find candidates for open roles: {profile['open_roles']}. Gaps: {profile['current_team_gaps']}", agent=hiring_agent, expected_output="List of candidates per role with name, current org, and fit rationale."),
            Task(description=f"Synthesize talent briefing for {profile['founder_name']}.\n{TALENT_PROMPT}", agent=talent_synthesizer, expected_output="Structured HTML talent briefing."),
        ]
        crew = Crew(agents=[advisor_agent, board_agent, hiring_agent, talent_synthesizer], tasks=tasks, verbose=True)
        result = crew.kickoff()
        result_str = result if isinstance(result, str) else str(result)
        save_digest({"client_id": profile["client_id"], "month": month, "briefing": result_str})
        push_to_notion(profile["client_id"], profile["founder_name"], result_str, month)
        send_talent_digest(profile["email"], profile["founder_name"], result_str, month)
    print("[TalentAdvisorAgent] Monthly run complete.")

if __name__ == "__main__":
    run_pipeline()
