from pptx import Presentation

template_path = r'C:\Agentic AI\AGENTIC_ARENA_Participant_Template.pptx'
output_path = r'C:\AgenticAI_Filled_Template.pptx'

prs = Presentation(template_path)

# Slide 1: Title & Details
s1 = prs.slides[0]
for shp in s1.shapes:
    if shp.has_text_frame:
        for p in shp.text_frame.paragraphs:
            txt = p.text.strip()
            if txt == '[Enter Project Name]': p.text = 'Intelligent Task Accountability Agent'
            elif txt == '[Enter Team Name]': p.text = 'Team Synapse'
            elif txt == '[Enter Team ID]': p.text = 'TA2026-01'
            elif txt == '[Fintech / Healthcare Technology / Smart City]': p.text = 'Business & Productivity'
            elif txt == '[Enter Names]': p.text = 'Alice Johnson, Bob Smith'

# Slide 2: Problem Statement
s2 = prs.slides[1]
for shp in s2.shapes:
    if shp.has_text_frame:
        for p in shp.text_frame.paragraphs:
            txt = p.text.strip()
            if txt == '[State the problem in one clear sentence.]':
                p.text = 'Teams waste 2–3 hours weekly chasing overdue tasks and manually compiling progress updates due to lack of visibility.'
            elif txt == '[Context or background]':
                p.text = 'Background: Student project groups and office teams manage multiple pending tasks across different owners without automated tracking.'
            elif txt == '[The gap or pain point]':
                p.text = 'Pain Point: Critical deadlines are missed because team leads have to manually check status and remind members.'
            elif txt == '[Evidence or source, if any]':
                p.text = 'Evidence: Symposium observation and common project management bottlenecks.'
            elif txt == '[Primary users]':
                p.text = 'Primary Users: Team leads, project managers, and student coordinators.'
            elif txt == '[Other affected stakeholders]':
                p.text = 'Other Stakeholders: All team members and external reviewers awaiting deliverables.'
            elif txt == '[Scale, urgency or consequence]':
                p.text = 'Urgency: Missed deadlines delay entire projects; each overdue task takes 30-60 mins of manual coordination.'
            elif txt == '[Who benefits when it is solved]':
                p.text = 'Benefits: Team leads recover 2-3 hours/week; deliverables are completed on time with clear audit trails.'
            elif txt == '[What current solutions miss]':
                p.text = 'Existing Gaps: Static dashboards only show data but do not take action, reason about risk, or plan follow-ups.'
            elif txt == '[Why they fall short]':
                p.text = 'Shortcoming: Conventional chatbots just answer questions and lack autonomous goal-driven workflows.'

# Slide 3: Proposed Solution & Innovation
s3 = prs.slides[2]
for shp in s3.shapes:
    if shp.has_text_frame:
        for p in shp.text_frame.paragraphs:
            txt = p.text.strip()
            if txt == '[Describe your solution in one or two sentences.]':
                p.text = 'An autonomous Task Accountability Agent that continuously monitors task deadlines, scores risk, drafts reminders, and compiles reports with human approval controls.'
            elif txt == '[Step 1: what the system does]':
                p.text = '1. Scans task database to identify overdue and at-risk items.'
            elif txt == '[Step 2: how it closes the gap]':
                p.text = '2. Reasons about risk levels (Critical, High, Low) and plans prioritized follow-up actions.'
            elif txt == '[Outcome for the user]':
                p.text = '3. Executes reminders and generates executive reports with human-in-the-loop approval.'
            elif txt == '[Feature 1]':
                p.text = 'Automated deadline risk scoring (CRITICAL/HIGH/LOW based on hours overdue).'
            elif txt == '[Feature 2]':
                p.text = 'Human-in-the-loop approval gate for critical task notifications.'
            elif txt == '[Feature 3]':
                p.text = 'Executive progress report generation with real-time audit logs.'
            elif txt == '[What makes it different]':
                p.text = 'Differentiator: Follows the official 7-step Agentic AI loop (Goal → Reason → Plan → Tools → Decide → Act → Learn).'
            elif txt == '[Why others cannot match it]':
                p.text = 'Unmatched: Combines autonomous reasoning with strict safety and permission controls.'

