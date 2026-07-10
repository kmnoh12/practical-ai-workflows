#!/usr/bin/env python3
from pathlib import Path
from PIL import Image, ImageDraw, ImageFont

ROOT = Path(__file__).resolve().parents[1]
OUT_EVIDENCE = ROOT / "public" / "assets" / "evidence" / "source-map-workflow-english.png"
OUT_SOCIAL = ROOT / "public" / "assets" / "social" / "practical-ai-workflows-og.png"
OUT_AGENT_EVIDENCE = ROOT / "public" / "assets" / "evidence" / "hermes-max-ultra-control-gap.png"
OUT_AGENT_SOCIAL = ROOT / "public" / "assets" / "social" / "hermes-max-ultra-og.png"
OUT_HOME_SOCIAL = ROOT / "public" / "assets" / "social" / "agent-field-notes-og.png"

FONT_REGULAR = "/System/Library/Fonts/HelveticaNeue.ttc"
FONT_BOLD = "/System/Library/Fonts/HelveticaNeue.ttc"
FONT_MONO = "/System/Library/Fonts/Monaco.ttf"

PAPER = "#f3f0e8"
INK = "#111111"
MUTED = "#5f5a52"
ACCENT = "#0f5b47"
PALE = "#d9efe4"
WHITE = "#ffffff"
SIGNAL = "#c93b16"
NIGHT = "#171716"
CREAM = "#f5f1e8"
GRID = "#d6d0c5"
SOFT = "#e9e3d7"


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


def wrapped_lines(draw, text, max_width, text_font):
    lines = []
    current = ""
    for word in text.split():
        candidate = (current + " " + word).strip()
        if current and draw.textbbox((0, 0), candidate, font=text_font)[2] > max_width:
            lines.append(current)
            current = word
        else:
            current = candidate
    if current:
        lines.append(current)
    return lines


def draw_wrapped(draw, text, xy, max_width, text_font, fill, line_gap=8):
    x, y = xy
    bbox = draw.textbbox((0, 0), "Ag", font=text_font)
    line_height = bbox[3] - bbox[1]
    for i, value in enumerate(wrapped_lines(draw, text, max_width, text_font)):
        draw.text((x, y + i * (line_height + line_gap)), value, font=text_font, fill=fill)


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


def agent_evidence_asset():
    w, h = 1568, 948
    im = Image.new("RGB", (w, h), CREAM)
    d = ImageDraw.Draw(im)

    d.rectangle((34, 34, w - 34, h - 34), fill=CREAM, outline=NIGHT, width=4)
    d.rectangle((34, 34, w - 34, 98), fill=NIGHT)
    d.text((64, 56), "PRACTICAL AI WORKFLOWS / CONTROL-PATH AUDIT", font=font(18, bold=True, mono=True), fill=CREAM)
    d.text((1215, 56), "CHECKED 2026-07-10", font=font(16, mono=True), fill=CREAM)

    d.text((68, 142), "The control gap", font=font(74, bold=True), fill=NIGHT)
    d.text((68, 220), "is not the model.", font=font(74, bold=True), fill=SIGNAL)
    draw_wrapped(
        d,
        "Hermes reaches GPT-5.6 Sol. Its UI, wire value, and Ultra orchestration still describe three different states.",
        (74, 326),
        620,
        font(29),
        "#4f4a43",
        10,
    )

    rows = [
        ("01 / MODEL", "gpt-5.6", "routes to", "gpt-5.6-sol", "PUBLIC MODEL"),
        ("02 / HERMES UI", "xhigh", "is labeled", "Max", "LABEL GAP"),
        ("03 / HERMES CORE", "max", "can reach", "reasoning.effort", "WIRE PATH"),
        ("04 / ULTRA", "max reasoning", "plus", "4 agents by default", "MODE GAP"),
    ]
    x1, x2 = 760, 1492
    y = 142
    for i, (label, left, verb, right, state) in enumerate(rows):
        height = 150
        fill = "#fffdf8" if i % 2 == 0 else SOFT
        d.rectangle((x1, y, x2, y + height), fill=fill, outline=NIGHT, width=2)
        d.text((x1 + 20, y + 17), label, font=font(15, bold=True, mono=True), fill="#5a554e")
        d.text((x1 + 20, y + 61), left, font=fit_text(d, left, 230, 28, 18, bold=True), fill=NIGHT)
        d.text((x1 + 265, y + 67), verb.upper(), font=font(14, mono=True), fill="#736d64")
        d.text((x1 + 390, y + 61), right, font=fit_text(d, right, 300, 28, 18, bold=True), fill=SIGNAL if i in (1, 3) else NIGHT)
        d.rectangle((x2 - 156, y + 16, x2 - 16, y + 43), fill=SIGNAL if i in (1, 3) else NIGHT)
        state_font = fit_text(d, state, 120, 13, 10, bold=True)
        state_box = d.textbbox((0, 0), state, font=state_font)
        state_width = state_box[2] - state_box[0]
        d.text((x2 - 86 - state_width / 2, y + 22), state, font=state_font, fill=CREAM)
        y += 166

    d.rectangle((68, 668, 690, 830), fill=NIGHT)
    d.text((92, 694), "VERDICT", font=font(16, bold=True, mono=True), fill=SIGNAL)
    draw_wrapped(
        d,
        "A max request value cannot recreate an Ultra agent mode by itself.",
        (92, 738),
        550,
        font(31, bold=True),
        CREAM,
        8,
    )
    d.text(
        (68, 868),
        "SOURCES: OPENAI GPT-5.6 DOCS / HERMES 0.18.2 / UPSTREAM caf557be5 / SANITIZED LOCAL ROUTE",
        font=font(15, mono=True),
        fill="#5a554e",
    )

    OUT_AGENT_EVIDENCE.parent.mkdir(parents=True, exist_ok=True)
    im.save(OUT_AGENT_EVIDENCE, optimize=True)


