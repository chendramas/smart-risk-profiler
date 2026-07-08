import streamlit as st
from components import section_title

FINANCIAL_HEALTH_QUESTIONS = [
    {
        "key": "dana_darurat",
        "label": "Dana Darurat",
        "question": "Berapa lama dana darurat lo bisa nutupin pengeluaran bulanan tanpa income?",
        "type": "select",
        "options": [
            "< 1 bulan (ga punya dana darurat)",
            "1 - 3 bulan",
            "3 - 6 bulan",
            "6 - 12 bulan",
            "> 12 bulan"
        ],
        "scores": [0, 1, 2, 3, 4],
        "source": "Hasanah, Wiryono & Koesrindartoto (2024) — ITB; CFA Institute IRP Factor 2",
    },
    {
        "key": "rasio_utang",
        "label": "Rasio Utang",
        "question": "Berapa persen penghasilan bulanan lo yang buat cicilan utang (KPR, KTA, kartu kredit, dll)?",
        "type": "select",
        "options": [
            "Ga ada utang",
            "< 20% penghasilan",
            "20 - 40% penghasilan",
            "40 - 60% penghasilan",
            "> 60% penghasilan"
        ],
        "scores": [4, 3, 2, 1, 0],
        "source": "CFA Institute IRP Factor 2 (Liquidity Need); Standar robo-advisor (Wealthfront, Betterment)",
    },
    {
        "key": "tanggungan",
        "label": "Jumlah Tanggungan",
        "question": "Berapa orang yang secara finansial bergantung sama lo? (anak, orang tua, pasangan, dll)",
        "type": "select",
        "options": [
            "0 (cuma diri sendiri)",
            "1 orang",
            "2 orang",
            "3 - 4 orang",
            "5+ orang"
        ],
        "scores": [4, 3, 2, 1, 0],
        "source": "Hasanah et al. (2024) — ITB; Private bank suitability assessment (UBS, JPM PB)",
    },
    {
        "key": "net_worth",
        "label": "Total Kekayaan Bersih",
        "question": "Berapa total kekayaan bersih lo? (total aset - total utang)",
        "type": "select",
        "options": [
            "< 0 (utang lebih besar dari aset)",
            "0 - 50 juta",
            "50 - 200 juta",
            "200 juta - 1 miliar",
            "> 1 miliar"
        ],
        "scores": [0, 1, 2, 3, 4],
        "source": "Grable & Chatterjee (2026) — Journal of Financial Planning 39(1); SCF 2016",
    },
    {
        "key": "kepemilikan_rumah",
        "label": "Kepemilikan Rumah",
        "question": "Status kepemilikan tempat tinggal lo?",
        "type": "select",
        "options": [
            "Ngontrak / numpang",
            "KPR (masih nyicil)",
            "Rumah sendiri (lunas)",
            "Punya properti > 1"
        ],
        "scores": [1, 1, 3, 4],
        "source": "Hasanah et al. (2024) — ITB; Common in robo-advisor questionnaires",
    },
]


def get_financial_health_score(answers):
    """Calculate financial health score from user answers.
    
    Returns:
        dict: score, max, pct, breakdown per question, risk_level
    """
    total_score = 0
    max_score = 0
    breakdown = {}

    for q in FINANCIAL_HEALTH_QUESTIONS:
        answer = answers.get(q["key"])
        if answer is None:
            score = 0
        else:
            idx = q["options"].index(answer)
            score = q["scores"][idx]
        
        total_score += score
        max_score += max(q["scores"])
        breakdown[q["key"]] = {
            "label": q["label"],
            "score": score,
            "max": max(q["scores"]),
            "answer": answer,
        }

    pct = round(total_score / max_score * 100) if max_score > 0 else 0

    if pct >= 70:
        risk_level = "SEHAT"
        risk_color = "#00FF88"
    elif pct >= 40:
        risk_level = "CUKUP"
        risk_color = "#FFB800"
    else:
        risk_level = "RAPUH"
        risk_color = "#FF3366"

    return {
        "score": total_score,
        "max": max_score,
        "pct": pct,
        "breakdown": breakdown,
        "risk_level": risk_level,
        "risk_color": risk_color,
    }


def render_step_financial_health():
    """Render Step 3a: Financial Health questions."""
    green = "#00FF88"

    st.html(f"""
    <div class="section-header">
        <p class="section-eyebrow" style="color: {green};">Kesehatan Finansial</p>
        <h2 class="section-title">Financial Health Check</h2>
        <p style="color: #888; font-size: 13px; margin: 0.5rem 0 0;">
            Pertanyaan ini membantu mengukur kemampuan finansial lo nanggung risiko secara objektif.
        </p>
    </div>
    """)

    answers = {}
    for q in FINANCIAL_HEALTH_QUESTIONS:
        st.html(f"""
        <div style="margin: 1.5rem 0 0.25rem;">
            <p style="font-size: 11px; font-weight: 700; letter-spacing: 3px; 
               text-transform: uppercase; color: {green}; margin: 0;">
                {q['label']}
            </p>
        </div>
        """)
        answer = st.radio(
            q["question"],
            q["options"],
            key=f"fh_{q['key']}",
            index=None,
        )
        st.caption(f"📌 {q['source']}")
        answers[q["key"]] = answer

    return answers
