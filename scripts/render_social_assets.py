#!/usr/bin/env python3
from pathlib import Path
from PIL import Image, ImageDraw, ImageFont

ROOT = Path(__file__).resolve().parents[1]
OUT_EVIDENCE = ROOT / "public" / "assets" / "evidence" / "source-map-workflow-english.png"
OUT_SOCIAL = ROOT / "public" / "assets" / "social" / "practical-ai-workflows-og.png"

FONT_REGULAR = "/System/Library/Fonts/HelveticaNeue.ttc"
FONT_BOLD = "/System/Library/Fonts/HelveticaNeue.ttc"
FONT_MONO = "/System/Library/Fonts/Monaco.ttf"

PAPER = "#f3f0e8"
INK = "#111111"
MUTED = "#5f5a52"
ACCENT = "#0f5b47"
PALE = "#d9efe4"
WHITE = "#ffffff"


def font(size, bold=False, mono=False):
    path = FONT_MONO if mono else (FONT_BOLD if bold else FONT_REGULAR)
    kwargs = {"size": size}
    if path.endswith(".ttc"):
        kwargs["index"] = 1 if bold else 0
    return ImageFont.truetype(path, **kwargs)


def fit_text(draw, text, max_width, start_size, min_size=20, bold=False):
    for size in range(start_size, min_size - 1, -2):
        f = font(size, bold=bold)
        if draw.textbbox((0, 0), text, font=f)[2] <= max_width:
            return f
    return font(min_size, bold=bold)


def line(draw, xy, fill=INK, width=2):
    draw.line(xy, fill=fill, width=width)


def draw_field_card(draw, box, label, value, accent=False):
    x1, y1, x2, y2 = box
    draw.rectangle(box, fill=PALE if accent else "#faf8f3", outline=INK, width=2)
    draw.text((x1 + 18, y1 + 15), label.upper(), font=font(17, mono=True), fill=MUTED)
    value_font = fit_text(draw, value, x2 - x1 - 36, 29, 20, bold=True)
    draw.text((x1 + 18, y1 + 47), value, font=value_font, fill=ACCENT if accent else INK)


def evidence_asset():
    w, h = 1568, 948
    im = Image.new("RGB", (w, h), PAPER)
    d = ImageDraw.Draw(im)

    for x in range(0, w, 42):
        line(d, (x, 0, x, h), fill="#ded8cc", width=1)
    for y in range(0, h, 42):
        line(d, (0, y, w, y), fill="#ded8cc", width=1)

    d.rectangle((42, 40, w - 42, h - 40), fill=PAPER, outline=INK, width=4)
    d.rectangle((42, 40, w - 42, 106), fill=INK)
    d.text((68, 62), "PRACTICAL AI WORKFLOWS", font=font(19, bold=True, mono=True), fill=PAPER)
    d.text((w - 370, 62), "FIELD TEST 01 / JUL 2026", font=font(17, mono=True), fill=PAPER)

    d.text((72, 152), "The source map", font=font(82, bold=True), fill=INK)
    d.text((72, 232), "comes first.", font=font(82, bold=True), fill=ACCENT)
    body = (
        "The raw NotebookLM capture includes Korean source labels. "
        "This English reconstruction keeps the recorded workflow readable "
        "without pretending the original interface was in English."
    )
    words = body.split()
    lines = []
    current = ""
    for word in words:
        candidate = (current + " " + word).strip()
        if d.textbbox((0, 0), candidate, font=font(29))[2] > 725:
            lines.append(current)
            current = word
        else:
            current = candidate
    if current:
        lines.append(current)
    for i, text in enumerate(lines):
        d.text((76, 342 + i * 40), text, font=font(29), fill=MUTED)

    rx = 880
    draw_field_card(d, (rx, 150, 1490, 258), "Source boundary", "1 synthetic study handout")
    draw_field_card(d, (rx, 274, 1490, 382), "Runs", "1 NotebookLM + 1 ChatGPT")
    draw_field_card(d, (rx, 398, 1490, 506), "Captured", "screenshots + raw outputs")
    draw_field_card(d, (rx, 522, 1490, 630), "Known flaw", "citation-label artifacts", accent=True)

    y1, y2 = 690, 830
    step_w = 346
    steps = [
        ("01", "MAP", "sections + source cues"),
        ("02", "VERIFY", "facts + uncertainty"),
        ("03", "PRACTICE", "closed-book questions"),
        ("04", "REPAIR", "retest missed concepts"),
    ]
    for i, (num, title, detail) in enumerate(steps):
        x1 = 72 + i * step_w
        x2 = x1 + step_w - 16
        d.rectangle((x1, y1, x2, y2), fill=WHITE if i % 2 == 0 else PALE, outline=INK, width=2)
        d.text((x1 + 16, y1 + 16), num, font=font(18, bold=True, mono=True), fill=MUTED)
        d.text((x1 + 16, y1 + 50), title, font=font(30, bold=True), fill=ACCENT if i in (0, 1) else INK)
        d.text((x1 + 16, y1 + 92), detail, font=font(20), fill=MUTED)

    d.text(
        (72, 872),
        "ENGLISH RECONSTRUCTION. ORIGINAL CAPTURE AND RAW OUTPUT REMAIN IN THE PUBLIC EVIDENCE PACK.",
        font=font(16, mono=True),
        fill=MUTED,
    )
    OUT_EVIDENCE.parent.mkdir(parents=True, exist_ok=True)
    im.save(OUT_EVIDENCE, optimize=True)


