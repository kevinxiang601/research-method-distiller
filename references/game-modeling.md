# Game And Analytical Modeling

Use this file for game-theory, analytical, platform, supply-chain, IO, information-design, mechanism-design, and behavioral-operation modeling tasks.

## Model-Building Order

1. Real decision: name the actors and their actual decisions.
2. One mechanism: keep only the mechanism that creates the paper's tension.
3. Players: firm, supplier, platform, consumer, regulator, worker, algorithm, or government.
4. Timing: who moves first, who observes what, and when uncertainty resolves.
5. Choices: price, quantity, quality, disclosure, certification, data sharing, capacity, sourcing, entry, effort, commission, allocation, or policy.
6. Information: complete/incomplete information, private type, signal, review, search cost, platform analytics, or data access.
7. Payoffs: profit, utility, welfare, expected cost, reputation loss, liability, carbon cost, waiting cost, or innovation benefit.
8. Equilibrium: backward induction, Nash, Perfect Bayesian, threshold equilibrium, separating/pooling, Markov, or mechanism-design solution.
9. Comparative statics: change one meaningful parameter and connect it to a decision.
10. Managerial implication: who should change what under which condition.

## Reusable Model Families

- Supply-chain Stackelberg: upstream contract or wholesale price first; downstream price/quantity/effort second.
- Dual-channel / encroachment: upstream firm also enters downstream; study cannibalization and channel coordination.
- Platform two-sided market: platform sets commission, access fee, information policy, matching rule, or ad mechanism; users/sellers respond.
- Information disclosure: seller/platform/regulator decides what signal to reveal; consumers update beliefs.
- Search market: consumers or firms search with costs; intermediaries may improve or distort search.
- Dynamic pricing and learning: early decisions create data, inventory, reputation, or strategic consumer responses.
- Behavioral operation: overconfidence, fairness, truth bias, strategic waiting, or algorithm aversion changes standard payoffs.
- Government/market creation: government or platform generates market-enabling resources, but may also distort market discipline.

## KISS Rule

Keep the model as simple as possible while preserving the mechanism. Do not add multiple heterogeneities, multiple stages, and multiple frictions at once unless each is needed to generate the result.

If the result disappears when the extra feature is removed, the feature is structural. If the result survives, the feature is decoration.

## Writing The Model Section

Use this order:

1. State the real-world trade-off in words.
2. Introduce players and timing before equations.
3. Define each symbol when it first appears.
4. Explain why assumptions are stylized but meaningful.
5. Derive equilibrium in a way that reveals intuition, not only algebra.
6. State propositions in plain language before formulas.
7. After each proposition, explain the economic intuition and boundary conditions.

## Model Quality Checks

- Can a reader describe the mechanism without seeing the equations?
- Does each assumption map to a real institutional or operational feature?
- Is there a parameter that clearly represents the new reality?
- Are comparative statics tied to decisions, not just signs?
- Is the main result counterintuitive or decision-changing?
- Is the model too complex for the insight it delivers?

## Evidence Pointers

Search `博弈建模套路蒸馏.md` for model families such as Hotelling, Stackelberg, Cournot, platform, disclosure, certification, privacy, data sharing, search, dynamic pricing, supply disruption, recall, green supply chain, liability, algorithm, and government.
