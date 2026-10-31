#!/usr/bin/env bash
set -euo pipefail

cp profile-3d-contrib/contributions-3d.svg generated/contributions-3d.svg

python3 - <<'PY'
from pathlib import Path
import xml.etree.ElementTree as ET

expected = [
    'snake.svg', 'snake-dark.svg', 'pacman.svg', 'pacman-dark.svg', 'contributions-3d.svg',
    'stats-dark.svg', 'stats-light.svg', 'languages-dark.svg', 'languages-light.svg',
    'streak-dark.svg', 'streak-light.svg',
    'repo-iot.svg', 'repo-facegate.svg', 'repo-codewriter.svg',
    'repo-prag.svg', 'repo-portfolio.svg',
]
for name in expected:
    path = Path('generated') / name
    tree = ET.parse(path)
    if tree.getroot().tag != '{http://www.w3.org/2000/svg}svg':
        raise SystemExit(f'Not an SVG: {name}')
    if any(error in path.read_text().lower() for error in [
        'something went wrong', 'could not fetch user', 'rate limit exceeded',
    ]):
        raise SystemExit(f'Upstream error card: {name}')
    print(f'Validated {name} ({path.stat().st_size:,} bytes)')
PY

gh auth setup-git
publish_dir="$(mktemp -d)"
if git ls-remote --exit-code origin refs/heads/output >/dev/null 2>&1; then
  git clone --quiet --single-branch --branch output \
    "${GITHUB_SERVER_URL}/${GITHUB_REPOSITORY}.git" "$publish_dir"
else
  git init --quiet --initial-branch=output "$publish_dir"
  git -C "$publish_dir" remote add origin "${GITHUB_SERVER_URL}/${GITHUB_REPOSITORY}.git"
fi

cp generated/*.svg "$publish_dir/"
git -C "$publish_dir" config user.name 'github-actions[bot]'
git -C "$publish_dir" config user.email '41898282+github-actions[bot]@users.noreply.github.com'
git -C "$publish_dir" add -- '*.svg'
if ! git -C "$publish_dir" diff --cached --quiet; then
  git -C "$publish_dir" commit --quiet -m 'Refresh contribution animations and profile cards'
  git -C "$publish_dir" push origin HEAD:output
fi
