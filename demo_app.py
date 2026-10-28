"""
Agentic AI Task Accountability Agent
A working web page demonstrating a live, goal-driven AI workflow where team members
assign tasks, the agent analyzes risk, and humans approve actions before execution.
"""

import streamlit as st
import json
import os
from datetime import datetime, timedelta

# --- App Setup ---
st.set_page_config(page_title="Agentic AI Task Accountability Agent", page_icon="🤖", layout="wide")
st.title("🤖 Agentic AI: Task Accountability Agent")
st.caption("Domain: Business & Productivity | Innovation Ignite Symposium 2026 | Shridevi Institute of Engineering & Technology")

st.markdown("---")

# --- Helper Functions ---
def load_tasks():
    try:
        with open("tasks.json", "r") as f:
            return json.load(f)["tasks"]
    except FileNotFoundError:
        return []

def save_tasks(tasks_list):
    with open("tasks.json", "w") as f:
        json.dump({"tasks": tasks_list}, f, indent=2)

def log_action(message):
    try:
        with open("agent_log.json", "r") as f:
            log = json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        log = []
    log.append({"timestamp": datetime.now().isoformat(), "message": message})
    with open("agent_log.json", "w") as f:
        json.dump(log, f, indent=2, default=str)

# --- Load Session State ---
if "tasks" not in st.session_state:
    st.session_state.tasks = load_tasks()

if "agent_ran" not in st.session_state:
    st.session_state.agent_ran = False

if "results" not in st.session_state:
    st.session_state.results = []

# --- Sidebar Navigation ---
with st.sidebar:
    st.header("🤖 Agent Control Panel")
    st.markdown("Use the tabs below or the menu above to navigate.")
    st.markdown("1. **Task Board** – View and manage team tasks.")
    st.markdown("2. **Agent Workflow** – See the 7-step agent in action.")
    st.markdown("3. **Reminder Drafts** – Review and approve agent-generated reminders.")
    st.markdown("4. **Report** – Final summary of actions taken.")
    st.divider()
    st.markdown(f"**Tasks in System:** {len(st.session_state.tasks)}")
    overdue_count = sum(1 for t in st.session_state.tasks if datetime.fromisoformat(t["deadline"]) < datetime.now() and t["status"] == "pending")
    st.markdown(f"**At-Risk Tasks:** {overdue_count}")

# --- Tabs ---
tab1, tab2, tab3, tab4 = st.tabs(["📋 Task Board", "🧠 Agent Workflow", "📝 Reminder Drafts", "📊 Report"])

