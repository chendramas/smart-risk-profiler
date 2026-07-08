import streamlit as st
import math

FINANCIAL_GOALS = [
    {
        "key": "rumah",
        "label": "Beli Rumah",
        "icon": "🏠",
        "default_amount": 500_000_000,
        "default_years": 5,
        "description": "Target dana untuk DP atau beli rumah",
    },
    {
        "key": "darurat",
        "label": "Dana Darurat",
        "icon": "🏦",
        "default_amount": 100_000_000,
        "default_years": 1,
        "description": "Dana cadangan untuk keadaan darurat",
    },
    {
        "key": "nikah",
        "label": "Dana Nikah",
        "icon": "💍",
        "default_amount": 200_000_000,
        "default_years": 3,
        "description": "Target dana untuk pernikahan",
    },
    {
        "key": "pensiun",
        "label": "Dana Pensiun",
        "icon": "🏖️",
        "default_amount": 5_000_000_000,
        "default_years": 25,
        "description": "Target dana untuk pensiun nyaman",
    },
    {
        "key": "pendidikan",
        "label": "Dana Pendidikan Anak",
        "icon": "🎓",
        "default_amount": 500_000_000,
        "default_years": 15,
        "description": "Target dana untuk pendidikan anak",
    },
]

INFLATION_RATE = 0.04


def calculate_required_return(target_amount, current_savings, years, monthly_contribution=0):
    """
    Calculate required annual return to reach a target.
    
    Uses binary search to solve: FV = PV*(1+r)^n + PMT*[((1+r)^n - 1)/r]
    """
    if years <= 0:
        return 0
    
    pv = current_savings
    fv = target_amount
    n = years
    pmt = monthly_contribution * 12
    
    total_contributions = pv + (pmt * n)
    if total_contributions >= fv:
        return 0
    
    low, high = -0.05, 0.50
    for _ in range(100):
        mid = (low + high) / 2
        r = mid
        if r == 0:
            calculated = pv + (pmt * n)
        else:
            calculated = pv * (1 + r) ** n + pmt * (((1 + r) ** n - 1) / r)
        
        if calculated < fv:
            low = mid
        else:
            high = mid
    
    return round(mid * 100, 1)


def get_risk_need_level(required_return):
    """
    Categorize risk need based on required return (adjusted for Indonesian inflation).
    RENDAH: < 5% real return, SEDANG: 5-10%, TINGGI: > 10%
    """
    real_return = required_return - (INFLATION_RATE * 100)
    
    if real_return <= 3:
        return "RENDAH", "#00FF88", "Bisa dicapai dengan instrumen aman (deposito, RDPU)"
    elif real_return <= 8:
        return "SEDANG", "#FFB800", "Butuh campuran saham + obligasi"
    else:
        return "TINGGI", "#FF3366", "Butuh porsi saham signifikan — flag jika melebihi capacity"


def calculate_goal_analysis(goals_data):
    """
    Analyze all user financial goals.
    
    Returns:
        dict per goal: required_return, risk_need_level, real_target
        overall: highest risk need, red light flag
    """
    results = {}
    highest_need = "RENDAH"
    red_light = False
    
    for goal in FINANCIAL_GOALS:
        data = goals_data.get(goal["key"], {})
        target = data.get("target", goal["default_amount"])
        years = data.get("years", goal["default_years"])
        current = data.get("current_savings", 0)
        monthly = data.get("monthly_contribution", 0)
        
        req_return = calculate_required_return(target, current, years, monthly)
        level, color, description = get_risk_need_level(req_return)
        
        real_target = target / ((1 + INFLATION_RATE) ** years)
        
        results[goal["key"]] = {
            "label": goal["label"],
            "icon": goal["icon"],
            "target": target,
            "years": years,
            "current_savings": current,
            "monthly_contribution": monthly,
            "required_return": req_return,
            "risk_need_level": level,
            "risk_need_color": color,
            "risk_need_description": description,
            "real_target": round(real_target),
            "inflation_impact": round(target - real_target),
        }
        
        if level == "TINGGI":
            highest_need = "TINGGI"
            red_light = True
        elif level == "SEDANG" and highest_need != "TINGGI":
            highest_need = "SEDANG"
    
    return {
        "goals": results,
        "highest_need": highest_need,
        "red_light": red_light,
    }


def render_step_goals():
    """Render goal input form in Step 1."""
    green = "#00FF88"
    blue = "#00D4FF"
    
    st.html(f"""
    <div style="margin: 2rem 0 1rem;">
        <p style="font-size: 11px; font-weight: 700; letter-spacing: 3px; 
           text-transform: uppercase; color: {blue}; margin: 0 0 0.5rem;">
            Tujuan Finansial
        </p>
        <p style="color: #888; font-size: 13px; margin: 0;">
            Isi tujuan lo (opsional). Ini bantu hitung berapa return yang lo BUTUHKAN.
        </p>
    </div>
    """)
    
    goals_data = {}
    
    for goal in FINANCIAL_GOALS:
        with st.expander(f"{goal['icon']} {goal['label']}", expanded=False):
            st.caption(goal["description"])
            
            col1, col2 = st.columns(2)
            with col1:
                target = st.number_input(
                    "Target (Rp)",
                    min_value=0,
                    value=goal["default_amount"],
                    step=50_000_000,
                    key=f"goal_target_{goal['key']}",
                    format="%d",
                )
                years = st.number_input(
                    "Waktu (tahun)",
                    min_value=1,
                    max_value=50,
                    value=goal["default_years"],
                    key=f"goal_years_{goal['key']}",
                )
            with col2:
                current = st.number_input(
                    "Udah terkumpul (Rp)",
                    min_value=0,
                    value=0,
                    step=10_000_000,
                    key=f"goal_current_{goal['key']}",
                    format="%d",
                )
                monthly = st.number_input(
                    "Tabungan/bulan (Rp)",
                    min_value=0,
                    value=0,
                    step=1_000_000,
                    key=f"goal_monthly_{goal['key']}",
                    format="%d",
                )
            
            goals_data[goal["key"]] = {
                "target": target,
                "years": years,
                "current_savings": current,
                "monthly_contribution": monthly,
            }
    
    return goals_data


def format_rp(amount):
    """Format number to Rupiah."""
    if amount >= 1_000_000_000:
        return f"Rp {amount/1_000_000_000:.1f} M"
    elif amount >= 1_000_000:
        return f"Rp {amount/1_000_000:.0f} jt"
    elif amount >= 1_000:
        return f"Rp {amount/1_000:.0f} rb"
    else:
        return f"Rp {amount:,.0f}"
