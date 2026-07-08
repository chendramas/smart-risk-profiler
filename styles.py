# CSS & Animations — Final version with proper dual theme
from config import COLORS_DARK, COLORS_LIGHT

def get_css(dark_mode=True):
    if dark_mode:
        bg = "#000000"
        card_bg = "#0a0a0a"
        border = "#1a1a1a"
        text = "#ffffff"
        text_sec = "#999999"
        text_muted = "#666666"
        input_bg = "#0a0a0a"
        hover_bg = "#111111"
        green = "#00FF88"
        blue = "#00D4FF"
        btn_text = "#000000"
        shadow = "rgba(0, 255, 136, 0.3)"
    else:
        bg = "#ffffff"
        card_bg = "#f5f5f5"
        border = "#dddddd"
        text = "#111111"
        text_sec = "#444444"
        text_muted = "#777777"
        input_bg = "#ffffff"
        hover_bg = "#eeeeee"
        green = "#00AA55"
        blue = "#0088AA"
        btn_text = "#ffffff"
        shadow = "rgba(0, 170, 85, 0.2)"

    return """
<style>
@import url('https://fonts.googleapis.com/css2?family=Space+Grotesk:wght@300;400;500;600;700&family=JetBrains+Mono:wght@400;500;600;700&display=swap');

* { box-sizing: border-box; }

/* === UNIVERSAL TEXT COLOR FIX === */
/* This catches ALL text elements in both modes */
.stApp,
.stApp *,
.stApp input,
.stApp textarea,
.stApp select,
.stApp label,
.stApp p,
.stApp span,
.stApp div,
.stApp li,
.stApp h1, .stApp h2, .stApp h3, .stApp h4, .stApp h5, .stApp h6 {
    color: """ + text + """ !important;
}

/* Specific overrides for backgrounds */
.stApp { background: """ + bg + """ !important; }
.main .block-container { background: """ + bg + """ !important; padding-top: 0 !important; max-width: 880px; }

#MainMenu, footer, header { visibility: hidden; }

/* === INPUT FIELDS === */
.stTextInput > div > div,
.stSelectbox > div > div {
    background: """ + input_bg + """ !important;
    border: 1px solid """ + border + """ !important;
    border-radius: 10px !important;
}

.stTextInput > div > div:focus-within,
.stSelectbox > div > div:focus-within {
    border-color: """ + green + """ !important;
    box-shadow: 0 0 0 3px """ + green + """20 !important;
}

/* Force input text color */
input[type="text"],
textarea,
select,
[contenteditable],
[data-baseweb="input"] input,
[data-baseweb="textarea"] textarea,
[data-baseweb="select"] span {
    color: """ + text + """ !important;
    -webkit-text-fill-color: """ + text + """ !important;
    caret-color: """ + text + """ !important;
}

input::placeholder,
textarea::placeholder {
    color: """ + text_muted + """ !important;
    -webkit-text-fill-color: """ + text_muted + """ !important;
}

/* === DROPDOWN MENU === */
[role="listbox"],
[role="option"],
[role="listbox"] li,
[role="option"] span,
[data-baseweb="popover"],
[data-baseweb="menu"],
[data-baseweb="menu"] li,
[data-baseweb="menu"] li span {
    background: """ + input_bg + """ !important;
    color: """ + text + """ !important;
    -webkit-text-fill-color: """ + text + """ !important;
}

[role="option"]:hover,
[role="option"][aria-selected="true"],
[data-baseweb="menu"] li:hover {
    background: """ + hover_bg + """ !important;
}

/* === RADIO BUTTONS === */
.stRadio > div {
    background: """ + card_bg + """ !important;
    border: 1px solid """ + border + """ !important;
    border-radius: 12px !important;
    padding: 14px !important;
    transition: all 0.3s ease !important;
}

.stRadio > div:hover {
    border-color: """ + green + """ !important;
    background: """ + hover_bg + """ !important;
}

.stRadio label {
    font-family: 'Space Grotesk', sans-serif !important;
    font-size: 14px !important;
    color: """ + text + """ !important;
    -webkit-text-fill-color: """ + text + """ !important;
}

/* Radio circle and text */
.stRadio label span,
.stRadio label p,
.stRadio [data-baseweb="radio"] span,
.stRadio [data-baseweb="radio"] p {
    color: """ + text + """ !important;
    -webkit-text-fill-color: """ + text + """ !important;
}

/* === SLIDER === */
.stSlider label {
    color: """ + text_sec + """ !important;
    font-size: 12px !important;
    font-weight: 600 !important;
}

.stSlider span,
.stSlider output {
    color: """ + text + """ !important;
    -webkit-text-fill-color: """ + text + """ !important;
}

.stSlider > div > div > div {
    background: linear-gradient(90deg, """ + green + """, """ + blue + """) !important;
}

/* === BUTTONS === */
.stButton > button,
[data-testid="stFormSubmitButton"] button {
    background: linear-gradient(135deg, """ + green + """, """ + blue + """) !important;
    color: """ + btn_text + """ !important;
    border: none !important;
    border-radius: 10px !important;
    font-family: 'Space Grotesk', sans-serif !important;
    font-weight: 700 !important;
    font-size: 14px !important;
    letter-spacing: 2px !important;
    text-transform: uppercase !important;
    padding: 16px 40px !important;
    transition: all 0.3s ease !important;
    box-shadow: 0 4px 15px """ + shadow + """ !important;
}

.stButton > button:hover,
[data-testid="stFormSubmitButton"] button:hover {
    transform: translateY(-2px);
    box-shadow: 0 8px 30px """ + shadow + """ !important;
}

/* === CAPTION & HELPERS === */
.stCaption { color: """ + text_muted + """ !important; }

/* === HERO === */
.hero-wrapper {
    position: relative;
    min-height: 80vh;
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
    text-align: center;
    padding: 0 2rem;
}

.hero-eyebrow {
    font-size: 12px;
    font-weight: 700;
    letter-spacing: 8px;
    text-transform: uppercase;
    background: linear-gradient(90deg, """ + green + """, """ + blue + """);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    margin-bottom: 2rem;
    opacity: 0;
    animation: fadeInUp 0.8s ease-out 0.2s forwards;
}

.hero-title {
    font-size: clamp(48px, 8vw, 96px);
    font-weight: 700;
    line-height: 0.95;
    letter-spacing: -0.04em;
    margin: 0 0 2rem;
    opacity: 0;
    animation: fadeInUp 0.8s ease-out 0.4s forwards;
}

.hero-title .green {
    background: linear-gradient(135deg, """ + green + """, """ + blue + """);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
}

.hero-title .white { color: """ + text + """; }

.hero-title .blue {
    background: linear-gradient(135deg, """ + blue + """, #0088CC);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
}

.hero-subtitle {
    font-size: 16px;
    font-weight: 300;
    color: """ + text_sec + """;
    max-width: 480px;
    margin: 0 auto 2rem;
    opacity: 0;
    animation: fadeInUp 0.8s ease-out 0.6s forwards;
}

.hero-divider {
    width: 60px;
    height: 2px;
    background: linear-gradient(90deg, """ + green + """, """ + blue + """);
    margin: 0 auto 2rem;
    opacity: 0;
    animation: fadeInUp 0.8s ease-out 0.8s forwards;
}

/* === PROGRESS === */
.progress-track { display: flex; justify-content: center; align-items: flex-start; padding: 2rem 0; margin-bottom: 2rem; gap: 0; }
.progress-node { display: flex; flex-direction: column; align-items: center; width: 100px; position: relative; }
.progress-node:not(:last-child)::after {
    content: '';
    position: absolute;
    top: 16px;
    left: calc(50% + 20px);
    width: calc(100% - 40px);
    height: 1px;
    background: #1a1a1a;
}
.progress-node.active:not(:last-child)::after {
    background: linear-gradient(90deg, #00FF88, #00D4FF);
}

.node-circle {
    width: 32px; height: 32px; border-radius: 50%;
    display: flex; align-items: center; justify-content: center;
    font-size: 13px; font-weight: 600; margin-bottom: 8px;
    border: 1px solid """ + border + """;
    color: """ + text_muted + """;
    transition: all 0.3s ease;
}

.progress-node.active .node-circle {
    background: """ + green + """; border-color: """ + green + """;
    color: """ + btn_text + """;
    box-shadow: 0 0 20px """ + shadow + """;
}

.node-label { font-size: 11px; font-weight: 600; letter-spacing: 2px; text-transform: uppercase; color: """ + text_muted + """; }
.progress-node.active .node-label { color: """ + text_sec + """; }

/* === SCENARIOS === */
.scenario-card {
    background: """ + card_bg + """;
    border: 1px solid """ + border + """;
    border-radius: 12px;
    padding: 1.5rem;
    margin: 1rem 0;
    transition: all 0.3s ease;
}

.scenario-card:hover { border-color: """ + green + """; transform: translateY(-2px); }

.scenario-number { font-size: 11px; font-weight: 700; letter-spacing: 3px; text-transform: uppercase; color: """ + green + """; margin-bottom: 0.75rem; }
.scenario-text { font-size: 16px; font-weight: 500; color: """ + text + """; line-height: 1.5; }
.scenario-highlight { color: """ + green + """; font-weight: 700; }

/* === PROFILE === */
.profile-hero { text-align: center; padding: 4rem 2rem; }
.profile-badge { font-size: 64px; margin-bottom: 1rem; animation: badgeFloat 3s ease-in-out infinite; }
@keyframes badgeFloat { 0%, 100% { transform: translateY(0); } 50% { transform: translateY(-8px); } }

.profile-type { font-size: clamp(36px, 6vw, 56px); font-weight: 700; letter-spacing: -0.04em; margin: 0 0 0.5rem; }
.score-display { font-family: 'JetBrains Mono', monospace; font-size: clamp(32px, 5vw, 48px); font-weight: 700; margin: 1rem 0; }

.score-current {
    background: linear-gradient(135deg, """ + green + """, """ + blue + """);
    -webkit-background-clip: text; -webkit-text-fill-color: transparent;
}

.score-max { color: """ + border + """; }

.progress-bar-track { width: 100%; max-width: 320px; height: 3px; background: """ + border + """; margin: 2rem auto; border-radius: 2px; overflow: hidden; }
.progress-bar-fill { height: 100%; background: linear-gradient(90deg, """ + green + """, """ + blue + """); transition: width 1.5s ease; }

/* === CARDS === */
.comparison-box, .insight-box, .tip-item {
    background: """ + card_bg + """;
    border: 1px solid """ + border + """;
    border-radius: 12px;
    padding: 1.5rem;
    margin: 1rem 0;
    transition: all 0.3s ease;
}

.comparison-box:hover, .tip-item:hover { border-color: """ + green + """; transform: translateY(-2px); }
.comparison-label { font-size: 11px; font-weight: 700; letter-spacing: 3px; text-transform: uppercase; color: """ + text_sec + """; margin-bottom: 0.75rem; }
.comparison-text { font-size: 18px; font-weight: 700; color: """ + text + """; }

.comparison-highlight {
    background: linear-gradient(90deg, """ + green + """, """ + blue + """);
    -webkit-background-clip: text; -webkit-text-fill-color: transparent;
}

.insight-box { border-left: 3px solid; border-radius: 0 12px 12px 0; }
.insight-title { font-size: 14px; font-weight: 700; margin: 0 0 0.5rem; }
.insight-text { font-size: 14px; color: """ + text_sec + """; line-height: 1.6; }

.tip-item { display: flex; align-items: center; gap: 0.75rem; }
.tip-number { font-family: 'JetBrains Mono', monospace; font-weight: 700; }

/* === METRICS === */
[data-testid="stMetricValue"] {
    font-family: 'JetBrains Mono', monospace !important;
    background: linear-gradient(135deg, """ + green + """, """ + blue + """);
    -webkit-background-clip: text; -webkit-text-fill-color: transparent;
    font-size: 28px !important; font-weight: 700 !important;
}

[data-testid="stMetricLabel"] {
    color: """ + text_sec + """ !important;
    font-size: 12px !important; font-weight: 600 !important;
    letter-spacing: 1px !important; text-transform: uppercase !important;
}

/* === ALERT === */
.stAlert { background: """ + card_bg + """ !important; border: 1px solid """ + border + """ !important; border-radius: 10px !important; }

/* === DIVIDER === */
hr {
    border: none !important; height: 1px !important;
    background: linear-gradient(90deg, transparent, """ + border + """, transparent) !important;
    margin: 2rem 0 !important;
}

/* === SCROLLBAR === */
::-webkit-scrollbar { width: 5px; }
::-webkit-scrollbar-track { background: """ + bg + """; }
::-webkit-scrollbar-thumb { background: linear-gradient(180deg, """ + green + """, """ + blue + """); border-radius: 3px; }

/* === ANIMATIONS === */
@keyframes fadeInUp { from { opacity: 0; transform: translateY(20px); } to { opacity: 1; transform: translateY(0); } }
@keyframes spin { to { transform: rotate(360deg); } }

.section-appear { opacity: 0; animation: fadeInUp 0.6s ease-out forwards; }
.section-appear:nth-child(2) { animation-delay: 0.1s; }
.section-appear:nth-child(3) { animation-delay: 0.2s; }
.section-appear:nth-child(4) { animation-delay: 0.3s; }
.progress-animated { animation: progressGrow 0.8s ease-out forwards; transform-origin: left; }
@keyframes progressGrow { from { transform: scaleX(0); } to { transform: scaleX(1); } }

.spinner {
    width: 40px; height: 40px;
    border: 2px solid """ + border + """;
    border-top-color: """ + green + """;
    border-right-color: """ + blue + """;
    border-radius: 50%;
    animation: spin 0.8s linear infinite;
    margin: 0 auto;
}

@media (prefers-reduced-motion: reduce) {
    *, *::before, *::after { animation-duration: 0.01ms !important; transition-duration: 0.01ms !important; }
}

@media (max-width: 768px) {
    .hero-wrapper { min-height: 60vh; }
    .hero-title { font-size: 40px; }
    .profile-type { font-size: 32px; }
    .progress-node { width: 70px; }
}
</style>
"""

