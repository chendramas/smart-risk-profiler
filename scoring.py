from config import ALLOCATIONS, MAX_USIA_SCORE, MAX_HORIZON_SCORE, MAX_PENGHASILAN_SCORE, BEHAVIORAL_LABELS
from questions import SCENARIOS
from overconfidence import detect_overconfidence
from financial_health import get_financial_health_score


def get_score_breakdown(usia, penghasilan, horizon, responses):
    """
    Calculate scoring breakdown using CFA Institute 3-Factor IRP Model.
    Factor 1 & 2 (Risk Need + Risk-Taking Ability): usia, penghasilan, horizon.
    Factor 3 (Behavioral Loss Tolerance): averaged per category from scenarios.
    """
    breakdown = {}

    # === FACTOR 1 & 2: Risk Need + Risk-Taking Ability ===
    if usia < 25: breakdown["Usia"] = 3
    elif usia < 35: breakdown["Usia"] = 2
    else: breakdown["Usia"] = 1

    if penghasilan == "> 15 juta": breakdown["Penghasilan"] = 2
    elif penghasilan == "5 - 15 juta": breakdown["Penghasilan"] = 1
    else: breakdown["Penghasilan"] = 0

    if horizon == "< 1 tahun": breakdown["Horizon"] = 1
    elif horizon == "1 - 3 tahun": breakdown["Horizon"] = 2
    elif horizon == "3 - 5 tahun": breakdown["Horizon"] = 3
    else: breakdown["Horizon"] = 4

    # === FACTOR 3: Behavioral Loss Tolerance ===
    # Aggregate by category (averaged)
    category_scores = {}
    for i, s in enumerate(SCENARIOS):
        answer = responses[i]
        score = s["options"].index(answer) + 1
        cat = s["category"]
        if cat not in category_scores:
            category_scores[cat] = []
        category_scores[cat].append(score)

    for cat, scores in category_scores.items():
        avg = sum(scores) / len(scores)
        breakdown[cat] = round(avg, 1)

    return breakdown


def get_breakdown_max():
    """Max score per component (averaged per category)."""
    base = {
        "Usia": MAX_USIA_SCORE,
        "Penghasilan": MAX_PENGHASILAN_SCORE,
        "Horizon": MAX_HORIZON_SCORE,
    }
    category_sums = {}
    category_counts = {}
    for s in SCENARIOS:
        cat = s["category"]
        max_val = len(s["options"])
        category_sums[cat] = category_sums.get(cat, 0) + max_val
        category_counts[cat] = category_counts.get(cat, 0) + 1
    
    category_max = {}
    for cat in category_sums:
        category_max[cat] = round(category_sums[cat] / category_counts[cat], 1)
    
    return {**base, **category_max}


def get_capacity_tolerance_split(usia, penghasilan, horizon, responses, fh_answers=None):
    """
    Split Risk Capacity (objective) vs Behavioral Tolerance (subjective).
    Capacity includes Financial Health factors: dana darurat, rasio utang, tanggungan, net worth, rumah.
    """
    # === Original capacity factors ===
    cap_score = 0
    if usia < 25: cap_score += 3
    elif usia < 35: cap_score += 2
    else: cap_score += 1
    
    if penghasilan == "> 15 juta": cap_score += 2
    elif penghasilan == "5 - 15 juta": cap_score += 1
    
    if horizon == "< 1 tahun": cap_score += 1
    elif horizon == "1 - 3 tahun": cap_score += 2
    elif horizon == "3 - 5 tahun": cap_score += 3
    else: cap_score += 4

    cap_max = MAX_USIA_SCORE + MAX_PENGHASILAN_SCORE + MAX_HORIZON_SCORE

    # === Financial Health bonus ===
    fh_score = 0
    fh_max = 0
    fh_data = None
    if fh_answers:
        fh_data = get_financial_health_score(fh_answers)
        fh_score = fh_data["score"]
        fh_max = fh_data["max"]

    total_cap_score = cap_score + fh_score
    total_cap_max = cap_max + fh_max

    # === Behavioral Tolerance ===
    tol_score = 0
    tol_max = 0
    for i, s in enumerate(SCENARIOS):
        answer = responses[i]
        tol_score += s["options"].index(answer) + 1
        tol_max += len(s["options"])

    return {
        "capacity": {
            "score": total_cap_score,
            "max": total_cap_max,
            "pct": round(total_cap_score / total_cap_max * 100) if total_cap_max > 0 else 0,
            "base_score": cap_score,
            "base_max": cap_max,
            "fh_score": fh_score,
            "fh_max": fh_max,
            "fh_data": fh_data,
        },
        "tolerance": {"score": tol_score, "max": tol_max, "pct": round(tol_score / tol_max * 100)},
    }


