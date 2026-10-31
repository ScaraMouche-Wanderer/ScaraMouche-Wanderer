# Profile integrations

The [profile visuals workflow](.github/workflows/profile-visuals.yml) runs daily
at 00:23 UTC and can be triggered manually. It uses the repository's automatic
GitHub Actions token; no personal access token or external account is needed.

| Integration | Upstream | Output |
| --- | --- | --- |
| Contribution snake | [Platane/snk](https://github.com/Platane/snk) | Animated light/dark snake SVGs |
| 3D contribution calendar | [yoshi389111/github-profile-3d-contrib](https://github.com/yoshi389111/github-profile-3d-contrib) | Animated contribution skyline, radar and language breakdown |
| Stats, languages and repository cards | [stats-organization/github-readme-stats-action](https://github.com/stats-organization/github-readme-stats-action) | Light/dark account cards and five project cards |
| Contribution streak | [DenverCoder1/github-readme-streak-stats](https://github.com/DenverCoder1/github-readme-streak-stats) | Light/dark total/current/longest streak cards |
| Header | [kyechan99/capsule-render](https://github.com/kyechan99/capsule-render) | Locally stored animated wave header |
| Skill icons | [tandpfun/skill-icons](https://github.com/tandpfun/skill-icons) | Locally stored icon strips; [license](assets/skill-icons-LICENSE) |

Generated contribution graphics and cards live on the `output` branch. The
workflow validates every SVG before publishing, and preserves the previous
output if generation fails. Scheduled refresh commits do not alter `main`.

The contribution graph includes explicitly generated fixtures from the
[contribution visualization lab](https://github.com/ScaraMouche-Wanderer/contribution-visualization-lab).
Those backdated author timestamps are synthetic and do not represent project
work completed on the displayed days. Committer timestamps record generation.

All data comes from the account's public GitHub activity. The language charts
represent repository source composition, not proficiency or hours worked.
Synthetic dashboard demonstrations are distinct from physical hardware results.

The terminal typing animation is a small local SVG and requires no third-party
image service. Light/dark account cards and snake images switch with GitHub's
theme. The 3D calendar and project cards use the profile's dark palette.
