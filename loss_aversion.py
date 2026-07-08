# Loss Aversion Measurement — Kahneman & Tversky Prospect Theory
import streamlit as st

# ─────────────────────────────────────────────────────────────
# LOSS AVERSION SCENARIOS
# ─────────────────────────────────────────────────────────────
# Setiap skenario punya 'source' dan 'reason' untuk dokumentasi.
# Lihat docs/05_loss_aversion.md untuk penjelasan lengkap.

LOSS_AVERSION_SCENARIOS = [
    {
        "number": 1,
        "label": "Skenario Gain",
        "text": "Lo ditawarin dua opsi:",
        "options": [
            {"label": "A) Pasti dapet Rp 5.000.000", "type": "safe", "value": 5},
            {"label": "B) 50% dapet Rp 12.000.000, 50% dapet Rp 0", "type": "risky", "expected": 6},
        ],
        "source": "Adapted from Kahneman & Tversky (1979) — Prospect Theory; Grable & Lytton (1999) Risk Tolerance Scale",
        "reason": "Mengukur apakah user lebih pilih 'pasti kecil' atau 'gambling besar'. "
                  "Expected value opsi B (Rp 6jt) > opsi A (Rp 5jt). "
                  "Yang milih A menunjukkan risk aversion di domain gain.",
        "safe_choice": 0,  # index of safe option
    },
    {
        "number": 2,
        "label": "Skenario Loss",
        "text": "Sekarang lo ditawarin dua opsi lain:",
        "options": [
            {"label": "A) Pasti rugi Rp 5.000.000", "type": "safe", "value": -5},
            {"label": "B) 50% rugi Rp 12.000.000, 50% rugi Rp 0", "type": "risky", "expected": -6},
        ],
        "source": "Kahneman & Tversky (1979) — Prospect Theory; Mirror of scenario 1 in loss domain",
        "reason": "Skenario mirror dari #1 tapi di domain loss. "
                  "Kahneman & Tversky menemukan orang cenderung RISK-SEEKING di domain loss "
                  "(lebih pilih gambling daripada pasti rugi). Ini yang bikin orang panic-sell — "
                  "mereka gamble dengan harapan recovery daripada realize loss kecil.",
        "safe_choice": 0,
    },
    {
        "number": 3,
        "label": "Loss Aversion Coefficient",
        "text": "Bayangin lo baru invest Rp 50.000.000. Sekarang nilainya turun jadi Rp 35.000.000 (turun 30%). Apa yang lo lakuin?",
        "options": [
            {"label": "Jual semua — realize rugi Rp 15jt", "type": "behavioral", "coefficient": 3},
            {"label": "Jual sebagian — realize rugi kecil, sisanya di-hold", "type": "behavioral", "coefficient": 2},
            {"label": "Tahan — ga mau realize rugi, berharap recovery", "type": "behavioral", "coefficient": 1.5},
            {"label": "Beli lagi — nambah posisi di harga bawah", "type": "behavioral", "coefficient": 1},
        ],
        "source": "Adapted from Loss Aversion Questionnaire (LAQ) — De Baets (2012); CFA Institute Behavioral Loss Tolerance",
        "reason": "Mengukur loss aversion coefficient secara behavioral (bukan teori). "
                  "Kahneman: rata-rata orang punya coefficient 2-2.5x (loss 2x lebih sakit dari gain). "
                  "Yang langsung jual = coefficient tinggi (sangat loss averse). "
                  "Yang beli lagi = coefficient rendah (bisa detach dari loss).",
        "coefficients": [3, 2, 1.5, 1],
    },
]