def get_behavioral_breakdown(responses):
    """Detail breakdown per Behavioral Loss Tolerance component."""
    category_data = {}
    for i, s in enumerate(SCENARIOS):
        cat = s["category"]
        answer = responses[i]
        score = s["options"].index(answer) + 1
        max_score = len(s["options"])
        
        if cat not in category_data:
            category_data[cat] = {"score": 0, "max": 0, "count": 0}
        category_data[cat]["score"] += score
        category_data[cat]["max"] += max_score
        category_data[cat]["count"] += 1

    result = {}
    
    for cat, data in category_data.items():
        pct = round(data["score"] / data["max"] * 100)
        meta = BEHAVIORAL_LABELS.get(cat, {"label": cat, "icon": "📊", "color": "#00FF88"})
        result[cat] = {
            "score": data["score"],
            "max": data["max"],
            "pct": pct,
            "label": meta["label"],
            "icon": meta["icon"],
            "color": meta["color"],
        }

    return result


def get_insight_text(capacity_pct, tolerance_pct):
    """Generate insight based on capacity vs tolerance difference."""
    diff = capacity_pct - tolerance_pct
    
    if diff > 20:
        return {
            "title": "🛡️ Capacity Tinggi, Tolerance Rendah",
            "text": "Lo secara finansial mampu ambil risiko lebih besar, tapi prefer main aman. "
                    "Alokasi lo ditentukan oleh tolerance (yang lebih rendah) karena kalau "
                    "dipaksa agresif, lo bakal panik pas market crash. "
                    "Ini growth potential — naikin tolerance pelan-pelan bisa unlock alokasi lebih growth.",
            "color": "#00D4FF"
        }
    elif diff < -20:
        return {
            "title": "⚡ Tolerance Tinggi, Capacity Rendah",
            "text": "Lo berani ambil risiko, tapi kondisi finansial belum support. "
                    "Alokasi lo dibatasi oleh capacity — fokus bangun dana darurat "
                    "& naikin income dulu. Begitu capacity naik, barulah agresif.",
            "color": "#FF3366"
        }
    else:
        return {
            "title": "⚖️ Seimbang",
            "text": "Profile lo antara capacity dan tolerance cukup seimbang. "
                    "Ini ideal — lo tahu batas kemampuan finansial lo dan "
                    "bertindak sesuai dengan toleransi risiko lo.",
            "color": "#00FF88"
        }


def calculate_score(usia, penghasilan, horizon, responses):
    return round(sum(get_score_breakdown(usia, penghasilan, horizon, responses).values()))


def get_risk_number(effective_pct):
    """
    Map effective percentage to 1-99 Risk Number scale.

    Mapping:
    1-20: Very Conservative
    21-40: Conservative
    41-60: Moderate
    61-80: Growth
    81-99: Aggressive

    Uses 1-99 instead of 1-100 because 100 implies certainty.
    """
    pct = max(0, min(100, effective_pct))
    risk_number = max(1, min(99, round(pct * 0.98 + 1)))
    return risk_number


