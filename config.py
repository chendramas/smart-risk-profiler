PAGE_CONFIG = {
    "page_title": "Smart Risk Profiler",
    "page_icon": "🎯",
    "layout": "centered",
    "initial_sidebar_state": "collapsed"
}

# Color Palette — Dark Mode (default)
COLORS_DARK = {
    "green": "#00FF88",
    "blue": "#00D4FF",
    "black": "#000000",
    "dark": "#0a0a0a",
    "white": "#ffffff",
    "red": "#FF3366",
    "gray": "#888888",
    "dark_red_bg": "#1A0510",
    "bg": "#000000",
    "card": "#0a0a0a",
    "border": "#1a1a1a",
    "text": "#ffffff",
    "text_secondary": "#888888",
    "text_muted": "#555555",
}

# Color Palette — Light Mode
COLORS_LIGHT = {
    "green": "#00CC6A",
    "blue": "#0099CC",
    "black": "#ffffff",
    "dark": "#f5f5f5",
    "white": "#111111",
    "red": "#CC2244",
    "gray": "#666666",
    "dark_red_bg": "#fff5f5",
    "bg": "#ffffff",
    "card": "#f8f8f8",
    "border": "#e0e0e0",
    "text": "#111111",
    "text_secondary": "#666666",
    "text_muted": "#888888",
}

# Default to dark (kept for backward compat in non-UI code)
COLORS = COLORS_DARK


def get_allocations(dark_mode=True):
    """Dynamic ALLOCATIONS — resolves border/bg colors based on current theme."""
    c = COLORS_DARK if dark_mode else COLORS_LIGHT
    return {
        "KONSERVATIF": {
            "border": c["green"],
            "bg": c["dark"],
            "border_key": "green",
            "assets": {"RDPU": 40, "Obligasi Pemerintah": 30, "Emas": 20, "Saham": 10},
            "desc": "Prioritas utama: menjaga modal. Cocok untuk jangka pendek atau yang baru mulai investasi.",
            "tips": [
                "Fokus di instrumen low-risk: deposito, RDPU, obligasi pemerintah",
                "Bangun dana darurat 6-12 bulan pengeluaran dulu",
                "Kalau mau coba saham, mulai dari reksadana indeks",
                "Hindari FOMO — konsistensi > timing"
            ]
        },
        "MODERAT": {
            "border": c["blue"],
            "bg": c["dark"],
            "border_key": "blue",
            "assets": {"RDPU": 20, "Obligasi": 20, "Emas": 15, "Saham": 35, "Crypto": 10},
            "desc": "Balance antara growth & safety. Siap terima fluktuasi moderat untuk return yang lebih tinggi.",
            "tips": [
                "Diversifikasi adalah kunci — jangan taruh semua di satu aset",
                "Rebalance portofolio setiap 3-6 bulan",
                "Saham blue-chip + reksadana campuran bisa jadi core",
                "Crypto max 10-15% — treat as high-risk satellite"
            ]
        },
        "AGRESIF": {
            "border": c["red"],
            "bg": c["dark_red_bg"],
            "border_key": "red",
            "assets": {"RDPU": 5, "Obligasi": 10, "Emas": 10, "Saham": 50, "Crypto": 25},
            "desc": "Fokus maksimalkan return. Siap terima volatilitas tinggi dan potensi loss besar.",
            "tips": [
                "Pastikan dana darurat sudah aman sebelum all-in",
                "Dollar-cost averaging > lump sum di volatile market",
                "Set stop-loss mental — tahu kapan harus cut loss",
                "Jangan invest uang yang lo butuhin dalam 1-2 tahun"
            ]
        }
    }


# Static fallback for non-UI code (scoring.py imports this)
ALLOCATIONS = get_allocations(dark_mode=True)

CHART_COLORS = ["#00FF88", "#00D4FF", "#00CCFF", "#66FFB3", "#99FFCC"]

# Behavioral category labels — single source of truth
BEHAVIORAL_LABELS = {
    "Risk Composure": {"label": "Ketahanan Emosional", "icon": "🧠", "color": "#00FF88"},
    "Risk Preference": {"label": "Preferensi Risiko", "icon": "⚖️", "color": "#00D4FF"},
    "Risk Perception": {"label": "Persepsi Pasar", "icon": "👁️", "color": "#FFB800"},
    "Financial Knowledge": {"label": "Pengetahuan Finansial", "icon": "📚", "color": "#FF3366"},
    "Investing Experience": {"label": "Pengalaman Investasi", "icon": "📈", "color": "#A855F7"},
}

BAR_COLORS = ['#00FF88', '#00E67A', '#00CC7A', '#00D4FF', '#00BBDD', '#00AACC', '#FFB800', '#FF9933', '#FF3366']

# Scoring Weights
MAX_USIA_SCORE = 3
MAX_HORIZON_SCORE = 4
MAX_PENGHASILAN_SCORE = 2

PROFILE_BADGES = {
    "KONSERVATIF": "🛡️",
    "MODERAT": "⚖️",
    "AGRESIF": "🚀",
}

COMPARISON_PERCENTILES = [
    (0.20, "lebih konservatif dari"),
    (0.35, "sedikit lebih konservatif dari"),
    (0.50, "seimbang dengan"),
    (0.65, "sedikit lebih agresif dari"),
    (0.80, "lebih agresif dari"),
    (1.00, "jauh lebih agresif dari"),
]
COMPARISON_PCT = [15, 35, 50, 65, 80, 95]
