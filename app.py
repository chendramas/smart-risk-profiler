import streamlit as st
import time

from config import PAGE_CONFIG, COLORS_DARK, COLORS_LIGHT
from styles import get_css, get_particles_js
from components import header, loading_spinner, progress_steps
from questions import render_step_data_diri, render_step_skenario, SCENARIOS
from financial_health import render_step_financial_health, get_financial_health_score
from loss_aversion import render_step_loss_aversion, get_loss_aversion_score
from overconfidence import detect_overconfidence, get_overconfidence_insight
from scoring import calculate_score, get_profile, get_max_score, get_score_breakdown, get_risk_number, get_risk_number_details
from goals import render_step_goals, calculate_goal_analysis
from config import get_allocations
from results import show_results

# Setup
st.set_page_config(**PAGE_CONFIG)

# Dark mode toggle at TOP of page (visible without sidebar)
col1, col2 = st.columns([6, 1])
with col2:
    dark_mode = st.toggle("🌙", value=True, key="dark_mode_toggle", help="Toggle dark/light mode")

# Set colors based on mode
st.session_state.theme = "dark" if dark_mode else "light"

# Inject CSS based on theme
st.markdown(get_css(dark_mode=dark_mode), unsafe_allow_html=True)

# Inject particles — re-inject when theme changes
prev_theme = st.session_state.get("particles_theme")
if "particles_injected" not in st.session_state or prev_theme != dark_mode:
    st.html(get_particles_js(dark_mode=dark_mode))
    st.session_state.particles_injected = True
    st.session_state.particles_theme = dark_mode

# State wizard
if "step" not in st.session_state:
    st.session_state.step = 1
if "form_data" not in st.session_state:
    st.session_state.form_data = {}
if "result" not in st.session_state:
    st.session_state.result = None

# Hero only on step 1
if st.session_state.step == 1:
    header(dark_mode=dark_mode)

# Progress steps — now 4 steps
progress_steps(st.session_state.step, labels=("Data Diri", "Skenario", "Financial", "Hasil"), dark_mode=dark_mode)

# ---------- STEP 1: Data Diri + Goals ----------
if st.session_state.step == 1:
    nama, usia, penghasilan, horizon, lanjut = render_step_data_diri()
    
    # Goal inputs (below personal data form)
    goals_data = render_step_goals()
    
    if lanjut:
        if not nama or not nama.strip():
            st.warning("Isi nama dulu bro!")
        else:
            st.session_state.form_data.update({
                "nama": nama.strip(),
                "usia": usia,
                "penghasilan": penghasilan,
                "horizon": horizon,
                "goals": goals_data,
            })
            st.session_state.step = 2
            if "balloons_shown" in st.session_state:
                del st.session_state.balloons_shown
            st.rerun()

# ---------- STEP 2: Skenario Behavioral ----------
elif st.session_state.step == 2:
    responses, kembali, lanjut = render_step_skenario()

    if kembali:
        st.session_state.step = 1
        st.rerun()

    if lanjut:
        unanswered = []
        for i, resp in enumerate(responses):
            if resp is None:
                unanswered.append(SCENARIOS[i]["number"])

        if unanswered:
            if len(unanswered) == 1:
                st.warning(f"⚠️ Skenario #{unanswered[0]} belum dijawab bro!")
            else:
                nums = ", ".join([f"#{n}" for n in unanswered])
                st.warning(f"⚠️ Masih ada {len(unanswered)} skenario yang belum dijawab: {nums}")
        else:
            # Save responses and overconfidence detection
            st.session_state.form_data["responses"] = responses
            oc = detect_overconfidence(responses)
            st.session_state.form_data["overconfidence"] = oc
            st.session_state.step = 3
            st.rerun()

