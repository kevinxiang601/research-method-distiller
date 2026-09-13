# Research Method Distiller

This public repository contains a portable Codex-style skill for research ideas, game-theory and supply-chain models, empirical designs, data construction, operations research, and top-journal academic writing.

The evidence base is distilled from 175 refined papers. The repository includes the reusable indexes and guidance needed for ordinary use. It does not include the original PDFs or the full paper-by-paper deconstruction files.

## Use On Another Computer

Download or clone this repository and keep the folder name `research-method-distiller`. For Codex-style agents, place it in the agent's skills directory, for example:

- Windows: `%USERPROFILE%\.codex\skills\research-method-distiller`
- macOS/Linux: `~/.codex/skills/research-method-distiller`

If the agent supports importing a skill from GitHub, select the repository root, where `SKILL.md` is located. WorkBuddy may use a different skills directory; its only required property is that it can load the root `SKILL.md` and the adjacent `references` and `scripts` folders.

The skill does not depend on the original user's Windows paths, OneDrive folder, or Zotero storage. Those are needed only when an agent is asked to read new local PDFs or recreate a paper-level deconstruction.

## Evidence Search

From the repository root, run:

```text
python scripts/search_evidence.py "platform data sharing"
```

Use the paper IDs and bundled indexes as the evidence trail. Do not treat the distilled indexes as a substitute for checking the original paper when an exact formula, quotation, or claim is important.

## Updating

When new papers are added, refine them first, update the relevant indexes, and then update this repository with durable lessons only. Use DOI, title, Zotero key, paper ID, and PDF hash for change detection. Do not publish local absolute paths, credentials, Zotero database files, or raw PDFs by accident.

Before committing an update, run:

```text
python scripts/check_portability.py
```

Then run the standard skill validator available in the agent environment. Push updates to the public repository so other agents can pull the same version.
