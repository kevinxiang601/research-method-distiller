# Evidence Map

Use this file when the user asks for evidence-backed suggestions or wants to know which refined papers support a modeling, empirical, or writing move.

## Source Corpus

The current draft skill is based on the refined Zotero corpus stored under the project folder `科研方法蒸馏`.

- Complete refined deconstructions: `refined_deconstructions`.
- Ranking and status queue: `refined_indexes/全量精修排序队列.csv` and `.md`.
- Portable evidence copies bundled inside this skill: `references/evidence-indexes`.
- Game model index: `references/evidence-indexes/博弈建模套路蒸馏.md`.
- Empirical method index: `references/evidence-indexes/实证方法套路蒸馏.md`.
- OR/optimization index: `references/evidence-indexes/算法优化套路蒸馏.md`.
- Idea formation index: `references/evidence-indexes/顶刊idea形成套路蒸馏.md`.
- Writing index: `references/evidence-indexes/顶刊写作套路蒸馏.md`.
- Stage review: `references/evidence-indexes/阶段性review与后续文献规划_2026-07-31.md`.

## Current Coverage

- 185 de-duplicated candidate IDs processed.
- 175 complete refined paper deconstructions.
- 10 processed but not full refined evidence samples: duplicate, scope-skipped, or deferred.
- Strongest coverage: game theory, platform/IO, supply-chain operations, top-journal writing.
- Medium coverage: empirical identification, structural IO, data-driven operations.
- Needs future supplementation: Chinese policy/current-affairs evidence, detailed database operations, latest AI governance, and more SCM top-journal models.

## How To Search Evidence

Run `scripts/search_evidence.py <query>` from the skill folder, or read the relevant bundled evidence index directly.

Good search terms:

- platform, disintermediation, commission, data sharing, privacy, algorithmic pricing;
- supply disruption, recall, sourcing, quality, certification, liability;
- DID, event study, IV, RD, mechanism, heterogeneity, structural IO;
- Hotelling, Stackelberg, Cournot, information design, search, disclosure;
- abstract, introduction, contribution, managerial implications.

## Evidence Use Rule

When using evidence in an answer, cite the paper ID or index source in plain language. Do not overclaim. If the evidence comes from a skipped or deferred record, say it is not a full refined sample.