def get_particles_js(dark_mode=True):
    green = "0, 255, 136" if dark_mode else "0, 170, 85"
    blue = "0, 212, 255" if dark_mode else "0, 136, 170"
    opacity = "0.3" if dark_mode else "0.12"

    return """
<script>
(function() {
    if (document.getElementById('particle-canvas')) return;
    var c = document.createElement('canvas');
    c.id = 'particle-canvas';
    c.style.cssText = 'position:fixed;top:0;left:0;width:100%;height:100%;z-index:0;pointer-events:none;opacity:""" + opacity + """;
    document.body.appendChild(c);
    var ctx = c.getContext('2d');
    c.width = innerWidth; c.height = innerHeight;
    var p = [];
    for (var i = 0; i < 30; i++) p.push({
        x: Math.random()*c.width, y: Math.random()*c.height,
        s: Math.random()*1.5+0.5, sy: Math.random()*0.15+0.05,
        sx: (Math.random()-0.5)*0.08, o: Math.random()*0.4+0.1,
        c: Math.random()>0.5 ? '""" + green + """' : '""" + blue + """'
    });
    var last = 0;
    function draw(now) {
        requestAnimationFrame(draw);
        if (now-last < 33) return; last = now;
        if (document.hidden) return;
        ctx.clearRect(0,0,c.width,c.height);
        for (var i=0;i<p.length;i++) {
            var q=p[i];
            ctx.beginPath(); ctx.arc(q.x,q.y,q.s,0,Math.PI*2);
            ctx.fillStyle='rgba('+q.c+','+q.o+')'; ctx.fill();
            q.y-=q.sy; q.x+=q.sx;
            if (q.y<-10) { q.y=c.height+10; q.x=Math.random()*c.width; }
        }
    }
    requestAnimationFrame(draw);
    addEventListener('resize', function(){ c.width=innerWidth; c.height=innerHeight; });
})();
</script>
"""

def get_counter_js(score, max_score):
    """Score counter — returns empty string (score rendered directly in HTML banner)."""
    # JS animation unreliable in Streamlit's st.html() — score rendered directly
    return ""
