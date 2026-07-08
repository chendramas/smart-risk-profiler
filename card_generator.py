import io
import os
from PIL import Image, ImageDraw, ImageFont

from config import COLORS, COLORS_DARK


def _font(size, bold=False):
    """Load font — try system fonts first, fallback to default."""
    font_paths = [
        "/System/Library/Fonts/Helvetica.ttc",
        "/System/Library/Fonts/Avenir.ttc",
        "/Library/Fonts/Arial.ttf",
        "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf",
        "C:/Windows/Fonts/arial.ttf",
    ]
    
    if bold:
        bold_paths = [
            "/System/Library/Fonts/HelveticaBold.ttf",
            "/Library/Fonts/Arial Bold.ttf",
            "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf",
            "C:/Windows/Fonts/arialbd.ttf",
        ]
        font_paths = bold_paths + font_paths
    
    for path in font_paths:
        if os.path.exists(path):
            try:
                return ImageFont.truetype(path, size)
            except (OSError, IOError):
                continue
    
    try:
        return ImageFont.load_default(size=size)
    except TypeError:
        return ImageFont.load_default()


def generate_result_card(nama, profil_name, badge_emoji, score, max_score, alokasi, ct=None):
    """Generate result card as PNG image."""
    W, H = 1080, 1350

    _hex_to_rgb = lambda h: tuple(int(h.lstrip('#')[i:i+2], 16) for i in (0, 2, 4))
    profile_border_map = {
        "KONSERVATIF": _hex_to_rgb(COLORS_DARK["green"]),
        "MODERAT": _hex_to_rgb(COLORS_DARK["blue"]),
        "AGRESIF": _hex_to_rgb(COLORS_DARK["red"]),
    }
    border_color = profile_border_map.get(profil_name, _hex_to_rgb(COLORS_DARK["green"]))

    img = Image.new("RGB", (W, H), (0, 0, 0))
    draw = ImageDraw.Draw(img)

    for y_pos in range(H):
        ratio = y_pos / H
        r = int(5 * (1 - ratio))
        g = int(15 * (1 - ratio))
        b = int(10 * (1 - ratio))
        draw.line([(0, y_pos), (W, y_pos)], fill=(r, g, b))

    margin = 30
    draw.rounded_rectangle(
        [margin, margin, W - margin, H - margin],
        radius=24, outline=border_color, width=3
    )

    draw.line([(margin + 40, margin + 2), (W - margin - 40, margin + 2)], fill=border_color, width=2)

    y = 80
    draw.text((W / 2, y), "SMART RISK PROFILER", font=_font(22), fill=(120, 120, 120), anchor="mm")

    y = 160
    draw.text((W / 2, y), badge_emoji, font=_font(72), anchor="mm")

    y = 270
    draw.text((W / 2, y), profil_name, font=_font(64, bold=True), fill=border_color, anchor="mm")

    y = 350
    draw.text((W / 2, y), f"— {nama} —", font=_font(28), fill=(180, 180, 180), anchor="mm")

    y = 420
    draw.text((W / 2, y), f"Skor: {score}/{max_score}", font=_font(24), fill=(120, 120, 120), anchor="mm")

    score_pct = score / max_score * 100 if max_score > 0 else 0
    bar_x, bar_y, bar_w, bar_h = 200, 470, 680, 8
    draw.rounded_rectangle([bar_x, bar_y, bar_x + bar_w, bar_y + bar_h], radius=4, fill=(17, 17, 17))
    fill_w = max(bar_h, int(bar_w * score_pct / 100))
    draw.rounded_rectangle([bar_x, bar_y, bar_x + fill_w, bar_y + bar_h], radius=4, fill=border_color)

    y = 510
    draw.line([(100, y), (W - 100, y)], fill=(30, 30, 30), width=1)

    if ct:
        y = 540
        draw.text((W / 2, y), "CAPACITY vs TOLERANCE", font=_font(16), fill=(100, 100, 100), anchor="mm")

        y = 580
        draw.text((200, y), "Capacity", font=_font(18), fill=(180, 180, 180))
        draw.text((W - 200, y), f"{ct['capacity']['pct']}%", font=_font(18, bold=True), fill=(0, 212, 255), anchor="rt")
        draw.rounded_rectangle([200, y + 28, 880, y + 36], radius=4, fill=(17, 17, 17))
        cap_fill = max(8, int(680 * ct['capacity']['pct'] / 100))
        draw.rounded_rectangle([200, y + 28, 200 + cap_fill, y + 36], radius=4, fill=(0, 212, 255))

        y += 60
        draw.text((200, y), "Tolerance", font=_font(18), fill=(180, 180, 180))
        draw.text((W - 200, y), f"{ct['tolerance']['pct']}%", font=_font(18, bold=True), fill=(0, 255, 136), anchor="rt")
        draw.rounded_rectangle([200, y + 28, 880, y + 36], radius=4, fill=(17, 17, 17))
        tol_fill = max(8, int(680 * ct['tolerance']['pct'] / 100))
        draw.rounded_rectangle([200, y + 28, 200 + tol_fill, y + 36], radius=4, fill=(0, 255, 136))

        y += 60
    else:
        y = 540

    draw.line([(100, y), (W - 100, y)], fill=(30, 30, 30), width=1)

    y += 30
    draw.text((W / 2, y), "REKOMENDASI ALOKASI", font=_font(16), fill=(100, 100, 100), anchor="mm")
    y += 40

    asset_colors = [(0, 255, 136), (0, 212, 255), (0, 204, 255), (102, 255, 179), (153, 255, 204)]
    for i, (asset, pct) in enumerate(alokasi.items()):
        color = asset_colors[i % len(asset_colors)]
        draw.text((200, y), asset, font=_font(20), fill=(220, 220, 220))
        draw.text((W - 200, y), f"{pct}%", font=_font(20, bold=True), fill=color, anchor="rt")
        draw.rounded_rectangle([200, y + 28, 880, y + 34], radius=3, fill=(10, 10, 10))
        asset_fill = max(6, int(680 * pct / 100))
        draw.rounded_rectangle([200, y + 28, 200 + asset_fill, y + 34], radius=3, fill=color)
        y += 50

    y += 10
    draw.line([(100, y), (W - 100, y)], fill=(30, 30, 30), width=1)

    y += 30
    draw.text((W / 2, y), "Simulasi edukasi, bukan saran investasi", font=_font(16), fill=(80, 80, 80), anchor="mm")
    y += 30
    draw.text((W / 2, y), "Framework: CFA Institute IRP", font=_font(14), fill=(60, 60, 60), anchor="mm")

    draw.line([(margin + 40, H - margin - 2), (W - margin - 40, H - margin - 2)], fill=border_color, width=2)

    buf = io.BytesIO()
    img.save(buf, format="PNG")
    buf.seek(0)
    return buf