def get_risk_number_details(risk_number):
    """Get category details for a given Risk Number (color, description, allocations)."""
    if risk_number <= 20:
        return {
            "category": "Very Conservative",
            "color": "#00FF88",
            "description": "Fokus preservasi modal. Cocok untuk dana darurat atau tujuan jangka pendek < 1 tahun.",
            "allocation": {"Deposito/RDPU": 50, "Obligasi Pemerintah": 30, "Emas": 15, "Saham IDX": 5},
            "expected_return": "4-6% per tahun",
            "max_drawdown": "< 5%",
        }
    elif risk_number <= 40:
        return {
            "category": "Conservative",
            "color": "#00CC6A",
            "description": "Prioritas keamanan dengan sedikit growth. Cocok untuk tujuan 1-3 tahun.",
            "allocation": {"RDPU": 30, "Obligasi Pemerintah": 25, "Emas": 15, "Saham IDX": 20, "Reksadana Campuran": 10},
            "expected_return": "6-9% per tahun",
            "max_drawdown": "5-15%",
        }
    elif risk_number <= 60:
        return {
            "category": "Moderate",
            "color": "#00D4FF",
            "description": "Balance growth & safety. Cocok untuk tujuan 3-5 tahun.",
            "allocation": {"RDPU": 15, "Obligasi": 15, "Emas": 10, "Saham IDX": 40, "Reksadana Campuran": 10, "Crypto": 10},
            "expected_return": "9-14% per tahun",
            "max_drawdown": "15-30%",
        }
    elif risk_number <= 80:
        return {
            "category": "Growth",
            "color": "#FFB800",
            "description": "Fokus growth dengan toleransi volatilitas tinggi. Cocok untuk tujuan 5-10 tahun.",
            "allocation": {"Saham IDX": 55, "Reksadana Saham": 15, "Emas": 10, "Obligasi": 10, "Crypto": 10},
            "expected_return": "14-20% per tahun",
            "max_drawdown": "30-50%",
        }
    else:
        return {
            "category": "Aggressive",
            "color": "#FF3366",
            "description": "Maksimalkan return, siap terima volatilitas ekstrem. Cocok untuk tujuan > 10 tahun.",
            "allocation": {"Saham IDX": 50, "Saham Small-Cap": 15, "Crypto": 20, "Emas": 5, "Obligasi": 5, "RDPU": 5},
            "expected_return": "20%+ per tahun",
            "max_drawdown": "50%+",
        }


def get_profile(score, usia=None, penghasilan=None, horizon=None, responses=None,
                allocations=None, fh_answers=None, oc_result=None, la_result=None):
    """
    Determine risk profile using CFA Institute IRP approach.

    Key behaviors:
    1. min(capacity, tolerance) — binding constraint governs
    2. Financial health factors included in capacity
    3. Overconfidence adjustment applied when detected
    4. Loss aversion penalty when coefficient > 2.0
    5. Traffic light reconciliation for factor alignment
    """
    alloc = allocations or ALLOCATIONS
    
    if usia is not None and responses is not None:
        ct = get_capacity_tolerance_split(usia, penghasilan, horizon, responses, fh_answers)
        cap_pct = ct["capacity"]["pct"]
        tol_pct = ct["tolerance"]["pct"]
        
        effective_pct = min(cap_pct, tol_pct)
        
        # === Overconfidence Adjustment ===
        oc_penalty = 0
        if oc_result and oc_result.get("adjusted"):
            oc_penalty = oc_result["score"] * 0.15
            effective_pct = max(0, effective_pct - oc_penalty)
        
        # === Loss Aversion Adjustment ===
        la_penalty = 0
        if la_result and la_result.get("coefficient"):
            coeff = la_result["coefficient"]
            if coeff > 2.0:
                la_penalty = (coeff - 2.0) * 10
                effective_pct = max(0, effective_pct - la_penalty)
        
        growth_potential = max(cap_pct, tol_pct) - min(cap_pct, tol_pct)
        
        traffic_light = _get_traffic_light(cap_pct, tol_pct, oc_result, la_result)
    else:
        # Fallback: use blended score (backward compatibility)
        max_score = get_max_score()
        effective_pct = (score / max_score * 100) if max_score > 0 else 0
        growth_potential = 0
        traffic_light = "GREEN"
        ct = None
        oc_penalty = 0
        la_penalty = 0
    
    if effective_pct <= 30:
        profile_name = "KONSERVATIF"
    elif effective_pct <= 65:
        profile_name = "MODERAT"
    else:
        profile_name = "AGRESIF"
    
    return profile_name, alloc[profile_name], {
        "growth_potential": growth_potential,
        "traffic_light": traffic_light,
        "ct": ct,
        "effective_pct": effective_pct,
        "oc_penalty": oc_penalty,
        "la_penalty": la_penalty,
        "cap_pct": cap_pct if usia is not None else None,
        "tol_pct": tol_pct if usia is not None else None,
    }


def _get_traffic_light(cap_pct, tol_pct, oc_result=None, la_result=None):
    """
    Traffic Light Reconciliation.
    GREEN: All factors aligned. YELLOW: Behavioral mismatch — caution needed.
    RED: Risk need exceeds capacity or high bias detected — reevaluate.
    """
    diff = abs(cap_pct - tol_pct)
    
    has_oc = oc_result and oc_result.get("level") in ("MODERAT", "TINGGI")
    has_high_la = la_result and la_result.get("coefficient", 0) > 2.5
    
    if diff > 30 or has_oc or has_high_la:
        return "RED"
    elif diff > 15:
        return "YELLOW"
    else:
        return "GREEN"


def get_max_score():
    return sum(get_breakdown_max().values())
