# Contributing

Thanks for your interest in improving this research project. Contributions that strengthen the
**educational and defensive** value of this repository are welcome.

## Scope

This project is a **defensive / educational** GNSS security resource. Contributions should keep
that focus. In particular:

- ✅ Improvements to documentation, methodology clarity, diagrams, and references.
- ✅ Better detection and countermeasure material (anti‑spoofing, RAIM/ARAIM, OSNMA, multi‑GNSS).
- ✅ Safer, clearer automation (stronger RF‑isolation safeguards, better validation/error handling).
- ✅ Fixes to commands, parameters, or links.
- ❌ Anything designed to facilitate illegal over‑the‑air transmission or real‑world interference.
- ❌ Instructions for targeting live aircraft, vehicles, ships, or third‑party devices.

All contributors must respect the project's [DISCLAIMER.md](DISCLAIMER.md).

## How to contribute

1. **Fork** the repository and create a feature branch:
   `git checkout -b improve-countermeasures-doc`
2. Make your change. Keep documentation in Markdown and shell scripts POSIX/Bash‑clean.
3. If you touch a script, run `bash -n <script>` (syntax check) and, where possible,
   `shellcheck`.
4. **Commit** with a clear message and **open a pull request** describing the what and why.

## Reporting issues

Open an issue for errors, unclear steps, broken links, or suggestions. Please do **not** open
issues requesting help with illegal or over‑the‑air spoofing — such requests will be closed.