# Slide 4: System Architecture & Workflow
s4 = prs.slides[3]
for shp in s4.shapes:
    if shp.has_text_frame:
        for p in shp.text_frame.paragraphs:
            txt = p.text.strip()
            if txt == '[Input / User]': p.text = 'Task Database'
            elif txt == '[What this component does]' and shp.name == 'Node Caption 1': p.text = 'JSON task store (tasks.json)'
            elif txt == '[Frontend / UI]': p.text = 'Streamlit Dashboard'
            elif txt == '[What this component does]' and shp.name == 'Node Caption 2': p.text = 'Interactive web app for live demo'
            elif txt == '[Backend / API]': p.text = 'Python Agent'
            elif txt == '[What this component does]' and shp.name == 'Node Caption 3': p.text = '7-step agentic execution engine'
            elif txt == '[AI/ML & Database]': p.text = 'Risk Engine'
            elif txt == '[What this component does]' and shp.name == 'Node Caption 4': p.text = 'Rule-based scoring & SQLite log'
            elif txt == '[Output / Result]': p.text = 'Reminders & Reports'
            elif txt == '[What this component does]' and shp.name == 'Node Caption 5': p.text = 'Approved actions and audit log'
            elif txt == '[Add items]' and shp.name == 'Stack Body Languages': p.text = 'Python 3.x'
            elif txt == '[Add items]' and shp.name == 'Stack Body Frameworks': p.text = 'Streamlit, python-pptx'
            elif txt == '[Add items]' and shp.name == 'Stack Body APIs': p.text = 'REST / JSON data store'
            elif txt == '[Add items]' and shp.name == 'Stack Body Databases': p.text = 'SQLite / JSON'
            elif txt == '[Add items]' and shp.name == 'Stack Body AI / ML Tools': p.text = 'Rule-based Planner & LLM templates'

# Slide 5: Prototype & Implementation
s5 = prs.slides[4]
for shp in s5.shapes:
    if shp.has_text_frame:
        for p in shp.text_frame.paragraphs:
            txt = p.text.strip()
            if txt == '[Demo flow or how to run it]': p.text = 'Run python agent.py (terminal) or streamlit run demo_app.py (web UI)'
            elif txt == '[What the judges will see]': p.text = 'Live task scan, risk prioritization, reminder drafting, and approval gate.'
            elif txt == '[https://github.com/your-repo]': p.text = 'https://github.com/your-repo/agentic-arena-task-agent'
            elif txt == '[Feature working today]' and shp.name == 'Implemented Body':
                p.text = 'Automated risk scoring | Human approval gate | Executive report generation'
            elif txt == '[Feature planned next]' and shp.name == 'Planned Body':
                p.text = 'Jira/Asana API integration | Email/SMS notifications | Multi-agent coordination'

# Slide 6: Impact & Benefits
s6 = prs.slides[5]
for shp in s6.shapes:
    if shp.has_text_frame:
        for p in shp.text_frame.paragraphs:
            txt = p.text.strip()
            if txt == '[Primary beneficiaries]': p.text = 'Team leads and student project managers'
            elif txt == '[Secondary beneficiaries]': p.text = 'All team members and stakeholders'
            elif txt == '[Benefit for users]': p.text = 'Reclaims 2-3 hours/week per team lead by eliminating manual follow-ups'
            elif txt == '[Benefit for the organisation]': p.text = '30-50% reduction in missed deadlines and improved project visibility'
            elif txt == 'Social: [expected impact]': p.text = 'Social: Reduced stress and friction in team collaborations'
            elif txt == 'Economic: [expected impact]': p.text = 'Economic: Higher productivity and on-time delivery rates'
            elif txt == 'Environmental: [expected impact]': p.text = 'Environmental: Paperless digital workflow'
            elif txt == '[Value]' and shp.name == 'Metric Value 1': p.text = '2-3 Hours'
            elif txt == '[Metric or outcome]' and shp.name == 'Metric Label 1': p.text = 'Saved per team lead weekly'
            elif txt == '[Value]' and shp.name == 'Metric Value 2': p.text = '30-50%'
            elif txt == '[Metric or outcome]' and shp.name == 'Metric Label 2': p.text = 'Reduction in missed deadlines'
            elif txt == '[Value]' and shp.name == 'Metric Value 3': p.text = '100%'
            elif txt == '[Metric or outcome]' and shp.name == 'Metric Label 3': p.text = 'Auditable decision trail'

