CONSISTENCY_CHECKS = [
    {
        "name": "composure_vs_knowledge",
        "scenario_a": 0,
        "scenario_b": 6,
        "description": "Ketahanan emosional vs pengetahuan finansial",
        "explanation": "Kalau bilang 'beli lebih banyak' pas turun 20% tapi jawaban diversifikasi salah, "
                       "kemungkinan besar overconfidence — sok berani tapi ga paham risiko beneran.",
        "inconsistency_rule": "aggressive_on_a_conservative_on_b",
    },
    {
        "name": "composure_vs_experience",
        "scenario_a": 0,
        "scenario_b": 7,
        "description": "Ketahanan emosional vs pengalaman investasi",
        "explanation": "Kalau bilang 'beli lebih banyak' pas turun 20% tapi belum pernah investasi, "
                       "kemungkinan overconfidence — belum pernah ngerasain loss beneran.",
        "inconsistency_rule": "aggressive_on_a_no_experience",
    },
    {
        "name": "preference_vs_perception",
        "scenario_a": 3,
        "scenario_b": 5,
        "description": "Preferensi risiko vs persepsi pasar",
        "explanation": "Kalau pilih 'beli crypto' tapi bilang pasar 'sangat berisiko, bisa rugi total', "
                       "ada kontradiksi — mau taruh uang di sesuatu yang dianggap sangat berisiko.",
        "inconsistency_rule": "aggressive_on_a_fearful_on_b",
    },
]


def detect_overconfidence(responses):
    """Detect overconfidence via consistency checks between scenarios.
    
    Args:
        responses: list of selected option strings for each scenario (8 items)
    
    Returns:
        dict: overconfidence_score (0-100, higher = more overconfident),
              flags (list of detected inconsistencies),
              adjusted (whether scoring was adjusted)
    """
    if not responses or len(responses) < 8:
        return {"score": 0, "flags": [], "adjusted": False, "level": "NORMAL"}

    flags = []
    total_penalty = 0

    for check in CONSISTENCY_CHECKS:
        idx_a = check["scenario_a"]
        idx_b = check["scenario_b"]

        answer_a = responses[idx_a]
        answer_b = responses[idx_b]

        if answer_a is None or answer_b is None:
            continue

        from questions import SCENARIOS
        scenario_a = SCENARIOS[idx_a]
        scenario_b = SCENARIOS[idx_b]

        pos_a = _get_option_position(scenario_a, answer_a)
        pos_b = _get_option_position(scenario_b, answer_b)

        max_a = len(scenario_a["options"])
        max_b = len(scenario_b["options"])

        norm_a = pos_a / (max_a - 1) if max_a > 1 else 0
        norm_b = pos_b / (max_b - 1) if max_b > 1 else 0

        is_inconsistent = False
        severity = 0

        if check["inconsistency_rule"] == "aggressive_on_a_conservative_on_b":
            if norm_a > 0.7 and norm_b < 0.3:
                is_inconsistent = True
                severity = (norm_a - norm_b) * 50

        elif check["inconsistency_rule"] == "aggressive_on_a_no_experience":
            if norm_a > 0.7 and pos_b == 0:
                is_inconsistent = True
                severity = 40

        elif check["inconsistency_rule"] == "aggressive_on_a_fearful_on_b":
            if norm_a > 0.6 and norm_b > 0.7:
                is_inconsistent = True
                severity = (norm_a + norm_b - 1) * 30

        if is_inconsistent:
            total_penalty += severity
            flags.append({
                "check": check["name"],
                "description": check["description"],
                "explanation": check["explanation"],
                "answer_a": answer_a,
                "answer_b": answer_b,
                "severity": round(severity),
            })

    max_possible_penalty = 120
    overconfidence_score = min(100, round(total_penalty / max_possible_penalty * 100))

    if overconfidence_score >= 50:
        level = "TINGGI"
    elif overconfidence_score >= 20:
        level = "MODERAT"
    else:
        level = "NORMAL"

    return {
        "score": overconfidence_score,
        "flags": flags,
        "adjusted": len(flags) > 0,
        "level": level,
    }


def _get_option_position(scenario, answer):
    """Get the position (0-indexed) of the selected option in a scenario."""
    try:
        return scenario["options"].index(answer)
    except ValueError:
        return 0


def get_overconfidence_insight(oc_result):
    """Generate insight text based on overconfidence detection."""
    level = oc_result["level"]
    flags = oc_result["flags"]

    if level == "NORMAL":
        return {
            "title": "✅ Konsisten",
            "text": "Jawaban lo konsisten di semua skenario. "
                    "Penilaian risiko lo reliable — ga ada tanda overconfidence.",
            "color": "#00FF88",
        }
    elif level == "MODERAT":
        flag_text = "; ".join([f['description'] for f in flags])
        return {
            "title": "⚠️ Sedikit Inkonsisten",
            "text": f"Ada beberapa kontradiksi dalam jawaban lo: {flag_text}. "
                    "Ini normal — tapi skor lo di-adjust ke yang lebih konservatif "
                    "untuk menghindari overestimate risiko tolerance.",
            "color": "#FFB800",
        }
    else:
        flag_text = "; ".join([f['description'] for f in flags])
        return {
            "title": "🚨 Overconfidence Terdeteksi",
            "text": f"Jawaban lo menunjukkan pola overconfidence: {flag_text}. "
                    "Kemungkinan besar lo overestimate risk tolerance lo. "
                    "Profil lo di-adjust signifikan ke arah konservatif.",
            "color": "#FF3366",
        }
