"""
Agentic AI Prototype: Intelligent Task Accountability Agent
Domain: Business & Productivity
Event: Innovation Ignite Symposium 2026 - Agentic Arena Challenge

Workflow: GOAL -> REASON -> PLAN -> USE TOOLS -> DECIDE -> ACT -> LEARN & ITERATE
"""

import json
from datetime import datetime, timedelta

TASKS_FILE = "tasks.json"
LOG_FILE = "agent_log.json"


def load_tasks():
    """Load tasks from JSON data source."""
    with open(TASKS_FILE, "r") as f:
        return json.load(f)["tasks"]


def save_log(log_entry):
    """Append an action to the agent's learning log."""
    try:
        with open(LOG_FILE, "r") as f:
            log = json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        log = []
    log.append(log_entry)
    with open(LOG_FILE, "w") as f:
        json.dump(log, f, indent=2)


# ============================================================
# 1. GOAL
# ============================================================
GOAL = """
Find overdue team tasks, prioritize follow-ups by risk level,
and generate reminder messages for team leads to review and approve.
"""


def show_goal():
    print("\n" + "=" * 60)
    print("AGENT GOAL")
    print("=" * 60)
    print(GOAL.strip())


# ============================================================
# 2. REASON
# ============================================================
def reason_about_tasks(tasks, now):
    """
    Reasoning step: evaluate each task for risk level.
    Returns list of tasks with risk assessments.
    """
    print("\n" + "=" * 60)
    print("STEP 2 - REASONING: Evaluating task risk levels...")
    print("=" * 60)

    analyzed = []
    for task in tasks:
        if task["status"] != "pending":
            continue

        deadline = datetime.fromisoformat(task["deadline"])
        time_remaining = deadline - now
        hours_overdue = (now - deadline).total_seconds() / 3600

        if time_remaining < timedelta(hours=0):
            # Task is overdue
            risk = "CRITICAL" if hours_overdue > 24 else "HIGH"
            reason = f"Deadline missed by {abs(hours_overdue):.1f} hours"
        elif hours_overdue > 0:
            risk = "HIGH"
            reason = f"Due in {hours_overdue:.1f} hours - urgent"
        else:
            risk = "LOW"
            reason = f"On track, due in {time_remaining.days} days"

        analyzed.append({
            **task,
            "risk": risk,
            "hours_overdue": hours_overdue,
            "reason": reason,
            "due_in_days": time_remaining.days if time_remaining > timedelta(hours=0) else 0
        })

        print(f"  [{task['id']}] {task['title'][:35]:<35} | Owner: {task['owner']:<8} | Risk: {risk:<8} | {reason}")

    return analyzed


# ============================================================
# 3. PLAN
# ============================================================
def plan_actions(analyzed_tasks):
    """
    Planning step: sort tasks by risk and decide order of action.
    """
    print("\n" + "=" * 60)
    print("STEP 3 - PLAN: Prioritizing follow-up actions...")
    print("=" * 60)

    # Sort: CRITICAL first, then HIGH, then by hours_overdue desc
    risk_order = {"CRITICAL": 0, "HIGH": 1, "LOW": 2}
    planned = sorted(
        analyzed_tasks,
        key=lambda t: (risk_order.get(t["risk"], 99), -t["hours_overdue"])
    )

    print("  Execution order (highest risk first):")
    for i, t in enumerate(planned, 1):
        print(f"    {i}. {t['id']} - {t['title']} (Owner: {t['owner']}, Risk: {t['risk']})")

    return planned


# ============================================================
# 4. USE TOOLS
# ============================================================
def draft_reminder(task):
    """
    Tool usage step: draft a reminder message using an LLM-style template.
    """
    return {
        "to": task["owner"],
        "task_id": task["id"],
        "title": task["title"],
        "deadline": task["deadline"],
        "risk": task["risk"],
        "message": (
            f"Hi {task['owner']},\n\n"
            f"This is a reminder that your task \"{task['title']}\" "
            f"is {task['risk'].lower()} priority and was due on {task['deadline'][:10]}.\n"
            f"Please update its status or confirm completion.\n\n"
            f"— Task Accountability Agent"
        )
    }


def compile_progress_report(planned_tasks):
    """Tool usage step: compile a summary report for the team lead."""
    total = len(planned_tasks)
    critical = sum(1 for t in planned_tasks if t["risk"] == "CRITICAL")
    high = sum(1 for t in planned_tasks if t["risk"] == "HIGH")

    return {
        "generated_at": datetime.now().isoformat(),
        "total_overdue": total,
        "critical_count": critical,
        "high_count": high,
        "tasks": [
            {
                "id": t["id"],
                "title": t["title"],
                "owner": t["owner"],
                "risk": t["risk"],
                "hours_overdue": round(t["hours_overdue"], 1) if t["hours_overdue"] > 0 else 0
            }
            for t in planned_tasks
        ]
    }


