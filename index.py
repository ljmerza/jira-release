import os

from dotenv import load_dotenv
from fastapi import FastAPI, HTTPException
from fastapi.templating import Jinja2Templates
from jira import JIRA
from starlette.requests import Request
from starlette.responses import RedirectResponse

load_dotenv()

JIRA_URL = os.getenv("JIRA_URL")
JIRA_USERNAME = os.getenv("JIRA_USERNAME")
JIRA_API_TOKEN = os.getenv("JIRA_API_TOKEN")


jira = JIRA(server=JIRA_URL, basic_auth=(JIRA_USERNAME, JIRA_API_TOKEN))
app = FastAPI()
templates = Jinja2Templates(directory="templates")

@app.get("/")
def redirect_to_docs():
    return RedirectResponse(url="/docs")

@app.put("/tickets/{ticket_key}/title")
async def update_ticket_title(ticket_key: str, new_title: str):
    try:
        ticket = jira.issue(ticket_key)
        ticket.update(fields={"summary": new_title})
        return {"status": "success", "message": f"Title of ticket {ticket_key} updated to: {new_title}"}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@app.get("/filters/{filter_id}/tickets")
async def view_tickets_from_filter(request: Request, filter_id: str):
    try:
        tickets = get_tickets(filter_id)
        return templates.TemplateResponse("tickets.html", {"request": request, "tickets": tickets, "JIRA_URL": JIRA_URL })
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@app.get("/filters/{filter_id}/tickets/ready")
async def view_ready_tickets_from_filter(request: Request, filter_id: str):
    try:
        tickets = get_tickets(filter_id)
        ready_to_release_tickets = [ticket for ticket in tickets if ticket['status'] == "Ready to Release"]
        return templates.TemplateResponse("tickets.html", {"request": request, "tickets": ready_to_release_tickets, "JIRA_URL": JIRA_URL })
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

def get_tickets(filter_id):
    jql = jira.filter(filter_id).jql
    issues = jira.search_issues(jql)

    tickets = []
    for issue in issues:
        ticket_data = {
            "key": issue.key,
            "summary": issue.fields.summary,
            "description": issue.fields.description,
            "status": issue.fields.status.name,
            "assignee": issue.fields.assignee.displayName if issue.fields.assignee else None,
        }
        tickets.append(ticket_data)
    return tickets

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8305)