import resend
from config.settings import settings
resend.api_key = settings.resend_api_key
def send_talent_digest(email, name, html, month):
    resend.Emails.send({"from": settings.talent_from_email, "to": email, "subject": f"Talent & Advisor Briefing — {month}",
        "html": f"<html><body style='font-family:sans-serif;max-width:700px;margin:auto'><h2 style='color:#1a237e'>👥 Talent & Advisor Briefing</h2><p>{month} — {name}</p><hr/>{html}<hr/><p style='font-size:12px;color:#999'>The Faulkner Group Advisors</p></body></html>"})
