# Empirical Design

Use this file for empirical papers, data construction, causal identification, mechanism tests, and empirical writing plans.

## Design Order

1. Unit: firm, product, listing, transaction, worker, market, dyad, region, user-day, or event.
2. Outcome: innovation, price, quantity, entry, welfare, performance, disclosure, search, matching, retention, or risk.
3. Key X or treatment: policy shock, exposure, platform rule, algorithm adoption, supply-chain risk, data access, tax, regulation, or event.
4. Comparison: treated vs control, high vs low exposure, before vs after, boundary, network exposure, staggered adoption, or randomized assignment.
5. Identification: why the comparison isolates the mechanism rather than selection.
6. Mechanism variables: market gap, collaboration, government support, search cost, information precision, learning, cost pass-through, or behavioral response.
7. Heterogeneity: who is more affected and why.
8. Robustness: alternative measures, placebo, pre-trend, fixed effects, matching, IV, sample restrictions, and alternative windows.
9. Economic magnitude: translate coefficients into meaningful decisions.

## Common Designs From The Refined Papers

- DID/event study: policy or platform shock with exposed and less-exposed units.
- Event study with network exposure: direct and indirect exposure through customers/suppliers.
- Spatial RD: geographic or administrative boundary creates quasi-random treatment intensity.
- IV/control-function: use exogenous variation in costs, distance, policy, historical exposure, or platform adoption.
- Field experiment: randomize information, incentives, interface, algorithmic assistance, or treatment assignment.
- Structural IO: estimate demand, supply, search, matching, or conduct, then run counterfactuals.
- Text-based measures: annual reports, reviews, policy texts, product descriptions, patents, or platform content.
- Mechanism chain: main effect, dynamic effect, robustness, mechanism, heterogeneity, spillover.

## Data Search Heuristics

For China-related supply chain and IO questions, consider:

- listed-firm financials and annual reports;
- customer-supplier relationship data;
- patent data and patent citations;
- customs, input-output tables, product lists, and tariff lists;
- government policy texts, regulatory lists, subsidy lists, pilot programs;
- platform listings, reviews, prices, rankings, sales proxies, or app data;
- geospatial boundaries, station locations, city policies, and region-level indicators.

For platform and AI questions, consider:

- timestamped user behavior;
- seller/product/listing panels;
- algorithm adoption timing;
- platform bans or policy changes;
- reviews, ratings, search positions, ad auctions;
- API restrictions, data-access changes, or model-release dates.

## Empirical Writing Order

Use this sequence unless the paper type demands otherwise:

1. Explain the shock or variation in plain language.
2. Explain why it is plausibly external to the outcome.
3. Define treatment/exposure carefully.
4. State the baseline equation.
5. Explain the identifying assumption.
6. Show pre-trend or balance evidence.
7. Present the main effect.
8. Test mechanisms and heterogeneity.
9. Discuss economic magnitude and managerial meaning.
10. Admit remaining threats.

## Warning Signs

- Treatment is vague and cannot be independently reconstructed.
- Mechanism variables are just additional outcomes with no timing logic.
- Fixed effects are listed but the identifying variation is unclear.
- Robustness tests do not address the main threat.
- The paper claims causality from descriptive or correlational evidence.

## Evidence Pointers

Search `实证方法套路蒸馏.md` for DID, event study, IV, RD, network exposure, structural IO, field experiment, text risk, annual report, patent, platform data, mechanism, heterogeneity, spillover, and policy shock.
