# Questions & Form Logic — Scientifically-backed (CFA Institute framework)
import streamlit as st
from components import section_title, scenario_text

# Framework: CFA Institute's 3-Factor IRP Model
# Factor 1: Risk Need (handled by usia + penghasilan + horizon)
# Factor 2: Risk-Taking Ability (handled by usia + penghasilan + horizon)
# Factor 3: Behavioral Loss Tolerance (6 komponen, diukur via skenario)
#
# Urutan options HARUS dari paling konservatif -> paling agresif.
# scoring.py ngambil skor dari posisi index (0 = skor 1, dst).

SCENARIOS = [
    # === RISK COMPOSURE (behavioral reaction) ===
    {
        "number": 1,
        "category": "Risk Composure",
        "text": "Saham lo di IHSG turun",
        "highlight": "20%",
        "suffix": "dalam 1 bulan. Apa yang lo lakuin?",
        "options": ["Jual semua (panic sell)", "Jual sebagian", "Tahan", "Beli lebih banyak"],
        "key": "r1",
        "context": "Mirip kejadian IHSG turun 20% di Maret 2020 (COVID crash)"
    },
    # === RISK COMPOSURE (behavioral reaction - gain scenario) ===
    {
        "number": 2,
        "category": "Risk Composure",
        "text": "Investasi lo naik",
        "highlight": "50%",
        "suffix": "dalam 6 bulan. Apa yang lo lakuin?",
        "options": ["Jual semua, ambil untung", "Jual sebagian", "Tahan", "Tambah investasi"],
        "key": "r2",
        "context": None
    },
    # === RISK COMPOSURE (worst-case scenario) ===
    {
        "number": 3,
        "category": "Risk Composure",
        "text": "Kabar buruk: perusahaan tempat lo invest",
        "highlight": "di-suspend BEI",
        "suffix": ". Saham lo ga bisa dijual. Reaksi lo?",
        "options": ["Panik, cari cara jual di harga berapapun", "Tahan berharap unsuspend", "Diversifikasi ke saham lain", "Pelajari kenapa bisa di-suspend"],
        "key": "r3",
        "context": "Simulasi worst-case: saham di-suspend BEI (seperti beberapa kasus 2023-2024)"
    },
    # === RISK PREFERENCE (willingness) ===
    {
        "number": 4,
        "category": "Risk Preference",
        "text": "Dapet bonus",
        "highlight": "Rp 10 juta",
        "suffix": ", pilih mana?",
        "options": ["Simpen di tabungan/deposito", "Beli emas", "Beli reksadana/saham IDX", "Beli crypto"],
        "key": "r4",
        "context": None
    },
    # === RISK PREFERENCE (guaranteed vs uncertain) ===
    {
        "number": 5,
        "category": "Risk Preference",
        "text": "Pilih mana: pasti naik",
        "highlight": "5% per tahun",
        "suffix": "tanpa volatilitas, ATAU 50/50 bisa naik 20% atau turun 10%?",
        "options": ["Ambil 5% pasti", "Ambil 50/50"],
        "key": "r5",
        "context": "Mengukur risk preference murni: safety vs expected return"
    },
    # === RISK PERCEPTION (subjective view of market) ===
    {
        "number": 6,
        "category": "Risk Perception",
        "text": "Menurut lo, pasar saham Indonesia (IHSG) itu",
        "highlight": "",
        "suffix": "...",
        "options": ["Sangat berisiko, bisa rugi total", "Berisiko tapi bisa diprediksi", "Moderat, naik turun biasa", "Relatif aman kalau jangka panjang"],
        "key": "r6",
        "context": "Persepsi subjektif lo terhadap risiko pasar IHSG"
    },
    # === FINANCIAL KNOWLEDGE (quiz) ===
    {
        "number": 7,
        "category": "Financial Knowledge",
        "text": "Lo punya Rp 100 juta. Opsi mana yang",
        "highlight": "paling terdiversifikasi",
        "suffix": "?",
        "options": ["Semua di 1 saham blue-chip IDX", "Split ke 5 saham IDX berbeda", "Split ke saham + obligasi + emas", "Gak tau"],
        "key": "r7",
        "context": "Quiz pengetahuan dasar diversifikasi (CFA Institute knowledge test)"
    },
    # === INVESTING EXPERIENCE ===
    {
        "number": 8,
        "category": "Investing Experience",
        "text": "Berapa lama lo udah",
        "highlight": "investasi",
        "suffix": "di pasar modal Indonesia?",
        "options": ["Belum pernah", "< 1 tahun", "1-3 tahun", "> 3 tahun (pernah lewat crash IHSG)"],
        "key": "r8",
        "context": "Pengalaman investasi = 'scar tissue' yang bantu lo tetap tenang saat crash"
    },
]


