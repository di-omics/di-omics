"""Make the highlight tiles shown at the top of the profile README.

Each tile is one checkable number from a public repository. Edit the list
below, then run:

    python3 assets/make_highlights.py

It writes a light and a dark SVG per tile next to this file.
"""
import pathlib

OUT = pathlib.Path(__file__).resolve().parent

# number, unit, two short lines, repository. Keep every number checkable
# in the repository it names.
TILES = [
    ("8", "environments",
     ["RL for drug development, every", "reward validated like an assay"],
     "drugdev-gym"),
    ("4", "instruments",
     ["as agent-callable MCP tools,", "simulation by default"],
     "plr-mcp"),
    ("5", "playbooks",
     ["for bringing lab instruments", "with no API under Python"],
     "plr-reverse-engineer"),
    ("4", "legs",
     ["of a closed loop, computed:", "it names the one that breaks"],
     "autonomous-lab"),
]

THEMES = {
    "light": {"line": "#d8dee4", "ink": "#24292f", "soft": "#6b7280",
              "accent": "#5b7089"},
    "dark": {"line": "#30363d", "ink": "#e6edf3", "soft": "#8b949e",
             "accent": "#9fb3c8"},
}

FONT = "'Helvetica Neue', Helvetica, Arial, sans-serif"
MONO = "ui-monospace, 'SF Mono', Menlo, Consolas, monospace"


def tile(number, unit, lines, repo, theme):
    c = THEMES[theme]
    text = "".join(
        f'<text x="26" y="{140 + 21 * i}" font-size="15.5"'
        f' fill="{c["soft"]}">{line}</text>'
        for i, line in enumerate(lines))
    return (
        '<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 300 208"'
        f' font-family="{FONT}" font-weight="300">'
        '<rect x="0.5" y="0.5" width="299" height="207" rx="6" fill="none"'
        f' stroke="{c["line"]}"/>'
        f'<text x="24" y="80" font-size="68" font-weight="200"'
        f' fill="{c["ink"]}">{number}</text>'
        f'<text x="26" y="110" font-size="17" fill="{c["accent"]}">'
        f'{unit}</text>'
        f'{text}'
        f'<text x="26" y="190" font-size="13" font-family="{MONO}"'
        f' font-weight="400" fill="{c["ink"]}">{repo}</text>'
        '</svg>\n')


if __name__ == "__main__":
    for index, (number, unit, lines, repo) in enumerate(TILES, start=1):
        for theme in THEMES:
            path = OUT / f"highlight-{index}-{theme}.svg"
            path.write_text(tile(number, unit, lines, repo, theme))
    print(f"Wrote {2 * len(TILES)} tiles to {OUT}")
