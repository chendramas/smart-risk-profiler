import streamlit as st
import plotly.graph_objects as go
from config import CHART_COLORS, COLORS, PROFILE_BADGES, COMPARISON_PERCENTILES, COMPARISON_PCT, ALLOCATIONS, BEHAVIORAL_LABELS, BAR_COLORS
from components import profile_banner, disclaimer
from styles import get_counter_js
from scoring import get_breakdown_max, get_capacity_tolerance_split, get_insight_text, get_behavioral_breakdown
from overconfidence import get_overconfidence_insight
from card_generator import generate_result_card


def _get_comparison_text(score, max_score):
    """Return (label, percentile) for the score."""
    ratio = score / max_score
    for i, (threshold, label) in enumerate(COMPARISON_PERCENTILES):
        if ratio <= threshold:
            pct = COMPARISON_PCT[i]
            return label, pct
    return COMPARISON_PERCENTILES[-1][1], COMPARISON_PCT[-1]


def _get_similar_profile_insight(profil_name):
    similar = {
        "KONSERVATIF": {
            "text": "Orang dengan profil mirip biasanya: 40% RDPU, 30% Obligasi, 20% Emas, 10% Saham",
            "tip": "Fokus di instrumen yang aman dulu, baru naikin porsi saham pelan-pelan"
        },
        "MODERAT": {
            "text": "Orang dengan profil mirip biasanya: 35% Saham, 20% Obligasi, 20% RDPU, 15% Emas, 10% Crypto",
            "tip": "Diversifikasi adalah kunci — jangan taruh semua di satu aset"
        },
        "AGRESIF": {
            "text": "Orang dengan profil mirip biasanya: 50% Saham, 25% Crypto, 10% Emas, 10% Obligasi, 5% RDPU",
            "tip": "Pastikan dana darurat sudah aman sebelum all-in di aset volatile"
        }
    }
    return similar.get(profil_name, {"text": "", "tip": ""})


def _animated_section_header(eyebrow, title, color="#00D4FF"):
    """Reusable animated section header."""
    st.html(f"""
    <div class="section-appear">
        <p style="font-size: 10px; font-weight: 700; letter-spacing: 5px; text-transform: uppercase; 
           color: {color}; margin: 0 0 0.75rem;">{eyebrow}</p>
        <h2 style="font-family: 'Space Grotesk', sans-serif; font-size: 32px; font-weight: 700; 
            letter-spacing: -0.03em; margin: 0;">{title}</h2>
    </div>
    """)