def render_step_data_diri():
    """Step 1: Data pribadi."""
    prev = st.session_state.get("form_data", {})
    with st.form("step1_form"):
        section_title("Data Diri & Preferensi", color="#00FF88", icon="📋")

        col1, col2 = st.columns(2)
        with col1:
            nama = st.text_input("Nama", value=prev.get("nama", ""), placeholder="Contoh: Budi")
            usia = st.slider("Usia", 18, 60, prev.get("usia", 25))
        with col2:
            penghasilan_options = ["< 5 juta", "5 - 15 juta", "> 15 juta"]
            horizon_options = ["< 1 tahun", "1 - 3 tahun", "3 - 5 tahun", "> 5 tahun"]
            penghasilan = st.selectbox(
                "Penghasilan per bulan", penghasilan_options,
                index=penghasilan_options.index(prev["penghasilan"]) if "penghasilan" in prev else 0
            )
            horizon = st.selectbox(
                "Horizon Investasi", horizon_options,
                index=horizon_options.index(prev["horizon"]) if "horizon" in prev else 0
            )

        st.markdown("<hr>", unsafe_allow_html=True)
        lanjut = st.form_submit_button("Lanjut ke Skenario →")

    return nama, usia, penghasilan, horizon, lanjut


def render_step_skenario():
    """Step 2: Skenario behavioral — 8 pertanyaan berdasarkan CFA framework."""
    with st.form("step2_form"):
        section_title("Skenario Risiko", color="#00D4FF", icon="🧠")

        responses = []
        current_category = None
        for s in SCENARIOS:
            # Category separator
            if s["category"] != current_category:
                current_category = s["category"]
                category_labels = {
                    "Risk Composure": ("Ketahanan Emosional", "#00FF88"),
                    "Risk Preference": ("Preferensi Risiko", "#00D4FF"),
                    "Risk Perception": ("Persepsi Pasar", "#FFB800"),
                    "Financial Knowledge": ("Pengetahuan Finansial", "#FF3366"),
                    "Investing Experience": ("Pengalaman Investasi", "#A855F7"),
                }
                label, color = category_labels.get(current_category, ("Skenario", "#00FF88"))
                st.html(f"""
                <div style="margin: 2rem 0 0.5rem; padding: 0.75rem 1rem; background: {color}10; border-left: 3px solid {color}; border-radius: 0 8px 8px 0;">
                    <span style="font-size: 10px; font-weight: 700; letter-spacing: 3px; text-transform: uppercase; color: {color};">
                        {label}
                    </span>
                </div>
                """)

            scenario_text(s["number"], s["text"], s["highlight"] + s["suffix"])
            if s.get("context"):
                st.caption(f"💡 {s['context']}")
            response = st.radio(" ", s["options"], key=s["key"], index=None)
            responses.append(response)

        st.markdown("<hr>", unsafe_allow_html=True)
        col_a, col_b = st.columns([1, 2])
        with col_a:
            kembali = st.form_submit_button("← Kembali")
        with col_b:
            lanjut = st.form_submit_button("Lanjut ke Financial Health →")

    return responses, kembali, lanjut