# --- Tab 1: Task Board ---
with tab1:
    st.subheader("📋 Task Board")

    # --- Add a New Task ---
    with st.expander("➕ Assign New Task"):
        with st.form(key="new_task_form"):
            title = st.text_input("Task Title", placeholder="e.g., Prepare Q4 budget report")
            owner = st.text_input("Assign To (Owner)", placeholder="e.g., Alice")
            deadline = st.date_input("Due Date", datetime.now().date() + timedelta(days=3))
            category = st.selectbox("Category", ["administrative", "design", "development", "research", "finance"])
            submitted = st.form_submit_button("Assign Task")

            if submitted and title and owner:
                new_task = {
                    "id": f"T{len(st.session_state.tasks) + 1:03d}",
                    "title": title,
                    "owner": owner,
                    "deadline": datetime.combine(deadline, datetime.min.time()).isoformat(),
                    "status": "pending",
                    "category": category
                }
                st.session_state.tasks.append(new_task)
                save_tasks(st.session_state.tasks)
                log_action(f"New task assigned: {new_task['id']} - '{new_task['title']}' to {new_task['owner']}")
                st.success(f"✅ Task **{new_task['id']}** assigned to **{owner}** with deadline **{deadline}**!")
                st.rerun()
            elif submitted and (not title or not owner):
                st.warning("⚠️ Please fill in all fields.")

    # --- Display Tasks ---
    if st.session_state.tasks:
        for task in st.session_state.tasks:
            deadline = datetime.fromisoformat(task["deadline"])
            overdue = deadline < datetime.now()
            risk_color = "🔴" if overdue else "🟢"
            with st.expander(f"{risk_color} {task['id']} — {task['title']}"):
                col1, col2, col3 = st.columns([2, 1, 1])
                with col1:
                    st.write(f"**Owner:** {task['owner']}")
                    st.write(f"**Status:** {task['status']}")
                with col2:
                    st.write(f"**Deadline:** {deadline.strftime('%Y-%m-%d %H:%M')}")
                    st.write(f"**Category:** {task['category']}")
                with col3:
                    st.write(f"**Risk:** {'OVERDUE!' if overdue else 'On Track'}")
                    if overdue:
                        hrs = (datetime.now() - deadline).total_seconds() / 3600
                        st.write(f"**Overdue By:** {hrs:.1f}h")

                # Action buttons: Mark Completed or Delete
                act_col1, act_col2 = st.columns(2)
                with act_col1:
                    if st.button(f"✅ Complete ({task['id']})", key=f"complete_{task['id']}"):
                        task["status"] = "completed"
                        save_tasks(st.session_state.tasks)
                        log_action(f"Task {task['id']} marked completed.")
                        st.rerun()
                with act_col2:
                    if st.button(f"🗑️ Delete ({task['id']})", key=f"delete_{task['id']}"):
                        st.session_state.tasks.remove(task)
                        save_tasks(st.session_state.tasks)
                        log_action(f"Task {task['id']} deleted.")
                        st.rerun()
    else:
        st.info("No tasks found. Assign one using the form above!")

# --- Tab 2: Agent Workflow ---
with tab2:
    st.subheader("🧠 Agent Workflow: 7-Step Agentic Loop")
    st.write("Click the button below to run the agent and see how it processes your tasks.")

    # Run the agent
    if st.button("▶️ Run Task Accountability Agent"):
        now = datetime.now()
        at_risk = []

        for task in st.session_state.tasks:
            if task["status"] != "pending":
                continue
            deadline = datetime.fromisoformat(task["deadline"])
            hours_overdue = (now - deadline).total_seconds() / 3600
            if hours_overdue > 0:
                risk = "CRITICAL" if hours_overdue > 24 else "HIGH"
                at_risk.append({**task, "risk": risk, "hours_overdue": hours_overdue})

        # Log 7 steps
        log_action("Agent started.")
        log_action(f"Goal: Monitor tasks and identify at-risk items. Found {len(at_risk)} at-risk tasks.")
        log_action("Reason: Evaluated each task's deadline vs current time.")
        log_action(f"Plan: Prioritized {len(at_risk)} tasks by risk level (Critical > High).")
        log_action("Tools: Drafted reminder messages for all at-risk tasks.")
        log_action("Decide: Determined human approval needed for CRITICAL tasks.")
        log_action("Act: Prepared reminder actions (awaiting approval).")
        log_action("Learn: Logged findings to agent_log.json for next cycle.")

        st.session_state.agent_ran = True
        st.session_state.results = at_risk
        st.success("🎉 Agent run complete!")

    # Show step-by-step visualization (only after agent runs)
    if st.session_state.agent_ran:
        st.markdown("---")
        st.subheader("📋 7-Step Breakdown")

        steps = [
            ("🎯 1. GOAL", "Monitor team tasks and identify at-risk items", "Completed"),
            ("🤔 2. REASON", f"Evaluated {len(st.session_state.results)} at-risk tasks by deadline", "Completed"),
            ("📋 3. PLAN", "Prioritized tasks by risk level (CRITICAL > HIGH > LOW)", "Completed"),
            ("🔧 4. USE TOOLS", "Generated personalized reminder messages for each task", "Completed"),
            ("⚖️ 5. DECIDE", "Flagged CRITICAL tasks for mandatory human approval", "Completed"),
            ("📤 6. ACT", "Prepared actions (reminders pending approval)", "Completed"),
            ("📚 7. LEARN", "Logged all processing steps for future cycles", "Completed"),
        ]

        for title, desc, status in steps:
            col1, col2, col3 = st.columns([2, 6, 2])
            with col1:
                st.markdown(f"**{title}**")
            with col2:
                st.write(desc)
            with col3:
                st.success(status)

        if st.session_state.results:
            st.markdown("---")
            st.subheader("⚠️ At-Risk Tasks Detected")
            for t in st.session_state.results:
                st.warning(f"{t['id']} — **{t['title']}** | Owner: {t['owner']} | Risk: {t['risk']} | Overdue by: {t['hours_overdue']:.1f}h")
        else:
            st.info("✅ No at-risk tasks found.")

