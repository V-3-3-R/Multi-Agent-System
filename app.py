import streamlit as st
import time
import threading
from pipeline import run_research_pipeline

# ── Page config ───────────────────────────────────────────────────────────────
st.set_page_config(
    page_title="Research Engine",
    page_icon="🔬",
    layout="wide",
    initial_sidebar_state="collapsed",
)

# ── CSS ───────────────────────────────────────────────────────────────────────
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Playfair+Display:wght@400;700;900&family=IBM+Plex+Mono:wght@300;400;500&family=IBM+Plex+Sans:wght@300;400;500&display=swap');

/* ── Reset & base ── */
html, body, [class*="css"] {
    font-family: 'IBM Plex Sans', sans-serif;
    background: #f5f0e8;
    color: #1a1410;
}
.stApp { background: #f5f0e8; }

/* ── Masthead ── */
.masthead {
    border-top: 4px solid #1a1410;
    border-bottom: 2px solid #1a1410;
    padding: 1.8rem 0 1.4rem;
    margin-bottom: 2.5rem;
    text-align: center;
    position: relative;
}
.masthead::before {
    content: '';
    position: absolute;
    top: 8px;
    left: 0; right: 0;
    border-top: 1px solid #1a1410;
}
.masthead .eyebrow {
    font-family: 'IBM Plex Mono', monospace;
    font-size: 0.72rem;
    letter-spacing: 0.22em;
    text-transform: uppercase;
    color: #8b7355;
    margin-bottom: 0.5rem;
}
.masthead h1 {
    font-family: 'Playfair Display', serif;
    font-weight: 900;
    font-size: 3.8rem;
    line-height: 1;
    letter-spacing: -0.02em;
    margin: 0;
    color: #1a1410;
}
.masthead h1 em {
    font-style: italic;
    color: #c0392b;
}
.masthead .tagline {
    font-family: 'IBM Plex Mono', monospace;
    font-size: 0.7rem;
    letter-spacing: 0.16em;
    text-transform: uppercase;
    color: #8b7355;
    margin-top: 0.6rem;
}

/* ── Input section ── */
.input-label {
    font-family: 'IBM Plex Mono', monospace;
    font-size: 0.72rem;
    letter-spacing: 0.15em;
    text-transform: uppercase;
    color: #8b7355;
    margin-bottom: 0.4rem;
}

.stTextInput > div > div > input {
    background: #fffef9 !important;
    border: 2px solid #1a1410 !important;
    border-radius: 0 !important;
    color: #1a1410 !important;
    font-family: 'IBM Plex Sans', sans-serif !important;
    font-size: 1.05rem !important;
    padding: 0.8rem 1rem !important;
    box-shadow: 4px 4px 0px #1a1410 !important;
    transition: box-shadow 0.15s !important;
}
.stTextInput > div > div > input:focus {
    box-shadow: 6px 6px 0px #c0392b !important;
    border-color: #c0392b !important;
    outline: none !important;
}
.stTextInput > div > div > input::placeholder {
    color: #b8a898 !important;
    font-style: italic;
}

/* ── Run button ── */
.stButton > button {
    background: #1a1410 !important;
    color: #f5f0e8 !important;
    border: 2px solid #1a1410 !important;
    border-radius: 0 !important;
    font-family: 'IBM Plex Mono', monospace !important;
    font-size: 0.78rem !important;
    font-weight: 500 !important;
    letter-spacing: 0.18em !important;
    text-transform: uppercase !important;
    padding: 0.7rem 2rem !important;
    box-shadow: 4px 4px 0px #c0392b !important;
    transition: all 0.15s !important;
    width: 100% !important;
}
.stButton > button:hover {
    background: #c0392b !important;
    border-color: #c0392b !important;
    box-shadow: 6px 6px 0px #1a1410 !important;
    transform: translate(-1px, -1px) !important;
}
.stButton > button:active {
    transform: translate(2px, 2px) !important;
    box-shadow: 2px 2px 0px #c0392b !important;
}

/* ── Pipeline stage tracker ── */
.pipeline-track {
    display: flex;
    align-items: center;
    gap: 0;
    margin: 2rem 0 1.5rem;
    border: 2px solid #1a1410;
    overflow: hidden;
}
.stage-block {
    flex: 1;
    padding: 0.7rem 0.5rem;
    text-align: center;
    border-right: 1px solid #1a1410;
    position: relative;
    transition: background 0.3s;
}
.stage-block:last-child { border-right: none; }
.stage-block .stage-num {
    font-family: 'Playfair Display', serif;
    font-size: 1.5rem;
    font-weight: 900;
    line-height: 1;
    color: #d4c5b0;
}
.stage-block .stage-lbl {
    font-family: 'IBM Plex Mono', monospace;
    font-size: 0.6rem;
    letter-spacing: 0.1em;
    text-transform: uppercase;
    color: #8b7355;
    margin-top: 0.15rem;
}
.stage-block.active {
    background: #1a1410;
}
.stage-block.active .stage-num { color: #c0392b; }
.stage-block.active .stage-lbl { color: #f5f0e8; }
.stage-block.done {
    background: #e8e0d0;
}
.stage-block.done .stage-num { color: #8b7355; }

/* ── Result panels ── */
.result-panel {
    background: #fffef9;
    border: 2px solid #1a1410;
    margin-bottom: 1.5rem;
    box-shadow: 5px 5px 0px #1a1410;
}
.panel-header {
    display: flex;
    align-items: baseline;
    gap: 0.8rem;
    padding: 0.9rem 1.2rem 0.8rem;
    border-bottom: 2px solid #1a1410;
    background: #1a1410;
}
.panel-header .step-tag {
    font-family: 'IBM Plex Mono', monospace;
    font-size: 0.62rem;
    letter-spacing: 0.18em;
    text-transform: uppercase;
    color: #c0392b;
    font-weight: 500;
}
.panel-header h3 {
    font-family: 'Playfair Display', serif;
    font-weight: 700;
    font-size: 1.15rem;
    color: #f5f0e8;
    margin: 0;
}
.panel-body {
    padding: 1.2rem 1.4rem;
    font-family: 'IBM Plex Sans', sans-serif;
    font-size: 0.93rem;
    font-weight: 300;
    line-height: 1.75;
    color: #2c2318;
    white-space: pre-wrap;
    word-break: break-word;
}

/* ── Report panel special ── */
.result-panel.report-panel {
    border-color: #c0392b;
    box-shadow: 5px 5px 0px #c0392b;
}
.result-panel.report-panel .panel-header {
    background: #c0392b;
}
.result-panel.report-panel .panel-header .step-tag {
    color: #f5e8e8;
}

/* ── Critic panel special ── */
.result-panel.critic-panel {
    border-color: #2c7a3a;
    box-shadow: 5px 5px 0px #2c7a3a;
}
.result-panel.critic-panel .panel-header {
    background: #2c7a3a;
}
.result-panel.critic-panel .panel-header .step-tag {
    color: #d4f0da;
}

/* ── Status bar ── */
.status-bar {
    font-family: 'IBM Plex Mono', monospace;
    font-size: 0.72rem;
    letter-spacing: 0.12em;
    color: #8b7355;
    border-top: 1px solid #d4c5b0;
    padding-top: 0.6rem;
    margin-top: 0.8rem;
    display: flex;
    align-items: center;
    gap: 0.5rem;
}
.pulse-dot {
    width: 7px; height: 7px;
    border-radius: 50%;
    background: #c0392b;
    display: inline-block;
    animation: pulse 1s infinite;
}
@keyframes pulse {
    0%, 100% { opacity: 1; transform: scale(1); }
    50% { opacity: 0.4; transform: scale(0.85); }
}

/* ── Section divider ── */
.section-rule {
    border: none;
    border-top: 2px solid #1a1410;
    margin: 2rem 0 1.5rem;
}
.section-rule-light {
    border: none;
    border-top: 1px solid #d4c5b0;
    margin: 1.2rem 0;
}

/* ── Empty state ── */
.empty-state {
    text-align: center;
    padding: 4rem 1rem;
    color: #b8a898;
}
.empty-state .big-num {
    font-family: 'Playfair Display', serif;
    font-size: 6rem;
    font-weight: 900;
    color: #e8e0d0;
    line-height: 1;
}
.empty-state p {
    font-family: 'IBM Plex Mono', monospace;
    font-size: 0.75rem;
    letter-spacing: 0.12em;
    text-transform: uppercase;
    margin-top: 0.8rem;
}

/* ── Streamlit overrides ── */
#MainMenu, footer, header { visibility: hidden; }
.block-container { padding-top: 1.5rem !important; max-width: 1100px !important; }
.stSpinner > div { border-top-color: #c0392b !important; }
[data-testid="stMarkdownContainer"] p { margin: 0; }
</style>
""", unsafe_allow_html=True)

# ── Session state ─────────────────────────────────────────────────────────────
for k, v in {
    "result": None,
    "running": False,
    "current_stage": 0,
    "error": None,
}.items():
    if k not in st.session_state:
        st.session_state[k] = v

# ── Masthead ──────────────────────────────────────────────────────────────────
st.markdown("""
<div class="masthead">
  <div class="eyebrow">Autonomous · Multi-Agent · Intelligence</div>
  <h1>Research <em>Engine</em></h1>
  <div class="tagline">Search · Read · Write · Critique</div>
</div>
""", unsafe_allow_html=True)

# ── Layout: input column + results column ─────────────────────────────────────
left_col, right_col = st.columns([1, 2], gap="large")

with left_col:
    st.markdown('<div class="input-label">Research Topic</div>', unsafe_allow_html=True)
    topic = st.text_input(
        label="",
        placeholder="e.g. Quantum computing in 2025",
        key="topic_input",
        label_visibility="collapsed",
        disabled=st.session_state.running,
    )

    run_clicked = st.button(
        "▶ Run Pipeline",
        disabled=st.session_state.running or not topic.strip(),
        use_container_width=True,
    )

    # ── Pipeline stage tracker ──
    stages = ["Search", "Read", "Write", "Critique"]
    stage_html = '<div class="pipeline-track">'
    for i, s in enumerate(stages):
        cs = st.session_state.current_stage
        if st.session_state.running and i + 1 == cs:
            cls = "active"
        elif (st.session_state.result and not st.session_state.running) or (st.session_state.running and i + 1 < cs):
            cls = "done"
        else:
            cls = ""
        stage_html += f'<div class="stage-block {cls}"><div class="stage-num">{i+1:02d}</div><div class="stage-lbl">{s}</div></div>'
    stage_html += "</div>"
    st.markdown(stage_html, unsafe_allow_html=True)

    # ── Status line ──
    if st.session_state.running:
        labels = ["", "Searching the web…", "Scraping deep content…", "Drafting report…", "Critiquing report…"]
        msg = labels[st.session_state.current_stage] if st.session_state.current_stage <= 4 else "Finishing up…"
        st.markdown(f'<div class="status-bar"><span class="pulse-dot"></span>{msg}</div>', unsafe_allow_html=True)
    elif st.session_state.result:
        st.markdown('<div class="status-bar">✓ &nbsp;Pipeline complete</div>', unsafe_allow_html=True)

    # ── About box ──
    st.markdown("<hr class='section-rule'>", unsafe_allow_html=True)
    st.markdown("""
    <div style="font-family:'IBM Plex Mono',monospace;font-size:0.68rem;letter-spacing:0.1em;color:#8b7355;line-height:2;">
    AGENT 01 — Search Agent<br>
    AGENT 02 — Reader Agent<br>
    CHAIN 03 — Writer Chain<br>
    CHAIN 04 — Critic Chain
    </div>
    """, unsafe_allow_html=True)


# ── Run pipeline ──────────────────────────────────────────────────────────────
if run_clicked and topic.strip():
    st.session_state.running = True
    st.session_state.result = None
    st.session_state.error = None
    st.session_state.current_stage = 1
    st.rerun()

if st.session_state.running and st.session_state.result is None and not st.session_state.error:
    # We need to drive the pipeline; use a placeholder to show live stage updates
    with right_col:
        stage_placeholder = st.empty()

        def run_with_stage_tracking(topic):
            """Monkey-patch pipeline to track stage via session state."""
            from agents import build_search_agent, build_reader_agent, writer_chain, critic_chain

            state = {}

            # Stage 1
            st.session_state.current_stage = 1
            search_agent = build_search_agent()
            search_results = search_agent.invoke({
                "messages": [("user", f"Find recent, reliable and detailed information on the topic: {topic}.")]
            })
            state["search_results"] = search_results['messages'][-1].content

            # Stage 2
            st.session_state.current_stage = 2
            reader_agent = build_reader_agent()
            reader_result = reader_agent.invoke({
                "messages": [("user",
                    f"Based on the following search results about '{topic},"
                    f"pick the most relevant URL and scrape it for deeper content.\n\n"
                    f"Search Results:\n{state['search_results'][:800]}"
                )]
            })
            state['scraped_content'] = reader_result['messages'][-1].content

            # Stage 3
            st.session_state.current_stage = 3
            research_combined = (
                f"Search Results:\n{state['search_results']}\n\n"
                f"Detailed Scraped Content:\n{state['scraped_content']}"
            )
            state["report"] = writer_chain.invoke({
                "topic": topic,
                "research": research_combined
            })

            # Stage 4
            st.session_state.current_stage = 4
            state["Feedback"] = critic_chain.invoke({
                "report": state["report"]
            })

            return state

        try:
            with st.spinner(""):
                result = run_with_stage_tracking(topic)
            st.session_state.result = result
            st.session_state.running = False
            st.session_state.current_stage = 0
        except Exception as e:
            st.session_state.error = str(e)
            st.session_state.running = False
            st.session_state.current_stage = 0

    st.rerun()

# ── Results ───────────────────────────────────────────────────────────────────
with right_col:
    if st.session_state.error:
        st.markdown(f"""
        <div class="result-panel" style="border-color:#c0392b;box-shadow:5px 5px 0 #c0392b;">
          <div class="panel-header" style="background:#c0392b;">
            <span class="step-tag">Error</span>
            <h3>Pipeline Failed</h3>
          </div>
          <div class="panel-body">{st.session_state.error}</div>
        </div>
        """, unsafe_allow_html=True)

    elif st.session_state.result:
        res = st.session_state.result

        # ── Search results ──
        st.markdown(f"""
        <div class="result-panel">
          <div class="panel-header">
            <span class="step-tag">Step 01</span>
            <h3>Search Results</h3>
          </div>
          <div class="panel-body">{res.get('search_results','—')}</div>
        </div>
        """, unsafe_allow_html=True)

        # ── Scraped content ──
        st.markdown(f"""
        <div class="result-panel">
          <div class="panel-header">
            <span class="step-tag">Step 02</span>
            <h3>Deep Scraped Content</h3>
          </div>
          <div class="panel-body">{res.get('scraped_content','—')}</div>
        </div>
        """, unsafe_allow_html=True)

        # ── Report ──
        report_text = res.get('report', '')
        if hasattr(report_text, 'content'):
            report_text = report_text.content
        st.markdown(f"""
        <div class="result-panel report-panel">
          <div class="panel-header">
            <span class="step-tag">Step 03</span>
            <h3>Research Report</h3>
          </div>
          <div class="panel-body">{report_text}</div>
        </div>
        """, unsafe_allow_html=True)

        # ── Feedback ──
        feedback_text = res.get('Feedback', '')
        if hasattr(feedback_text, 'content'):
            feedback_text = feedback_text.content
        st.markdown(f"""
        <div class="result-panel critic-panel">
          <div class="panel-header">
            <span class="step-tag">Step 04</span>
            <h3>Critic's Feedback</h3>
          </div>
          <div class="panel-body">{feedback_text}</div>
        </div>
        """, unsafe_allow_html=True)

        # ── Download ──
        report_md = f"""# Research Report: {st.session_state.get('topic_input','Topic')}

## Search Results
{res.get('search_results','')}

## Scraped Content
{res.get('scraped_content','')}

## Report
{report_text}

## Critic Feedback
{feedback_text}
"""
        st.download_button(
            label="↓ Download Report (.md)",
            data=report_md,
            file_name="research_report.md",
            mime="text/markdown",
            use_container_width=True,
        )

    else:
        # Empty state
        st.markdown("""
        <div class="empty-state">
          <div class="big-num">04</div>
          <p>Agents standing by<br>Enter a topic to begin</p>
        </div>
        """, unsafe_allow_html=True)