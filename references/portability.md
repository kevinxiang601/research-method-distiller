# Portability and Maintenance

## What Travels With The Skill

The repository is a self-contained research-method coach built around the distilled evidence indexes in `references/evidence-indexes`. It does not need the original Windows account, OneDrive folder, Zotero database, or PDF storage directory for ordinary idea, modeling, empirical-design, or writing requests.

The stable evidence identifiers are paper IDs such as `P0002`, titles, DOIs, and the index filenames. These identifiers should be used when referring to evidence across computers and agents.

## Download And Use

Keep the repository folder name `research-method-distiller` and make sure the root contains `SKILL.md`. A Codex-style installation normally places the folder at `~/.codex/skills/research-method-distiller` on macOS/Linux or `%USERPROFILE%\.codex\skills\research-method-distiller` on Windows. Platforms that support importing a skill directly from GitHub can select the repository root instead.

The exact skill directory for WorkBuddy or another agent may differ. The portable requirement is the same: the agent must see the root `SKILL.md`, `agents/openai.yaml` when supported, the `references` folder, and the `scripts` folder.

## Evidence Boundary

The repository contains distilled indexes rather than the original PDFs and the 175 paper-level deconstruction files. Therefore:

- Existing distilled lessons can be used directly after download.
- Paper-level quotations, formula checks, or a new full deconstruction require the PDF or the relevant full deconstruction to be supplied to the agent.
- A new Zotero library can be used as an external input, but it is not assumed to exist at any fixed path.

## Updating From Another Computer

1. Pull or download the latest public repository.
2. Add only durable lessons to the relevant reference index and keep the `SKILL.md` router concise.
3. Identify papers with paper ID, DOI, title, Zotero key, and PDF hash when available.
4. Do not publish local absolute paths, credentials, database files, or raw PDFs unless separately intended.
5. Run `python scripts/check_portability.py` and the skill validator before committing.
6. Commit and push to the same repository so other agents can pull the updated version.

The repository is the portable skill source. Local project drafts and local Zotero paths are supporting workspaces, not dependencies of the downloaded skill.