def agent_social_asset():
    w, h = 1200, 630
    im = Image.new("RGB", (w, h), CREAM)
    d = ImageDraw.Draw(im)

    d.rectangle((32, 32, w - 32, h - 32), fill=CREAM, outline=NIGHT, width=4)
    d.rectangle((32, 32, w - 32, 92), fill=NIGHT)
    d.text((58, 53), "PRACTICAL AI WORKFLOWS", font=font(18, bold=True, mono=True), fill=CREAM)
    d.text((924, 53), "INVESTIGATION 01", font=font(15, mono=True), fill=CREAM)

    d.text((66, 142), "HERMES SAYS MAX.", font=font(62, bold=True), fill=NIGHT)
    d.text((66, 211), "THE CODE SAYS xhigh.", font=font(62, bold=True), fill=SIGNAL)
    d.text((70, 306), "Why GPT-5.6 Sol Max and Ultra disappear", font=font(29), fill="#4f4a43")
    d.text((70, 344), "inside a third-party agent runtime.", font=font(29), fill="#4f4a43")

    boxes = [
        ("UI", "xhigh", "labeled Max"),
        ("WIRE", "max", "accepted"),
        ("ULTRA", "4 agents", "separate mode"),
    ]
    x = 70
    for i, (label, value, note) in enumerate(boxes):
        width = 334
        d.rectangle((x, 424, x + width, 548), fill="#fffdf8" if i != 1 else SOFT, outline=NIGHT, width=2)
        d.text((x + 16, 440), label, font=font(15, bold=True, mono=True), fill="#6a645c")
        d.text((x + 16, 474), value, font=font(29, bold=True), fill=SIGNAL if i in (0, 2) else NIGHT)
        d.text((x + 16, 516), note, font=font(17), fill="#5a554e")
        x += width + 14

    d.text((70, 576), "MODEL ACCESS / REASONING / ORCHESTRATION / REAL FIXES", font=font(15, mono=True), fill="#5a554e")
    OUT_AGENT_SOCIAL.parent.mkdir(parents=True, exist_ok=True)
    im.save(OUT_AGENT_SOCIAL, optimize=True)


def home_social_asset():
    w, h = 1200, 630
    im = Image.new("RGB", (w, h), CREAM)
    d = ImageDraw.Draw(im)

    d.rectangle((32, 32, w - 32, h - 32), fill=CREAM, outline=NIGHT, width=4)
    d.rectangle((32, 32, 388, h - 32), fill=NIGHT)
    d.text((58, 58), "PRACTICAL", font=font(18, bold=True, mono=True), fill=CREAM)
    d.text((58, 86), "AI WORKFLOWS", font=font(18, bold=True, mono=True), fill=CREAM)
    d.text((58, 492), "FIELD NOTES", font=font(15, bold=True, mono=True), fill=SIGNAL)
    d.text((58, 526), "MODELS / AGENTS", font=font(15, mono=True), fill=CREAM)
    d.text((58, 554), "FAILURES / FIXES", font=font(15, mono=True), fill=CREAM)

    d.text((438, 96), "AI agents fail", font=font(72, bold=True), fill=NIGHT)
    d.text((438, 173), "in the gaps.", font=font(72, bold=True), fill=SIGNAL)
    draw_wrapped(
        d,
        "Independent tests of model access, reasoning controls, orchestration, and the fixes that survive real workflows.",
        (444, 290),
        670,
        font(29),
        "#4f4a43",
        10,
    )
    d.line((444, 454, 1110, 454), fill=NIGHT, width=2)
    labels = [("01", "ACCESS"), ("02", "EFFORT"), ("03", "AGENTS"), ("04", "PROOF")]
    x = 444
    for num, label in labels:
        d.text((x, 486), num, font=font(14, bold=True, mono=True), fill=SIGNAL)
        d.text((x, 516), label, font=font(18, bold=True), fill=NIGHT)
        x += 170

    OUT_HOME_SOCIAL.parent.mkdir(parents=True, exist_ok=True)
    im.save(OUT_HOME_SOCIAL, optimize=True)


if __name__ == "__main__":
    evidence_asset()
    social_asset()
    agent_evidence_asset()
    agent_social_asset()
    home_social_asset()
    print(OUT_EVIDENCE)
    print(OUT_SOCIAL)
    print(OUT_AGENT_EVIDENCE)
    print(OUT_AGENT_SOCIAL)
    print(OUT_HOME_SOCIAL)