# ============================================================
# 5. DECIDE
# ============================================================
def decide_action(task):
    """
    Decision step: determine if agent can act autonomously or needs human approval.
    Rule: CRITICAL risk -> human approval required before sending.
    """
    if task["risk"] == "CRITICAL":
        return "NEEDS_APPROVAL"
    return "AUTO_SEND"


# ============================================================
# 6. ACT
# ============================================================
def execute_action(task, reminder, decision, human_approved=False):
    """
    Action step: perform the actual action (send reminder).
    Returns action result.
    """
    if decision == "NEEDS_APPROVAL" and not human_approved:
        return {
            "task_id": task["id"],
            "action": "reminder_drafted",
            "status": "PENDING_APPROVAL",
            "message": f"Reminder drafted for {task['owner']} but requires human approval before sending."
        }

    # Simulate sending the reminder
    return {
        "task_id": task["id"],
        "action": "reminder_sent",
        "status": "COMPLETED",
        "message": f"Reminder sent to {task['owner']} regarding '{task['title']}'."
    }


# ============================================================
# 7. LEARN & ITERATE
# ============================================================
def log_learning(summary):
    """Record what happened so the agent can improve next cycle."""
    save_log(summary)
    print("\n" + "=" * 60)
    print("STEP 7 - LEARN: Recording outcomes for future iterations...")
    print("=" * 60)
    print(f"  {summary['message']}")


# ============================================================
# MAIN AGENT LOOP
# ============================================================
def run_agent():
    now = datetime.now()

    print("\n" + "#" * 60)
    print("#  AGENTIC AI: Intelligent Task Accountability Agent  #")
    print("#  Domain: Business & Productivity                   #")
    print("#  Event: Agentic Arena - Innovation Ignite 2026     #")
    print("#" * 60)

    # Step 1: Show goal
    show_goal()

    # Load tasks
    tasks = load_tasks()
    print(f"\n  Loaded {len(tasks)} tasks from data source.")

    # Step 2: Reason
    analyzed = reason_about_tasks(tasks, now)

    # Filter only overdue or at-risk tasks
    at_risk = [t for t in analyzed if t["risk"] != "LOW"]

    if not at_risk:
        print("\n  No overdue or at-risk tasks found. All clear!")
        return

    # Step 3: Plan
    planned = plan_actions(at_risk)

    # Step 4: Use tools - draft reminders
    print("\n" + "=" * 60)
    print("STEP 4 - USE TOOLS: Drafting reminder messages...")
    print("=" * 60)

    reminders = []
    for task in planned:
        reminder = draft_reminder(task)
        reminders.append(reminder)
        print(f"\n  Drafted reminder for {task['id']}:")
        print(f"    To: {reminder['to']}")
        print(f"    Subject: Task Reminder - {reminder['title']}")
        print(f"    Message preview: {reminder['message'][:60]}...")

    # Step 5 & 6: Decide + Act
    print("\n" + "=" * 60)
    print("STEP 5-6 - DECIDE & ACT: Executing actions...")
    print("=" * 60)

    results = []
    human_approved = False  # Simulates human-in-the-loop approval

    for task, reminder in zip(planned, reminders):
        decision = decide_action(task)
        result = execute_action(task, reminder, decision, human_approved=human_approved)
        results.append(result)

        status_icon = "[OK]" if result["status"] == "COMPLETED" else "[PENDING]"
        print(f"  {status_icon} {task['id']} -> {result['status']}: {result['message']}")

    # Step 7: Compile report and log
    report = compile_progress_report(planned)
    print("\n" + "=" * 60)
    print("STEP 7 - REPORT: Progress Summary for Team Lead")
    print("=" * 60)
    print(f"  Total at-risk tasks: {report['total_overdue']}")
    print(f"  Critical priority:   {report['critical_count']}")
    print(f"  High priority:       {report['high_count']}")
    print(f"  Report generated:    {report['generated_at'][:19]}")

    summary = {
        "cycle_time": datetime.now().isoformat(),
        "tasks_processed": report["total_overdue"],
        "reminders_drafted": len(reminders),
        "reminders_sent": sum(1 for r in results if r["status"] == "COMPLETED"),
        "pending_approval": sum(1 for r in results if r["status"] == "PENDING_APPROVAL"),
        "message": f"Agent cycle complete: {report['total_overdue']} tasks reviewed, reminders drafted for team lead approval."
    }
    log_learning(summary)

    print("\n" + "#" * 60)
    print("#  Agent cycle complete. See agent_log.json for history.  #")
    print("#" * 60 + "\n")


if __name__ == "__main__":
    run_agent()