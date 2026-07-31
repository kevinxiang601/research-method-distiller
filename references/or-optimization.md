# OR And Data-Driven Operations

Use this file for operations research, optimization, inventory, scheduling, pricing, learning, algorithms, and data-driven decision tasks.

## Core Translation

Turn the real problem into:

1. state: what is known at decision time;
2. action: what the decision maker controls;
3. uncertainty: demand, arrival, no-show, disruption, service time, learning signal, or censoring;
4. feedback: what is observed after action;
5. objective: cost, profit, regret, waiting, fairness, service level, revenue, or welfare;
6. benchmark: full-information optimum, deterministic approximation, heuristic, current practice, or robust baseline.

## Reusable Families

- Newsvendor and inventory learning: demand is uncertain; stockout creates censored observations.
- Joint pricing and inventory: price changes both demand and inventory risk.
- Appointment and queue scheduling: customers arrive strategically or randomly; waiting, idle time, and overtime trade off.
- Robust optimization: uncertainty set controls protection and conservativeness.
- Contextual learning: features predict demand or response; decision quality matters more than forecast accuracy.
- Platform operations: dispatch, matching, cold start, ad allocation, market thickness, fairness, and long-run retention.

## Research Idea Moves

- Find where current practice uses the wrong proxy metric.
- Find a hidden form of censoring or selection.
- Find a simple rule that practitioners use but theory has not justified.
- Find a new operational constraint created by platforms, AI, carbon policy, or service quality promises.
- Find a setting where optimization has to account for strategic responses.

## Writing Method Sections

1. Describe the operational process before the mathematical program.
2. Define decision epochs, state variables, actions, uncertainty, and costs.
3. Explain why the benchmark is appropriate.
4. State the structural result or algorithm clearly.
5. Translate performance bounds or regret into managerial meaning.
6. Validate with real data, simulation, or counterfactual policy when possible.

## Evidence Pointers

Search `算法优化套路蒸馏.md` and `实证方法套路蒸馏.md` for newsvendor, censored demand, feature-based, appointment, dispatch, contextual bandit, robust optimization, minimax regret, dynamic pricing, and service operations.