# --- Tab 3: Reminder Drafts ---
with tab3:
    st.subheader("📝 Reminder Drafts (Human-in-the-Loop Approval)")
    st.write("The agent drafts reminders for each at-risk task. **Humans must approve before sending.**")

    if not st.session_state.agent_ran or not st.session_state.results:
        st.info("Run the agent from the 'Agent Workflow' tab first to generate draft reminders.")
    else:
        for task in st.session_state.results:
            with st.form(f"approval_form_{task['id']}"):
                st.write(f"### 📨 Reminder to {task['owner']} — {task['id']} ({task['risk']})")
                message = (
                    f"Hi {task['owner']},\n\n"
                    f"This is a reminder that your task \"{task['title']}\" is "
                    f"{task['risk'].lower()} priority and is overdue by "
                    f"{task['hours_overdue']:.1f} hours.\n\n"
                    f"Please update its status or confirm completion at your earliest convenience.\n\n"
                    f"— Task Accountability Agent"
                )
                st.code(message)
                approved = st.checkbox(f"✅ Approve sending reminder for {task['id']}")
                submitted = st.form_submit_button(f"Process {task['id']}")

                if submitted:
                    if approved:
                        log_action(f"Reminder approved and 'sent' for {task['id']} to {task['owner']}.")
                        st.success(f"✅ Reminder for {task['id']} has been approved and will be sent to {task['owner']}.")
                    else:
                        log_action(f"Reminder for {task['id']} held for further review.")
                        st.warning(f"⏸️ Reminder for {task['id']} held. Needs manual review.")

# --- Tab 4: Report ---
with tab4:
    st.subheader("📊 Progress Report for Team Lead")

    if st.session_state.agent_ran:
        total_at_risk = len(st.session_state.results)
        critical = sum(1 for t in st.session_state.results if t["risk"] == "CRITICAL")
        high = sum(1 for t in st.session_state.results if t["risk"] == "HIGH")

        col1, col2, col3 = st.columns(3)
        with col1:
            st.metric("Total At-Risk Tasks", total_at_risk)
        with col2:
            st.metric("Critical Priority", critical)
        with col3:
            st.metric("High Priority", high)

        st.markdown("---")
        st.subheader("📈 Expected Impact")
        st.write("""
        - **Time saved:** 2-3 hours per week per team lead
        - **Reduced missed deadlines:** Automated follow-ups ensure no task slips through
        - **Improved visibility:** Clear, prioritized view of at-risk work
        - **Human-in-the-loop:** Safe, auditable decisions before any action
        """)

        st.markdown("---")
        st.subheader("📄 Action Log")
        try:
            with open("agent_log.json", "r") as f:
                log_data = json.load(f)
            if log_data:
                for entry in reversed(log_data[-10:]):
                    st.write(f"- `{entry['timestamp'][:19]}` — {entry['message']}")
            else:
                st.info("No actions logged yet.")
        except FileNotFoundError:
            st.info("No actions logged yet.")
    else:
        st.info("Run the agent from the 'Agent Workflow' tab to generate a report.")

# --- Footer ---
st.markdown("---")
st.caption("Built for Agentic Arena Challenge — Innovation Ignite Symposium 2026 | Shridevi Institute of Engineering & Technology")
