# AGENTIC ARENA CHALLENGE - 2026
## Project: Intelligent Task Accountability Agent
**Domain:** Business & Productivity  
**Event:** Innovation Ignite Symposium 2026 (Shridevi Institute of Engineering and Technology)

---

### 🚀 Quick Start Guide for Symposium

#### 1. What We Built:
- **`tasks.json`**: Sample team task database containing pending and overdue tasks.
- **`agent.py`**: A fully functional command-line AI Agent implementing the official **7-Step Agentic Loop**:
  1. **Goal** (Understand objective)
  2. **Reason** (Evaluate deadline risk & urgency)
  3. **Plan** (Prioritize tasks by risk level)
  4. **Use Tools** (Query task store, draft reminder templates)
  5. **Decide** (Determine if human approval is needed)
  6. **Act** (Execute reminders / queue actions)
  7. **Learn** (Log outcomes to `agent_log.json`)
- **`demo_app.py`**: A stunning interactive web interface built with Streamlit for your live demo!

---

#### 2. How to Run the Demo on Your Laptop:

1. Open **Command Prompt** or **PowerShell** and navigate to the folder:
   ```bash
   cd C:\Users\USER\Desktop\AgenticArenaDemo
   ```

2. **Run the Console Agent (Terminal Demo):**
   ```bash
   python agent.py
   ```
   *Watch the agent reason, plan, prioritize, and log actions live in the terminal!*

3. **Run the Interactive Web Dashboard (Live UI Demo):**
   *(Make sure streamlit is installed: `pip install streamlit`)*
   ```bash
   streamlit run demo_app.py
   ```
   *This opens a browser window showing the Task Board, Live 7-Step Workflow, Reminder Drafts with Human Approval Gate, and Impact Report!*

---

#### 3. How to Pitch This to the Judges (Round 1 - 5 Minutes):

* **Problem (30s):** "Team leads and student groups waste 2–3 hours every week chasing overdue tasks and compiling manual progress updates."
* **Solution (1s Statement):** "An autonomous **Task Accountability Agent** that monitors team deadlines, reasons about risk, drafts follow-ups, and prepares executive reports — with human-in-the-loop approval."
* **The Agentic Workflow (2m):** Walk through the 7 steps:
  * **Goal:** Monitor tasks.
  * **Reason:** Detect missed deadlines (`hours_overdue`).
  * **Plan:** Rank critical vs. high-risk tasks.
  * **Tools:** Query JSON database & template engine.
  * **Decide & Act:** Hold critical messages for human approval.
  * **Learn:** Log cycle history.
* **Why it's an Agent, Not a Chatbot (1m):** "Unlike a chatbot that waits for prompts, our agent continuously evaluates state, executes multi-step plans, uses tools, makes decisions, and performs observable actions safely."

---
*Good luck at the symposium tomorrow! You're going to crush it! 🚀*
