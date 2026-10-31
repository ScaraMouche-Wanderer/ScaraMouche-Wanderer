#!/usr/bin/env python3
"""Apply the profile's neon palette without changing the generated game data."""

from pathlib import Path
import re
import xml.etree.ElementTree as ET


PALETTES = {
    "dark": {
        "#0d1117": "#080c1a",
        "#161b22": "#171b3a",
        "#0e4429": "#5b21b6",
        "#006d32": "#a855f7",
        "#26a641": "#ff2d95",
        "#39d353": "#00e5ff",
        "#8b949e": "#bec9ff",
    },
    "light": {
        "#ebedf0": "#ede9fe",
        "#9be9a8": "#d8b4fe",
        "#40c463": "#c084fc",
        "#30a14e": "#f472b6",
        "#216e39": "#06b6d4",
        "#57606a": "#5b21b6",
    },
}


def colorize(source: Path, target: Path, palette: dict[str, str]) -> None:
    original = source.read_text()
    document = ET.fromstring(original)
    if document.tag != "{http://www.w3.org/2000/svg}svg":
        raise ValueError(f"Expected an SVG from the game renderer: {source}")
    changes = 0

    def replace(match: re.Match) -> str:
        nonlocal changes
        color = match.group().lower()
        if color in palette:
            changes += 1
            return palette[color]
        return match.group()

    result = re.sub(r"#[0-9a-fA-F]{6}(?![0-9a-fA-F])", replace, original)
    if not changes:
        raise ValueError("The upstream game palette changed; review colors before publishing.")
    ET.fromstring(result)
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_text(result)
    print(f"{target}: recolored {changes} values; gameplay and embedded sprites preserved.")


if __name__ == "__main__":
    for theme in ("dark", "light"):
        suffix = "-dark" if theme == "dark" else ""
        colorize(
            Path(f"dist/pacman-contribution-graph{suffix}.svg"),
            Path(f"generated/pacman{suffix}.svg"),
            PALETTES[theme],
        )