def social_asset():
    w, h = 1200, 630
    im = Image.new("RGB", (w, h), PAPER)
    d = ImageDraw.Draw(im)
    for x in range(0, w, 40):
        line(d, (x, 0, x, h), fill="#ded8cc", width=1)
    for y in range(0, h, 40):
        line(d, (0, y, w, y), fill="#ded8cc", width=1)

    d.rectangle((34, 34, w - 34, h - 34), fill=PAPER, outline=INK, width=4)
    d.rectangle((34, 34, w - 34, 92), fill=INK)
    d.text((58, 52), "PRACTICAL AI WORKFLOWS", font=font(18, bold=True, mono=True), fill=PAPER)
    d.text((875, 52), "SOURCE-GROUNDED", font=font(16, mono=True), fill=PAPER)

    d.text((66, 145), "Stop summarizing", font=font(70, bold=True), fill=INK)
    d.text((66, 216), "PDFs first.", font=font(70, bold=True), fill=ACCENT)
    d.text((70, 315), "Map the source. Check the claims.", font=font(31), fill=MUTED)
    d.text((70, 356), "Then turn verified notes into retrieval practice.", font=font(31), fill=MUTED)

    steps = [("01", "SOURCE MAP"), ("02", "CLAIM CHECK"), ("03", "RETRIEVAL"), ("04", "REPAIR")]
    x = 70
    for i, (num, label) in enumerate(steps):
        bw = 250
        d.rectangle((x, 440, x + bw, 526), fill=PALE if i < 2 else WHITE, outline=INK, width=2)
        d.text((x + 14, 454), num, font=font(15, bold=True, mono=True), fill=MUTED)
        d.text((x + 14, 485), label, font=font(21, bold=True), fill=ACCENT if i < 2 else INK)
        x += bw + 14

    d.text((70, 562), "PROMPTS / SCREENSHOTS / RAW OUTPUTS / FAILURE LOGS", font=font(16, mono=True), fill=MUTED)
    OUT_SOCIAL.parent.mkdir(parents=True, exist_ok=True)
    im.save(OUT_SOCIAL, optimize=True)


if __name__ == "__main__":
    evidence_asset()
    social_asset()
    print(OUT_EVIDENCE)
    print(OUT_SOCIAL)