# ---------- STEP 3: Financial Health + Loss Aversion ----------
elif st.session_state.step == 3:
    tab_fh, tab_la = st.tabs(["💰 Kesehatan Finansial", "📉 Loss Aversion Test"])

    with tab_fh:
        fh_answers = render_step_financial_health()

    with tab_la:
        la_responses = render_step_loss_aversion()

    # Unified navigation below both tabs
    st.markdown("<hr>", unsafe_allow_html=True)
    col_back, col_analyze = st.columns([1, 3])
    with col_back:
        kembali = st.button("← Kembali", key="step3_back")
    with col_analyze:
        lanjut = st.button("🔍 ANALISIS PROFIL RISIKO", key="step3_analyze", type="primary")

    if kembali:
        st.session_state.step = 2
        st.rerun()

    if lanjut:
        # Check financial health completeness
        fh_incomplete = []
        from financial_health import FINANCIAL_HEALTH_QUESTIONS
        for q in FINANCIAL_HEALTH_QUESTIONS:
            if fh_answers.get(q["key"]) is None:
                fh_incomplete.append(q["label"])

        # Check loss aversion completeness
        la_incomplete = []
        from loss_aversion import LOSS_AVERSION_SCENARIOS
        for i, s in enumerate(LOSS_AVERSION_SCENARIOS):
            if la_responses[i] is None:
                la_incomplete.append(f"Skenario {s['number']}")

        if fh_incomplete:
            st.warning(f"⚠️ Financial health belum lengkap: {', '.join(fh_incomplete)}")
        elif la_incomplete:
            st.warning(f"⚠️ Loss aversion belum dijawab: {', '.join(la_incomplete)}")
        else:
            # All complete — analyze!
            with st.spinner("🔬 Analyzing risk profile..."):
                time.sleep(1.0)

            fd = st.session_state.form_data
            responses = fd["responses"]
            oc_result = fd["overconfidence"]

            # Process financial health
            fh_data = get_financial_health_score(fh_answers)

            # Process loss aversion
            la_result = get_loss_aversion_score(la_responses)

            # Calculate score
            breakdown = get_score_breakdown(fd["usia"], fd["penghasilan"], fd["horizon"], responses)
            score = calculate_score(fd["usia"], fd["penghasilan"], fd["horizon"], responses)

            # Get profile with all factors
            allocations = get_allocations(dark_mode=dark_mode)
            profil_name, profile_data, profile_meta = get_profile(
                score, fd["usia"], fd["penghasilan"], fd["horizon"], responses,
                allocations=allocations,
                fh_answers=fh_answers,
                oc_result=oc_result,
                la_result=la_result,
            )
            max_score = get_max_score()

            # Risk Number (1-99 continuous scale)
            effective_pct = profile_meta.get("effective_pct", 50)
            risk_number = get_risk_number(effective_pct)
            risk_details = get_risk_number_details(risk_number)

            # Goal-Based Risk Need Analysis
            goal_analysis = calculate_goal_analysis(fd.get("goals", {}))

            st.session_state.result = {
                "nama": fd["nama"],
                "score": score,
                "profil_name": profil_name,
                "profile_data": profile_data,
                "max_score": max_score,
                "breakdown": breakdown,
                "responses": responses,
                "profile_meta": profile_meta,
                "fh_data": fh_data,
                "la_result": la_result,
                "oc_result": oc_result,
                "risk_number": risk_number,
                "risk_details": risk_details,
                "goal_analysis": goal_analysis,
            }
            st.session_state.step = 4
            if "balloons_shown" in st.session_state:
                del st.session_state.balloons_shown
            st.rerun()

# ---------- STEP 4: Hasil ----------
elif st.session_state.step == 4:
    r = st.session_state.result
    if r is None:
        st.error("Data hasil tidak ditemukan. Silakan mulai ulang.")
        if st.button("🔄 Mulai Ulang"):
            st.session_state.step = 1
            st.session_state.form_data = {}
            st.session_state.result = None
            st.rerun()
        st.stop()

    show_results(
        r["nama"], r["score"], r["profil_name"], r["profile_data"],
        r["max_score"], r["breakdown"],
        profile_meta=r.get("profile_meta"),
        fh_data=r.get("fh_data"),
        la_result=r.get("la_result"),
        oc_result=r.get("oc_result"),
        risk_number=r.get("risk_number"),
        risk_details=r.get("risk_details"),
        goal_analysis=r.get("goal_analysis"),
        dark_mode=dark_mode,
    )

    st.markdown("<br>", unsafe_allow_html=True)
    if st.button("🔄 Mulai Ulang"):
        st.session_state.step = 1
        st.session_state.form_data = {}
        st.session_state.result = None
        if "balloons_shown" in st.session_state:
            del st.session_state.balloons_shown
        st.rerun()