def get_loss_aversion_score(responses):
    """Hitung loss aversion coefficient dan score dari jawaban user.
    
    Returns:
        dict: coefficient, score, max, pct, breakdown, risk_level
    """
    total_coefficient = 0
    valid_count = 0
    breakdown = {}

    for i, s in enumerate(LOSS_AVERSION_SCENARIOS):
        answer = responses[i]
        if answer is None:
            continue

        # Find which option was selected
        selected_idx = None
        for j, opt in enumerate(s["options"]):
            if opt["label"] == answer:
                selected_idx = j
                break

        if selected_idx is None:
            continue

        valid_count += 1

        if s["number"] == 1:
            # Gain domain: safe choice = risk averse
            is_safe = (selected_idx == s["safe_choice"])
            coeff = 1.5 if is_safe else 1.0
            total_coefficient += coeff
            breakdown["gain_domain"] = {
                "label": "Domain Gain",
                "answer": answer,
                "is_safe": is_safe,
                "coefficient": coeff,
                "interpretation": "Risk averse di domain gain" if is_safe else "Risk seeking di domain gain",
            }
        elif s["number"] == 2:
            # Loss domain: risky choice = risk seeking in loss (more loss averse)
            is_risky = (selected_idx != s["safe_choice"])
            coeff = 2.5 if is_risky else 1.5
            total_coefficient += coeff
            breakdown["loss_domain"] = {
                "label": "Domain Loss",
                "answer": answer,
                "is_risky": is_risky,
                "coefficient": coeff,
                "interpretation": "Risk seeking di domain loss (loss averse)" if is_risky 
                                 else "Risk averse di domain loss (bisa realize loss)",
            }
        elif s["number"] == 3:
            # Behavioral response to actual loss
            coeff = s["coefficients"][selected_idx]
            total_coefficient += coeff
            breakdown["behavioral"] = {
                "label": "Behavioral Response",
                "answer": answer,
                "coefficient": coeff,
                "interpretation": _get_behavioral_interpretation(coeff),
            }

    avg_coefficient = round(total_coefficient / valid_count, 1) if valid_count > 0 else 2.0

    # Score: lower coefficient = better (less loss averse = more rational)
    # Map coefficient to score (1=best, 3=worst)
    # Invert for scoring: lower coeff = higher score
    score = max(0, round((3 - avg_coefficient) / 2 * 100))

    # Risk level
    if avg_coefficient <= 1.5:
        risk_level = "RASIONAL"
        risk_color = "#00FF88"
        interpretation = "Lo punya hubungan sehat dengan loss — bisa detach secara emosional."
    elif avg_coefficient <= 2.0:
        risk_level = "MODERAT"
        risk_color = "#FFB800"
        interpretation = "Loss aversion lo normal — sesuai rata-rata populasi (Kahneman: 2-2.5x)."
    else:
        risk_level = "TINGGI"
        risk_color = "#FF3366"
        interpretation = "Loss aversion lo tinggi — loss terasa jauh lebih sakit dari gain. " \
                         "Ini prediktor kuat panic selling behavior."

    return {
        "coefficient": avg_coefficient,
        "score": score,
        "max": 100,
        "pct": score,
        "breakdown": breakdown,
        "risk_level": risk_level,
        "risk_color": risk_color,
        "interpretation": interpretation,
    }


def _get_behavioral_interpretation(coeff):
    """Interpretasi behavioral response coefficient."""
    if coeff >= 2.5:
        return "Langsung jual = sangat loss averse. Kemungkinan besar panic-sell saat crash."
    elif coeff >= 2:
        return "Jual sebagian = moderat loss averse. Coba reduce exposure tapi masih hold sebagian."
    elif coeff >= 1.5:
        return "Tahan = loss averse tapi bisa kontrol emosi. Cenderung hold tapi stres."
    else:
        return "Beli lagi = low loss aversion. Bisa detach dari loss dan lihat opportunity."


def render_step_loss_aversion():
    """Render Step 3b: Loss Aversion scenarios."""
    green = "#00FF88"
    red = "#FF3366"

    st.html(f"""
    <div class="section-header">
        <p class="section-eyebrow" style="color: {red};">Prospect Theory</p>
        <h2 class="section-title">Loss Aversion Test</h2>
        <p style="color: #888; font-size: 13px; margin: 0.5rem 0 0;">
            Berdasarkan Kahneman & Tversky Prospect Theory — mengukur berapa x lebih sakit 
            loss dibanding gain. Rata-rata orang: 2-2.5x.
        </p>
    </div>
    """)

    responses = []
    for s in LOSS_AVERSION_SCENARIOS:
        st.html(f"""
        <div style="margin: 1.5rem 0 0.25rem;">
            <p style="font-size: 11px; font-weight: 700; letter-spacing: 3px; 
               text-transform: uppercase; color: {red}; margin: 0;">
                {s['label']}
            </p>
        </div>
        """)

        st.html(f"""
        <div class="scenario-card">
            <p class="scenario-number">Skenario {s['number']}</p>
            <p class="scenario-text">{s['text']}</p>
        </div>
        """)

        option_labels = [opt["label"] for opt in s["options"]]
        answer = st.radio(" ", option_labels, key=f"la_{s['number']}", index=None)
        st.caption(f"📌 {s['source']}")
        responses.append(answer)

    return responses
