---
name: research-method-distiller
description: Distill management-science, supply-chain, platform, IO, game-theory, empirical, operations, and top-journal writing methods from refined paper evidence. Use when the user wants to turn a real-world research problem into a publishable idea, build a game-theory or empirical design, find data/identification strategies, imitate top-journal academic English style without copying, or update this skill after new Zotero papers are refined.
---

# Research Method Distiller

## Core Rule

Use this skill as a research-design coach, not as a citation generator. Ground suggestions in the distilled paper evidence when possible, but do not pretend a paper supports a claim if the evidence is missing.

This skill is portable. When it is downloaded on another computer, use the bundled files under `references/evidence-indexes` as the available evidence base. Do not assume that the original OneDrive project, Zotero database, PDF files, or any machine-specific path is available. Use a local Zotero library only when the user explicitly provides access to it.

The target user is a Chinese-speaking management-science / supply-chain / IO PhD-track student. Explain in clear Chinese by default, keep technical terms, and translate the intuition into concrete modeling, data, and writing moves.

## Workflow

1. Identify the user's task type: idea formation, game model, empirical design, OR/data-driven operations, top-journal writing, paper-positioning, or skill update.
2. Read only the relevant reference file(s) below. Avoid loading every reference at once.
3. If the user gives a concrete problem, first restate the real setting in plain Chinese: actors, decisions, information, timing, incentives, and observable traces.
4. Propose 2-3 candidate research angles. For each angle, state the mechanism, closest literature family, minimal model or empirical design, likely data, and why it may or may not be top-journal-worthy.
5. When writing prose, learn rhetorical moves and sentence functions from the reference files, but do not copy full sentences from papers.
6. When uncertain, say what evidence is missing and what Zotero paper group or data source should be added next.

## Reference Routing

- For turning reality into research questions, read `references/idea-formation.md`.
- For analytical, game-theory, platform, supply-chain, or IO models, read `references/game-modeling.md`.
- For empirical models, causal identification, variables, and data sources, read `references/empirical-design.md`.
- For OR, optimization, data-driven operations, learning, and algorithms, read `references/or-optimization.md`.
- For abstract, introduction, literature review, model/method, results, managerial implications, and conclusion writing, read `references/top-journal-writing.md`.
- For finding which refined papers support a claim, read `references/evidence-map.md` and use `scripts/search_evidence.py`.
- For incorporating newly refined Zotero papers into this skill, read `references/update-workflow.md`.
- For installation, portability limits, and updating from another computer, read `references/portability.md`.

## Output Shapes

For idea evaluation, return:

1. research question;
2. real-world tension;
3. closest literature and gap;
4. model path;
5. empirical path;
6. data path;
7. expected contribution;
8. top-journal writing angle;
9. risks and what evidence is missing.

For model building, return:

1. players;
2. timing;
3. choices;
4. information structure;
5. demand/payoff/objective functions;
6. equilibrium concept;
7. comparative statics;
8. managerial implications;
9. how to write the model section.

For empirical design, return:

1. unit of observation;
2. data sources;
3. sample construction;
4. outcome, treatment/key X, mechanisms, moderators;
5. baseline equation;
6. identification assumption;
7. threats;
8. robustness and mechanism tests;
9. writing plan.

## Evidence Discipline

Use the refined indexes as evidence, not as a pile of text to summarize blindly. If a request is close to platform data sharing, search the evidence for data sharing, privacy, platform, information design, and IO. If it is close to supply-chain risk, search for disruption, sourcing, recall, quality, certification, and policy shock.

When the evidence is thin, recommend the next papers to add rather than forcing a confident answer.
