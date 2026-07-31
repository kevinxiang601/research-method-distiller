# Update Workflow

Use this file when the user adds new Zotero papers and asks to update the distiller skill.

## Update Order

1. Read the latest inventory and queue in `refined_indexes`.
2. Identify new or changed papers by Zotero key, DOI, title similarity, PDF path, and PDF hash when available.
3. Prioritize papers close to the user's current direction: supply chain, IO, platform, game theory, empirical identification, OR/data-driven operations, AI/platform governance, and Chinese policy mechanisms.
4. Skip or defer papers that are far from the direction, duplicated, not formal research papers, or lack readable full text.
5. For each accepted paper, produce a full refined deconstruction with eight modules, top-journal writing deconstruction, and idea-formation distillation.
6. Append distilled lessons to the relevant refined indexes.
7. Update `refined_indexes/全量精修排序队列.csv` and `.md`.
8. Update this skill's references only when the new papers add a reusable rule, model family, empirical design, writing move, or evidence category.

## What To Add To The Skill

Add only durable lessons, not paper-by-paper summaries. A new paper should change the skill if it contributes at least one of these:

- a new idea-formation route;
- a new game model family or variant;
- a new empirical identification design;
- a new data construction pattern;
- a new OR/data-driven operations formulation;
- a reusable writing move;
- a boundary condition that prevents overgeneralization.

## What Not To Add

- Do not paste long deconstructions into `SKILL.md`.
- Do not copy full sentences from top-journal papers.
- Do not include weakly related management, entrepreneurship, or psychology papers unless their method clearly transfers to the user's direction.
- Do not treat unreadable/OCR-failed papers as evidence.

## Validation

After edits, run the skill validator and a small evidence search. Check that:

- `SKILL.md` remains concise;
- all referenced files exist;
- `agents/openai.yaml` default prompt mentions `$research-method-distiller`;
- search script can find at least one known topic in the refined indexes;
- stage review still reports the right corpus status.