# Slide 7: Feasibility, Scalability & Future Scope
s7 = prs.slides[6]
for shp in s7.shapes:
    if shp.has_text_frame:
        for p in shp.text_frame.paragraphs:
            txt = p.text.strip()
            if txt == '[Is it buildable today?]': p.text = 'Buildable Today: Fully functional prototype completed with Python and Streamlit.'
            elif txt == '[Skills and tools ready]': p.text = 'Skills Ready: Python, SQLite, Streamlit framework.'
            elif txt == '[Current readiness level]': p.text = 'Readiness Level: TRL 5 (Validated in simulated environment).'
            elif txt == '[Estimated cost]': p.text = 'Cost: Zero licensing cost; open-source stack.'
            elif txt == '[Team, time and tools needed]': p.text = 'Resources: 2 developers, 2 weeks development time.'
            elif txt == '[Key dependencies]': p.text = 'Dependencies: Task data source and human reviewer approval.'
            elif txt == '[Key challenge or risk]': p.text = 'Risk: Over-automation of sensitive communications.'
            elif txt == '[Mitigation approach]': p.text = 'Mitigation: Strict human-in-the-loop approval gate for all critical actions.'
            elif txt == '[Known limitation]': p.text = 'Limitation: Currently tested on sample JSON datasets.'
            elif txt == '[Improvement or scaling step]' and shp.name == 'Phase Text 1': p.text = 'Integrate with real task management APIs (Jira, GitHub Issues).'
            elif txt == '[Improvement or scaling step]' and shp.name == 'Phase Text 2': p.text = 'Deploy department-wide multi-team monitoring dashboard.'
            elif txt == '[Improvement or scaling step]' and shp.name == 'Phase Text 3': p.text = 'Add ML-based deadline prediction analytics.'

# Slide 8: Conclusion & Competitive Advantage
s8 = prs.slides[7]
for shp in s8.shapes:
    if shp.has_text_frame:
        for p in shp.text_frame.paragraphs:
            txt = p.text.strip()
            if txt == '[Problem addressed]': p.text = 'Problem: Team task tracking is manual, leading to missed deadlines and wasted time.'
            elif txt == '[Solution built]': p.text = 'Solution: Intelligent Task Accountability Agent with 7-step agentic workflow.'
            elif txt == '[Result achieved]': p.text = 'Result: Fully working prototype demonstrating reasoning, planning, tool use, and human approval.'
            elif txt == '[Value delivered]': p.text = 'Value: Reclaims 2-3 hours/week, eliminates missed deadlines, ensures full transparency.'
            elif txt == '[Feasibility in practice]': p.text = 'Feasibility: High practicality, zero cost, ready for immediate pilot testing.'
            elif txt == '[Potential to scale]': p.text = 'Scalability: Easily extensible to enterprise task management systems.'
            elif txt == '[One line on what sets your solution apart]': p.text = 'Unlike chatbots, our agent reasons, plans, uses tools, makes decisions, and acts autonomously.'
            elif txt == '[One memorable sentence that sums up your project.]': p.text = 'An autonomous agent that turns scattered team tasks into managed accountability and guaranteed on-time delivery.'

prs.save(output_path)
print('SUCCESS')