def show_results(nama, score, profil_name, profile_data, max_score, breakdown,
                 profile_meta=None, fh_data=None, la_result=None, oc_result=None,
                 risk_number=None, risk_details=None, goal_analysis=None,
                 dark_mode=True):
    # Theme colors
    if dark_mode:
        _bg = "#000000"; _card_bg = "#0a0a0a"; _card_bg2 = "#080808"
        _border = "#1a1a1a"; _text = "#ffffff"; _text_sec = "#888888"
        _text_muted = "#666666"; _green = "#00FF88"; _blue = "#00D4FF"
        _plot_bg = "#000000"; _grid = "#111111"; _tick = "#444444"
    else:
        _bg = "#ffffff"; _card_bg = "#f5f5f5"; _card_bg2 = "#f8f8f8"
        _border = "#e0e0e0"; _text = "#111111"; _text_sec = "#666666"
        _text_muted = "#888888"; _green = "#00CC6A"; _blue = "#0099CC"
        _plot_bg = "#ffffff"; _grid = "#e0e0e0"; _tick = "#888888"

    if "balloons_shown" not in st.session_state:
        st.balloons()
        st.session_state.balloons_shown = True

    badge_emoji = PROFILE_BADGES.get(profil_name, "")
    profile_banner(nama, profil_name, profile_data["border"], profile_data["bg"], score, max_score, badge_emoji)

    # ---- RISK NUMBER GAUGE + SCALE BAR (1-99) ----
    if risk_number and risk_details:
        rn_color = risk_details["color"]
        rn_cat = risk_details["category"]
        rn_desc = risk_details["description"]
        rn_alloc = risk_details["allocation"]
        rn_return = risk_details["expected_return"]
        rn_drawdown = risk_details["max_drawdown"]

        needle_angle = ((risk_number - 1) / 98) * 270
        arc_bg = "#1a1a1a" if dark_mode else "#e8e8e8"

        st.html(f"""
        <div style="text-align: center; margin: 1.5rem 0 0.5rem;">
            <p style="font-size: 11px; font-weight: 700; letter-spacing: 5px; text-transform: uppercase;
               color: {_text_sec}; margin: 0 0 1.5rem;">Risk Number</p>

            <!-- Gauge container -->
            <div style="position: relative; width: 260px; height: 145px; margin: 0 auto; overflow: hidden;">
                <!-- Background arc -->
                <div style="position: absolute; top: 0; left: 0; width: 260px; height: 260px; border-radius: 50%;
                     background: conic-gradient(from 210deg, #00FF88 0deg, #00FF88 54deg, #00CC6A 54deg, #00CC6A 108deg, #00D4FF 108deg, #00D4FF 162deg, #FFB800 162deg, #FFB800 216deg, #FF3366 216deg, #FF3366 270deg, transparent 270deg, transparent 360deg); opacity: 0.85;">
                    <!-- Inner circle cutout -->
                    <div style="position: absolute; top: 35px; left: 35px; width: 190px; height: 190px;
                         border-radius: 50%; background: {_bg};"></div>
                </div>

                <!-- Needle -->
                <div style="position: absolute; bottom: 0; left: 50%; width: 3px; height: 95px;
                     background: {rn_color}; transform-origin: bottom center;
                     transform: translateX(-50%) rotate({needle_angle - 135}deg);
                     transition: transform 1.5s cubic-bezier(0.16, 1, 0.3, 1);
                     box-shadow: 0 0 8px {rn_color}40;"></div>
                <!-- Needle center dot -->
                <div style="position: absolute; bottom: -8px; left: 50%; width: 16px; height: 16px;
                     background: {rn_color}; border-radius: 50%; transform: translateX(-50%);
                     box-shadow: 0 0 12px {rn_color}60;">
                    <div style="position: absolute; top: 4px; left: 4px; width: 8px; height: 8px;
                         background: {_bg}; border-radius: 50%;"></div>
                </div>

                <!-- Center number -->
                <div style="position: absolute; bottom: 8px; left: 50%; transform: translateX(-50%);
                     font-family: 'JetBrains Mono', monospace; font-size: 42px; font-weight: 700;
                     color: {rn_color}; text-shadow: 0 0 20px {rn_color}30;
                     line-height: 1;">{risk_number}</div>
            </div>

            <!-- Category -->
            <p style="font-size: 16px; font-weight: 700; color: {rn_color}; margin: 0.75rem 0 0.25rem;
               letter-spacing: 2px;">{rn_cat.upper()}</p>
            <p style="font-size: 13px; color: {_text_sec}; max-width: 420px; margin: 0 auto;">{rn_desc}</p>

            <!-- Zone labels -->
            <div style="display: flex; justify-content: space-between; max-width: 260px; margin: 0.5rem auto 0;">
                <span style="font-size: 9px; color: #00FF88; font-weight: 700;">1</span>
                <span style="font-size: 9px; color: #00CC6A; font-weight: 700;">20</span>
                <span style="font-size: 9px; color: #00D4FF; font-weight: 700;">40</span>
                <span style="font-size: 9px; color: #FFB800; font-weight: 700;">60</span>
                <span style="font-size: 9px; color: #FF3366; font-weight: 700;">80</span>
                <span style="font-size: 9px; color: #FF3366; font-weight: 700;">99</span>
            </div>
        </div>
        """)

        # ---- RISK SCALE BAR (1-99 horizontal) ----
        marker_pos = (risk_number - 1) / 98 * 100
        zones = [
            (0, 20, "Very Conservative", "#00FF88"),
            (20, 40, "Conservative", "#00CC6A"),
            (40, 60, "Moderate", "#00D4FF"),
            (60, 80, "Growth", "#FFB800"),
            (80, 100, "Aggressive", "#FF3366"),
        ]
        zones_html = ""
        for z_start, z_end, z_label, z_color in zones:
            z_width = z_end - z_start
            text_color = "#000" if dark_mode else "#fff"
            zones_html += f'<div style="flex: {z_width}; background: {z_color}; text-align: center; padding: 6px 0; font-size: 9px; font-weight: 700; letter-spacing: 1px; text-transform: uppercase; color: {text_color}; opacity: 0.85;">{z_label}</div>'

        st.html(f"""
        <div style="margin: 0 auto 2rem; max-width: 500px;">
            <!-- Scale bar -->
            <div style="display: flex; border-radius: 8px; overflow: hidden; position: relative; margin: 0 0 8px;">
                {zones_html}
            </div>
            <!-- Marker -->
            <div style="position: relative; height: 24px; margin: 0;">
                <div style="position: absolute; left: {marker_pos}%; transform: translateX(-50%); transition: left 1.5s cubic-bezier(0.16, 1, 0.3, 1);">
                    <div style="width: 3px; height: 16px; background: {rn_color}; margin: 0 auto; border-radius: 2px;"></div>
                    <div style="width: 0; height: 0; border-left: 6px solid transparent; border-right: 6px solid transparent; border-bottom: 8px solid {rn_color}; margin: 0 auto; transform: rotate(180deg);"></div>
                </div>
            </div>
            <!-- Scale numbers -->
            <div style="display: flex; justify-content: space-between; margin: 4px 0 0;">
                <span style="font-family: 'JetBrains Mono', monospace; font-size: 10px; color: {_text_muted};">1</span>
                <span style="font-family: 'JetBrains Mono', monospace; font-size: 10px; color: {_text_muted};">20</span>
                <span style="font-family: 'JetBrains Mono', monospace; font-size: 10px; color: {_text_muted};">40</span>
                <span style="font-family: 'JetBrains Mono', monospace; font-size: 10px; color: {_text_muted};">60</span>
                <span style="font-family: 'JetBrains Mono', monospace; font-size: 10px; color: {_text_muted};">80</span>
                <span style="font-family: 'JetBrains Mono', monospace; font-size: 10px; color: {_text_muted};">99</span>
            </div>
        </div>
        """)

        col_ret, col_dd = st.columns(2)
        with col_ret:
            st.metric("Expected Return", rn_return, help="Estimasi return tahunan berdasarkan profil risiko")
        with col_dd:
            st.metric("Max Drawdown", rn_drawdown, help="Estimasi penurunan maksimal dalam kondisi pasar buruk")

        st.html(f"""
        <p style="font-size: 11px; font-weight: 700; letter-spacing: 3px; text-transform: uppercase; color: {_text_sec}; margin: 1.5rem 0 0.75rem;">Alokasi yang Disarankan</p>
        """)
        alloc_cols = st.columns(len(rn_alloc))
        for i, (asset, pct) in enumerate(rn_alloc.items()):
            with alloc_cols[i]:
                st.metric(label=asset, value=f"{pct}%")

    growth_potential = profile_meta.get("growth_potential", 0) if profile_meta else 0

    st.html(f"""
    <div class="section-appear" style="max-width: 580px; margin: 0 auto 3rem; text-align: center;">
        <p style="color: {_text_sec}; font-size: 15px; line-height: 1.8; margin: 0;">{profile_data["desc"]}</p>
    </div>
    """)

    # ---- COMPARISON ----
    comp_label, comp_pct = _get_comparison_text(score, max_score)
    st.html(f"""
    <div class="comparison-box section-appear">
        <p class="comparison-label">Perbandingan</p>
        <p class="comparison-text">
            Lo {comp_label} <span class="comparison-highlight">{comp_pct}%</span> orang
        </p>
    </div>
    """)

    # ---- SIMILAR PROFILE ----
    similar = _get_similar_profile_insight(profil_name)
    st.html(f"""
    <div class="section-appear" style="padding: 1.5rem; background: {_card_bg2}; border: 1px solid {_border}; border-radius: 12px; margin: 2rem 0;">
        <p style="font-size: 10px; font-weight: 700; letter-spacing: 4px; text-transform: uppercase; color: {_text_sec}; margin: 0 0 1rem;">
            Profil Mirip
        </p>
        <p style="color: {_text}; font-size: 14px; line-height: 1.6; margin: 0 0 0.75rem;">{similar['text']}</p>
        <p style="color: {_text_sec}; font-size: 13px; margin: 0;">&#128161; {similar['tip']}</p>
    </div>
    """)

    # ---- BEHAVIORAL BREAKDOWN ----
    _animated_section_header("CFA Institute Framework", "Behavioral Loss Tolerance", "#00D4FF")

    fd = st.session_state.form_data
    responses = st.session_state.result.get("responses", [])
    behavioral = get_behavioral_breakdown(responses)

    radar_labels = [v["label"] for v in behavioral.values()]
    radar_pcts = [v["pct"] for v in behavioral.values()]

    fig_radar = go.Figure()
    _radar_fill = 'rgba(0, 212, 255, 0.1)' if dark_mode else 'rgba(0, 136, 170, 0.15)'
    _radar_line = '#00D4FF' if dark_mode else '#0088AA'
    fig_radar.add_trace(go.Scatterpolar(
        r=radar_pcts + [radar_pcts[0]],
        theta=radar_labels + [radar_labels[0]],
        fill='toself',
        fillcolor=_radar_fill,
        line=dict(color=_radar_line, width=2),
        marker=dict(size=6, color=_radar_line),
    ))
    fig_radar.update_layout(
        polar=dict(
            radialaxis=dict(visible=True, range=[0, 100], gridcolor=_grid, tickfont=dict(color=_tick, size=10)),
            angularaxis=dict(gridcolor=_grid, tickfont=dict(color=_text_sec, size=11, family='Space Grotesk')),
            bgcolor=_plot_bg
        ),
        showlegend=False,
        paper_bgcolor=_plot_bg,
        plot_bgcolor=_plot_bg,
        margin=dict(t=40, b=40, l=80, r=80),
        height=380,
        font=dict(family='Space Grotesk', color=_text_sec)
    )
    st.plotly_chart(fig_radar, width="stretch")

    tooltip_descriptions = {
        "Risk Composure": "Kemampuan lo tetap tenang & gak panik saat market crash",
        "Risk Preference": "Seberapa besar keinginan lo untuk ambil risiko demi return lebih tinggi",
        "Risk Perception": "Cara lo melihat risiko pasar saham — apakah berisiko atau aman",
        "Financial Knowledge": "Pemahaman lo tentang konsep dasar investasi seperti diversifikasi",
        "Investing Experience": "Pengalaman lo di market — semakin lama, semakin tahan banting",
    }

    for cat, data in behavioral.items():
        tooltip = tooltip_descriptions.get(cat, "")
        if cat in BEHAVIORAL_LABELS:
            data["color"] = BEHAVIORAL_LABELS[cat]["color"]
        st.html(f"""
        <div class="section-appear tip-item" style="display: flex; align-items: center; gap: 1rem; padding: 1rem 1.25rem;" title="{tooltip}">
            <span style="font-size: 20px;">{data['icon']}</span>
            <div style="flex: 1;">
                <div style="display: flex; align-items: center; gap: 0.5rem; margin-bottom: 4px;">
                    <p style="font-size: 13px; font-weight: 600; color: {_text}; margin: 0;">{data['label']}</p>
                    <span style="font-size: 11px; color: {_text_muted}; cursor: help;" title="{tooltip}">ℹ️</span>
                </div>
                <div style="width: 100%; height: 4px; background: {_border}; border-radius: 2px; overflow: hidden;">
                    <div class="progress-animated" style="width: {data['pct']}%; height: 100%; background: {data['color']}; border-radius: 2px;"></div>
                </div>
            </div>
            <span style="font-family: 'JetBrains Mono', monospace; font-size: 16px; font-weight: 700; color: {data['color']};">{data['pct']}%</span>
        </div>
        """)

    # ---- CAPACITY VS TOLERANCE ----
    _animated_section_header("Deep Analysis", "Capacity vs Tolerance", "#00FF88")

    st.html(f"""
    <p style="color: {_text_muted}; font-size: 13px; margin: 0 0 1.5rem 0;">
        <strong style="color: {_text_sec};">Capacity</strong> = kemampuan finansial lo nanggung risiko (objektif)<br>
        <strong style="color: {_text_sec};">Tolerance</strong> = ketahanan psikologis lo terhadap risiko (subjektif)
    </p>
    """)

    ct = get_capacity_tolerance_split(fd["usia"], fd["penghasilan"], fd["horizon"], responses)
    insight = get_insight_text(ct["capacity"]["pct"], ct["tolerance"]["pct"])

    col_cap, col_tol = st.columns(2)
    with col_cap:
        st.metric("Risk Capacity", f"{ct['capacity']['pct']}%",
                   help="Kemampuan finansial lo nanggung risiko — berdasarkan usia, income, horizon")
    with col_tol:
        st.metric("Behavioral Tolerance", f"{ct['tolerance']['pct']}%",
                   help="Toleransi psikologis lo — berdasarkan jawaban skenario")

    st.html(f"""
    <div class="insight-box section-appear" style="border-color: {insight['color']};">
        <p class="insight-title" style="color: {insight['color']};">{insight['title']}</p>
        <p class="insight-text">{insight['text']}</p>
    </div>
    """)

    if growth_potential > 10:
        st.html(f"""
        <div class="section-appear" style="padding: 1rem 1.25rem; background: {_card_bg2}; border: 1px solid {_border}; border-radius: 12px; margin: 1rem 0; display: flex; align-items: center; gap: 1rem;">
            <span style="font-size: 24px;">&#127793;</span>
            <div>
                <p style="font-size: 13px; font-weight: 600; color: {_text}; margin: 0;">Growth Potential</p>
                <p style="font-size: 12px; color: {_text_muted}; margin: 0.25rem 0 0;">Lo punya gap <strong style="color: {_green};">{growth_potential}%</strong> antara capacity dan tolerance. Naikin yang lebih rendah bisa unlock alokasi lebih growth.</p>
            </div>
        </div>
        """)

    # ---- TRAFFIC LIGHT RECONCILIATION ----
    if profile_meta and profile_meta.get("traffic_light"):
        tl = profile_meta["traffic_light"]
        tl_colors = {"GREEN": "#00FF88", "YELLOW": "#FFB800", "RED": "#FF3366"}
        tl_labels = {"GREEN": "SEMUA FAKTOR SEJALAN", "YELLOW": "ADA KETIDAKSEIMBANGAN", "RED": "PERLU REVIEW"}
        tl_descs = {
            "GREEN": "Capacity, tolerance, dan behavioral factors lo sejalan. Profil lo reliable.",
            "YELLOW": "Ada gap antara capacity dan tolerance. Disarankan edukasi sebelum alokasi final.",
            "RED": "Faktor-faktor lo kontradiktif (overconfidence / loss aversion tinggi / gap besar). Profil lo di-adjust ke arah konservatif.",
        }
        tl_color = tl_colors.get(tl, "#888")
        _animated_section_header("CFA IRP", "Traffic Light Reconciliation", tl_color)
        st.html(f"""
        <div class="insight-box section-appear" style="border-color: {tl_color};">
            <p class="insight-title" style="color: {tl_color};">&#x1F6A6; {tl_labels[tl]}</p>
            <p class="insight-text">{tl_descs[tl]}</p>
        </div>
        """)

    # ---- GOAL-BASED RISK NEED ----
    if goal_analysis and goal_analysis.get("goals"):
        ga = goal_analysis
        need_color = {"RENDAH": "#00FF88", "SEDANG": "#FFB800", "TINGGI": "#FF3366"}.get(ga["highest_need"], "#888")
        _animated_section_header("CFA IRP Factor 1", "Goal-Based Risk Need", need_color)

        if ga["red_light"]:
            st.html("""
            <div class="insight-box section-appear" style="border-color: #FF3366;">
                <p class="insight-title" style="color: #FF3366;">&#x1F6A8; Red Light: Risk Need > Capacity</p>
                <p class="insight-text">Salah satu tujuan lo butuh return yang melebihi kemampuan finansial lo.
                Pertimbangkan: perpanjang waktu, kurangi target, atau naikin tabungan bulanan.</p>
            </div>
            """)

        from goals import format_rp
        for key, goal in ga["goals"].items():
            g_color = goal["risk_need_color"]
            st.html(f"""
            <div class="section-appear tip-item" style="display: flex; align-items: center; gap: 1rem; padding: 1rem 1.25rem;">
                <span style="font-size: 24px;">{goal['icon']}</span>
                <div style="flex: 1;">
                    <p style="font-size: 13px; font-weight: 600; color: {_text}; margin: 0;">{goal['label']}</p>
                    <p style="font-size: 12px; color: {_text_muted}; margin: 0.25rem 0;">
                        Target: {format_rp(goal['target'])} dalam {goal['years']} tahun
                    </p>
                    <p style="font-size: 12px; color: {_text_muted}; margin: 0;">
                        Required Return: <strong style="color: {g_color};">{goal['required_return']}%</strong> per tahun
                        ({goal['risk_need_description']})
                    </p>
                </div>
                <span style="font-family: 'JetBrains Mono', monospace; font-size: 14px; font-weight: 700; color: {g_color};">{goal['risk_need_level']}</span>
            </div>
            """)

    # ---- FINANCIAL HEALTH ----
    if fh_data:
        _animated_section_header("Kesehatan Finansial", "Financial Health Check", fh_data["risk_color"])
        st.html(f"""
        <div style="text-align: center; margin-bottom: 1rem;">
            <span style="font-size: 48px;">{"&#128154;" if fh_data['risk_level'] == "SEHAT" else "&#128155;" if fh_data['risk_level'] == "CUKUP" else "&#10084;&#65039;"}</span>
            <p style="font-size: 24px; font-weight: 700; color: {fh_data['risk_color']}; margin: 0.5rem 0 0;">{fh_data['risk_level']}</p>
            <p style="font-size: 13px; color: {_text_sec}; margin: 0;">Skor: {fh_data['score']}/{fh_data['max']} ({fh_data['pct']}%)</p>
        </div>
        """)

        for key, item in fh_data["breakdown"].items():
            bar_pct = round(item["score"] / item["max"] * 100) if item["max"] > 0 else 0
            bar_color = "#00FF88" if bar_pct >= 70 else "#FFB800" if bar_pct >= 40 else "#FF3366"
            st.html(f"""
            <div class="section-appear tip-item" style="display: flex; align-items: center; gap: 1rem; padding: 0.75rem 1.25rem;">
                <div style="flex: 1;">
                    <p style="font-size: 13px; font-weight: 600; color: {_text}; margin: 0 0 4px;">{item['label']}</p>
                    <div style="width: 100%; height: 4px; background: {_border}; border-radius: 2px; overflow: hidden;">
                        <div class="progress-animated" style="width: {bar_pct}%; height: 100%; background: {bar_color}; border-radius: 2px;"></div>
                    </div>
                </div>
                <span style="font-size: 11px; color: {_text_muted};">{item['answer'] or '-'}</span>
            </div>
            """)

    # ---- OVERCONFIDENCE DETECTION ----
    if oc_result and oc_result.get("adjusted"):
        oc_insight = get_overconfidence_insight(oc_result)
        _animated_section_header("Bias Detection", "Overconfidence Check", oc_insight["color"])
        st.html(f"""
        <div class="insight-box section-appear" style="border-color: {oc_insight['color']};">
            <p class="insight-title" style="color: {oc_insight['color']};">{oc_insight['title']}</p>
            <p class="insight-text">{oc_insight['text']}</p>
        </div>
        """)
        for flag in oc_result["flags"]:
            st.html(f"""
            <div class="section-appear tip-item" style="padding: 0.75rem 1.25rem;">
                <span style="color: #FFB800;">&#9888;&#65039;</span>
                <div>
                    <p style="font-size: 13px; font-weight: 600; color: {_text}; margin: 0;">{flag['description']}</p>
                    <p style="font-size: 12px; color: {_text_muted}; margin: 0.25rem 0 0;">{flag['explanation']}</p>
                </div>
            </div>
            """)
    elif oc_result:
        _animated_section_header("Bias Detection", "Overconfidence Check", "#00FF88")
        st.html("""
        <div class="insight-box section-appear" style="border-color: #00FF88;">
            <p class="insight-title" style="color: #00FF88;">&#9989; Konsisten</p>
            <p class="insight-text">Jawaban lo konsisten di semua skenario. Ga ada tanda overconfidence.</p>
        </div>
        """)

    # ---- LOSS AVERSION ----
    if la_result:
        _animated_section_header("Prospect Theory", "Loss Aversion Analysis", la_result["risk_color"])
        col_coeff, col_level = st.columns(2)
        with col_coeff:
            st.metric("Loss Aversion Coefficient", f"{la_result['coefficient']}x",
                       help="Berapa x lebih sakit loss dibanding gain. Rata-rata: 2-2.5x (Kahneman)")
        with col_level:
            st.metric("Risk Level", la_result["risk_level"])
        st.html(f"""
        <div class="insight-box section-appear" style="border-color: {la_result['risk_color']};">
            <p class="insight-title" style="color: {la_result['risk_color']};">&#128202; Interpretasi</p>
            <p class="insight-text">{la_result['interpretation']}</p>
        </div>
        """)
        for key, item in la_result.get("breakdown", {}).items():
            st.html(f"""
            <div class="section-appear tip-item" style="padding: 0.75rem 1.25rem;">
                <div style="flex: 1;">
                    <p style="font-size: 13px; font-weight: 600; color: {_text}; margin: 0;">{item['label']}</p>
                    <p style="font-size: 12px; color: {_text_muted}; margin: 0.25rem 0 0;">{item['interpretation']}</p>
                </div>
            </div>
            """)

    # ---- SCORE BREAKDOWN ----
    _animated_section_header("Rincian Skor", "Score Breakdown", "#00BFFF")

    breakdown_max = get_breakdown_max()
    labels = list(breakdown.keys())
    values = [breakdown[k] for k in labels]
    maxes = [breakdown_max[k] for k in labels]
    pcts = [round(v / m * 100) for v, m in zip(values, maxes)]

    bar_colors = BAR_COLORS
    
    fig_breakdown = go.Figure()
    
    for i in reversed(range(len(labels))):
        fig_breakdown.add_trace(go.Bar(
            y=[labels[i]],
            x=[pcts[i]],
            orientation='h',
            marker=dict(
                color=bar_colors[i % len(bar_colors)],
                line=dict(width=0),
            ),
            text=[f"{values[i]}/{maxes[i]}"],
            textposition='outside',
            textfont=dict(color=_text_sec, family='JetBrains Mono', size=13),
            hovertemplate=f'<b>{labels[i]}</b>: {values[i]}/{maxes[i]} ({pcts[i]}%)<extra></extra>',
            showlegend=False,
        ))
    
    fig_breakdown.update_layout(
        xaxis=dict(range=[0, 130], showgrid=False, showticklabels=False),
        yaxis=dict(color=_text, autorange="reversed", tickfont=dict(size=13)),
        paper_bgcolor=_plot_bg,
        plot_bgcolor=_plot_bg,
        margin=dict(t=10, b=30, l=10, r=80),
        height=max(300, len(labels) * 45),
        font=dict(family='Space Grotesk', color=_text_sec),
        bargap=0.3,
    )
    st.plotly_chart(fig_breakdown, width="stretch")

    # ---- ALOKASI ----
    _animated_section_header("Rekomendasi", "Alokasi Aset", "#00FF88")

    alokasi = profile_data["assets"]
    asset_labels = list(alokasi.keys())
    asset_values = list(alokasi.values())

    fig = go.Figure(data=[go.Pie(
        labels=asset_labels, values=asset_values, hole=0.48,
        marker=dict(
            colors=['#00FF88', '#00D4FF', '#00CCFF', '#66FFB3', '#99FFCC'][:len(asset_labels)],
            line=dict(color='#000', width=3)
        ),
        textinfo='label+percent',
        textfont=dict(family='Space Grotesk', size=13, color='#888'),
        insidetextfont=dict(family='JetBrains Mono', size=12, color='#000'),
        hovertemplate='<b>%{label}</b><br>%{value}%<extra></extra>',
        pull=[0.03] * len(asset_labels)
    )])
    fig.update_layout(
        showlegend=False,
        paper_bgcolor=_plot_bg,
        plot_bgcolor=_plot_bg,
        margin=dict(t=20, b=20, l=20, r=20),
        height=420,
        font=dict(family='Space Grotesk', color=_text_sec)
    )
    fig.add_annotation(
        text=f'<b>{profil_name[:3]}</b>',
        x=0.5, y=0.5,
        font=dict(family='JetBrains Mono', size=20, color=profile_data["border"]),
        showarrow=False
    )
    if not dark_mode:
        fig.update_traces(textfont=dict(color='#333333'))
    st.plotly_chart(fig, width="stretch")

    cols = st.columns(len(alokasi))
    for i, (asset, pct_val) in enumerate(alokasi.items()):
        with cols[i]:
            st.metric(label=asset, value=f"{pct_val}%")

    # ---- TIPS ----
    _animated_section_header("Strategi", f"Tips untuk {profil_name}", "#00FF88")

    tips = profile_data.get("tips", [])
    for i, tip in enumerate(tips):
        st.html(f"""
        <div class="tip-item section-appear">
            <span class="tip-number" style="color: {profile_data['border']};">{i+1}.</span>
            <span style="color: {_text};">{tip}</span>
        </div>
        """)

    # ---- DOWNLOAD & SHARE ----
    _animated_section_header("Export & Share", "Download & Bagikan", "#00D4FF")

    col_dl1, col_dl2, col_dl3 = st.columns(3)

    summary_lines = [
        "SMART RISK PROFILER — Hasil Analisis (CFA Framework)",
        "=" * 50,
        f"Nama            : {nama}",
        f"Skor            : {int(round(score))}/{max_score}",
        f"Profil Risiko   : {profil_name}",
        "",
        "Risk Capacity vs Behavioral Tolerance:",
        f"  Capacity       : {ct['capacity']['pct']}%",
        f"  Tolerance      : {ct['tolerance']['pct']}%",
        "",
        "Behavioral Loss Tolerance Breakdown:",
    ]
    for cat, data in behavioral.items():
        summary_lines.append(f"  - {data['label']}: {data['pct']}%")
    summary_lines += ["", "Rincian Skor:"]
    for k, v in breakdown.items():
        summary_lines.append(f"  - {k}: {int(round(v))}/{breakdown_max[k]}")
    summary_lines += ["", "Rekomendasi Alokasi Aset:"]
    for asset, pct_val in alokasi.items():
        summary_lines.append(f"  - {asset}: {pct_val}%")
    summary_lines += ["", "Catatan: Ini simulasi edukasi, bukan saran investasi.",
                       "Framework: CFA Institute Investment Risk Profile (IRP)"]
    summary_text = "\n".join(summary_lines)

    with col_dl1:
        st.download_button("&#11015;&#65039; Data (.txt)", data=summary_text,
                           file_name=f"risk_profile_{nama.replace(' ', '_')}.txt",
                           mime="text/plain", width="stretch")

    with col_dl2:
        card_buf = generate_result_card(nama, profil_name, badge_emoji, int(round(score)), max_score, alokasi, ct)
        st.download_button("&#128444;&#65039; Kartu (.png)", data=card_buf,
                           file_name=f"risk_profile_{nama.replace(' ', '_')}.png",
                           mime="image/png", width="stretch")

    with col_dl3:
        share_caption = f"""&#127919; Smart Risk Profiler — Hasil Analisis

&#128100; {nama}
&#128202; Profil: {profil_name} {badge_emoji}
&#128175; Skor: {int(round(score))}/{max_score}

&#128300; Behavioral Breakdown:
"""
        for cat, data in behavioral.items():
            share_caption += f"  {data['icon']} {data['label']}: {data['pct']}%\n"
        
        share_caption += f"""
&#128200; Rekomendasi Alokasi:
"""
        for asset, pct_val in alokasi.items():
            share_caption += f"  • {asset}: {pct_val}%\n"
        
        share_caption += f"""
&#9888;&#65039; Simulasi edukasi, bukan saran investasi.
&#129516; Framework: CFA Institute IRP

#SmartRiskProfiler #Investasi #FinancialPlanning"""

        st.download_button("&#128203; Caption (.txt)", data=share_caption,
                           file_name=f"share_caption_{nama.replace(' ', '_')}.txt",
                           mime="text/plain", width="stretch")

    disclaimer(dark_mode=dark_mode)
