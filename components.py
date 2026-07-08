# Reusable UI Components — Dual theme support
import html
import streamlit as st
from config import COLORS_DARK, COLORS_LIGHT

def header(dark_mode=True):
    c = COLORS_DARK if dark_mode else COLORS_LIGHT
    text = "#ffffff" if dark_mode else "#111111"
    text_secondary = "#888888" if dark_mode else "#666666"
    green = "#00FF88" if dark_mode else "#00CC6A"
    blue = "#00D4FF" if dark_mode else "#0099CC"
    
    st.html(f"""
    <div class="hero-wrapper">
        <div class="hero-content">
            <p class="hero-eyebrow">Financial Intelligence</p>
            <h1 class="hero-title">
                <span class="green">Smart</span> <span class="white">Risk</span><br>
                <span class="blue">Profiler</span>
            </h1>
            <div class="hero-divider"></div>
            <p class="hero-subtitle">
                Profil risiko & rekomendasi alokasi aset multi-instrument
            </p>
        </div>
    </div>
    """)

def progress_steps(current_step, labels=("Data Diri", "Skenario", "Hasil"), dark_mode=True):
    steps_html = ""
    for i, label in enumerate(labels, start=1):
        active = i <= current_step
        step_class = "active" if active else ""
        steps_html += f"""
        <div class="progress-node {step_class}">
            <div class="node-circle">{i}</div>
            <div class="node-label">{label}</div>
        </div>
        """
    
    st.html(f"""
    <div class="progress-track">
        {steps_html}
    </div>
    """)

def section_title(title, color=None, icon="📋", dark_mode=True):
    if color is None:
        color = "#00FF88" if dark_mode else "#00CC6A"
    label_map = {"📋": "Informasi Personal", "🧠": "Evaluasi Risiko"}
    label = label_map.get(icon, "Langkah")
    
    st.html(f"""
    <div class="section-header">
        <p class="section-eyebrow" style="color: {color};">{label}</p>
        <h2 class="section-title">{title}</h2>
    </div>
    """)

def scenario_text(number, text, highlight, dark_mode=True):
    green = "#00FF88" if dark_mode else "#00CC6A"
    text_color = "#ffffff" if dark_mode else "#111111"
    
    st.html(f"""
    <div class="scenario-card">
        <p class="scenario-number">Skenario {number}</p>
        <p class="scenario-text">
            {text} <span class="scenario-highlight">{highlight}</span>
        </p>
    </div>
    """)

def loading_spinner():
    st.html("""
    <div style="text-align: center; padding: 8rem 2rem;">
        <div class="spinner"></div>
        <p style="color: #888; margin-top: 2.5rem; font-size: 11px; font-weight: 700; letter-spacing: 5px; text-transform: uppercase;">
            Analyzing risk profile
        </p>
    </div>
    """)

def profile_banner(nama, profil, warna_border, warna_bg, score, max_score, badge_emoji="", dark_mode=True):
    nama_aman = html.escape(nama)
    progress_pct = (score / max_score) * 100
    text = "#ffffff" if dark_mode else "#111111"
    text_secondary = "#888888" if dark_mode else "#666666"
    border = "#1a1a1a" if dark_mode else "#e0e0e0"

    st.html(f"""
    <div class="profile-hero">
        <p style="font-size: 14px; font-weight: 300; color: {text_secondary}; margin: 0 0 0.5rem;">
            Halo, <span style="color: {text};">{nama_aman}</span>
        </p>
        <div class="profile-badge">{badge_emoji}</div>
        <p style="font-size: 11px; font-weight: 700; letter-spacing: 5px; text-transform: uppercase; color: {text_secondary}; margin: 0 0 0.75rem;">
            Profil Risiko Anda
        </p>
        <h2 class="profile-type" style="color: {warna_border};">{profil}</h2>
        <div class="score-display">
            <span class="score-current">{int(round(score))}</span>
            <span class="score-max">/{int(round(max_score))}</span>
        </div>
        <div class="progress-bar-track">
            <div class="progress-bar-fill" style="width: {progress_pct}%;"></div>
        </div>
    </div>
    """)

def disclaimer(dark_mode=True):
    if dark_mode:
        _bg = "#050505"; _border = "#333"; _text = "#666"; _text_bold = "#888"
    else:
        _bg = "#f8f8f8"; _border = "#ddd"; _text = "#555"; _text_bold = "#333"
    st.html(f"""
    <div style="margin: 3rem 0 1rem; padding: 1.25rem; border: 1px solid {_border}; border-radius: 12px; background: {_bg};">
        <p style="font-size: 10px; font-weight: 700; letter-spacing: 4px; text-transform: uppercase; color: #FFB800; margin: 0 0 0.75rem;">&#9888;&#65039; Disclaimer</p>
        <p style="font-size: 13px; color: {_text}; line-height: 1.7; margin: 0;">
            Ini hanya <strong style="color: {_text_bold};">simulasi edukasi</strong>, bukan saran investasi.
            Profil risiko ditentukan oleh faktor terbatas dari 'kemampuan menanggung risiko'
            (usia, penghasilan, horizon) dan 'toleransi behavioral' (reaksi skenario).
            Menggunakan pendekatan <strong style="color: {_text_bold};">CFA Institute IRP</strong>: profil mengikuti batas terendah
            antara capacity dan tolerance. Lakukan riset sendiri sebelum investasi.
        </p>
    </div>
    """)
