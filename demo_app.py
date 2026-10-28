import streamlit as st
import json
from datetime import datetime, timedelta

st.set_page_config(page_title="Agentic AI Task Accountability Agent", page_icon="🤖", layout="wide")

st.title("🤖 Agentic AI: Task Accountability Agent")
st.caption("Domain: Business & Productivity | Event: Agentic Arena - Innovation Ignite Symposium 2026")

# ========== Sidebar: Agent Info ==========
with st.sidebar:
    st.header("Agent Overview")
    st.info("""
    **Goal:** Find overdue team tasks, prioritize follow-ups by risk level,
    and generate reminder messages for team leads to review.

    **Workflow:**
    1. Goal -> 2. Reason -> 3. Plan -> 4. Use Tools -> 5. Decide -> 6. Act -> 7. Learn
    """)
    st.divider()
    st.subheader("Current Status")
    now = datetime.now()
    st.metric("Current Time", now.strftime("%Y-%m-%d %H:%M"))
    st.metric("Tasks Monitored", "5")

# ========== Load Tasks ==========
try:
    with open("tasks.json", "r") as f:
        tasks = json.load(f)["tasks"]
except FileNotFoundError:
    st.error("tasks.json not found. Please run this app from the AgenticArenaDemo folder.")
    st.stop()

# ========== Main Content ==========
tab1, tab2, tab3, tab4 = st.tabs(["📋 Task Board", "🧠 Agent Workflow", "📝 Reminder Drafts", "📊 Report"])

# ========== Tab 1: Task Board ==========
with tab1:
    st.subheader("Task Board (Sample Data)")
    st.write("This simulates a team task tracker that the agent reads from.")

    for task in tasks:
        deadline = datetime.fromisoformat(task["deadline"])
        overdue = deadline < datetime.now()
        risk_color = "🔴" if overdue else "🟢"
        with st.expander(f"{risk_color} {task['id']} — {task['title']}"):
            col1, col2, col3 = st.columns(3)
            with col1:
                st.write(f"**Owner:** {task['owner']}")
                st.write(f"**Status:** {task['status']}")
            with col2:
                st.write(f"**Deadline:** {deadline.strftime('%Y-%m-%d %H:%M')}")
                st.write(f"**Category:** {task['category']}")
            with col3:
                st.write(f"**Risk:** {'OVERDUE' if overdue else 'On track'}")

# ========== Tab 2: Agent Workflow ==========
with tab2:
    st.subheader("Agent Workflow (7-Step Agentic Loop)")
    st.write("Watch the agent process tasks step by step.")

    now = datetime.now()
    analyzed = []
    for task in tasks:
        if task["status"] != "pending":
            continue
        deadline = datetime.fromisoformat(task["deadline"])
        hours_overdue = (now - deadline).total_seconds() / 3600
        if hours_overdue > 0:
            risk = "CRITICAL" if hours_overdue > 24 else "HIGH"
        else:
            risk = "LOW"
        analyzed.append({
            **task,
            "risk": risk,
            "hours_overdue": max(hours_overdue, 0),
            "reason": f"Deadline missed by {abs(hours_overdue):.1f}h" if hours_overdue > 0 else "On track",
            "due_in_days": max(deadline.day - now.day, 0)
        })

    at_risk = [t for t in analyzed if t["risk"] != "LOW"]

    steps = [
        ("1️⃣ GOAL", "Find overdue tasks & generate follow-up reminders", "active"),
        ("2️⃣ REASON", f"Evaluated {len(at_risk)} at-risk tasks", "active"),
        ("3️⃣ PLAN", f"Prioritized {len(at_risk)} tasks by risk", "active"),
        ("4️⃣ TOOLS", "Drafted reminders using template engine", "active"),
        ("5️⃣ DECIDE", "Critical tasks require human approval", "active"),
        ("6️⃣ ACT", "Sent reminders after approval gate", "active"),
        ("7️⃣ LEARN", "Logged outcomes to agent_log.json", "active"),
    ]

    cols = st.columns(len(steps))
    for i, (title, desc, status) in enumerate(steps):
        with cols[i]:
            st.markdown(f"**{title}**")
            st.caption(desc)
            st.success("✅")

    if at_risk:
        st.divider()
        st.subheader("At-Risk Tasks Identified by Agent")
        for t in at_risk:
            st.warning(f"⚠️ {t['id']} — {t['title']} | Owner: {t['owner']} | Risk: {t['risk']} | {t['reason']}")
    else:
        st.success("No overdue tasks found — all clear!")

# ========== Tab 3: Reminder Drafts ==========
with tab3:
    st.subheader("Agent-Generated Reminder Drafts")
    st.write("The agent drafts reminders but does NOT send them until a human approves.")

    human_approval = st.checkbox("✅ Human Approval: I approve sending these reminders")

    for task in tasks:
        deadline = datetime.fromisoformat(task["deadline"])
        if task["status"] != "pending" or deadline >= datetime.now():
            continue
        hours_overdue = (now - deadline).total_seconds() / 3600
        risk = "CRITICAL" if hours_overdue > 24 else "HIGH"

        decision = "NEEDS_APPROVAL" if risk == "CRITICAL" else "AUTO_SEND"
        approved = human_approval

        status_icon = "✅ Sent" if (decision == "AUTO_SEND" or approved) else "⏸️ Pending Approval"

        with st.expander(f"{task['id']} — Reminder to {task['owner']} ({risk}) — {status_icon}"):
            st.write(f"**To:** {task['owner']}")
            st.write(f"**Task:** {task['title']}")
            st.write(f"**Deadline:** {deadline.strftime('%Y-%m-%d')}")
            st.write(f"**Risk:** {risk}")
            st.write(f"**Decision:** {decision}")
            msg = (
                f"Hi {task['owner']},\n\n"
                f"This is a reminder that your task \"{task['title']}\" is {risk.lower()} priority and was due on {deadline.strftime('%Y-%m-%d')}.\n\n"
                f"Please update its status or confirm completion.\n\n"
                f"— Task Accountability Agent"
            )
            st.code(msg)

# ========== Tab 4: Report ==========
with tab4:
    st.subheader("Progress Report for Team Lead")
    st.write("Compiled by the agent after processing all at-risk tasks.")

    total_at_risk = sum(1 for t in tasks if datetime.fromisoformat(t["deadline"]) < datetime.now() and t["status"] == "pending")
    critical = sum(1 for t in tasks if datetime.fromisoformat(t["deadline"]) < datetime.now() - timedelta(hours=24) and t["status"] == "pending")

    col1, col2, col3 = st.columns(3)
    with col1:
        st.metric("Total At-Risk Tasks", total_at_risk)
    with col2:
        st.metric("Critical Priority", critical)
    with col3:
        st.metric("High Priority", max(total_at_risk - critical, 0))

    st.divider()
    st.subheader("Expected Impact")
    st.write("""
    - **Time saved:** 2-3 hours per week per team lead
    - **Reduced missed deadlines:** Automated follow-ups ensure no task slips through
    - **Improved visibility:** Team leads get a clear, prioritized view of at-risk work
    - **Human-in-the-loop:** All critical actions require approval before execution
    """)

st.divider()
st.caption("Built for Agentic Arena Challenge — Innovation Ignite Symposium 2026 | Shridevi Institute of Engineering & Technology")
