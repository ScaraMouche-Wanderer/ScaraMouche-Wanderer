#!/usr/bin/env python3
"""Apply the profile's neon palette without changing the generated game data."""

from pathlib import Path
import colorsys
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
    document = ET.fromstring(result)
    # Hue follows the calendar column; lightness retains contribution intensity.
    dark = palette is PALETTES["dark"]
    source_levels = ["#0e4429", "#006d32", "#26a641", "#39d353"] if dark else ["#9be9a8", "#40c463", "#30a14e", "#216e39"]
    levels = [palette[color] for color in source_levels]
    width = float(document.get("width", "1166"))
    for rectangle in document.iter("{http://www.w3.org/2000/svg}rect"):
        position = min(1.0, float(rectangle.get("x", "0")) / width)
        hue = (320.0 - 250.0 * position) / 360.0
        shades = [0.51, 0.58, 0.65, 0.72] if dark else [0.78, 0.68, 0.58, 0.47]
        rainbow = []
        for lightness in shades:
            rgb = colorsys.hls_to_rgb(hue, lightness, 0.94)
            rainbow.append("#" + "".join(f"{round(channel * 255):02x}" for channel in rgb))
        replacements = dict(zip(levels, rainbow))
        for node in [rectangle, *list(rectangle)]:
            for attribute in ("fill", "values"):
                if attribute in node.attrib:
                    node.set(attribute, re.sub(r"#[0-9a-fA-F]{6}(?![0-9a-fA-F])", lambda match: replacements.get(match.group().lower(), match.group()), node.get(attribute)))
    ET.register_namespace("", "http://www.w3.org/2000/svg")
    result = ET.tostring(document, encoding="unicode")
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_text(result)
    print(f"{target}: rainbow calendar palette; gameplay and embedded sprites preserved.")


if __name__ == "__main__":
    for theme in ("dark", "light"):
        suffix = "-dark" if theme == "dark" else ""
        colorize(
            Path(f"dist/pacman-contribution-graph{suffix}.svg"),
            Path(f"generated/pacman{suffix}.svg"),
            PALETTES[theme],
        )
