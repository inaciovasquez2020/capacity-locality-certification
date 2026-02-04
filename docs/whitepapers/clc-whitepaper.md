# Capacity–Locality Certification for Safety-Critical Prediction

## Problem
Safety-critical AI systems often output confident predictions even when the situation is
underdetermined (occlusion, distribution shift, rare events). Improving the model does not
eliminate this failure mode because the limitation is structural: limited information + local view.

## Our contribution
We certify **when a system is allowed to predict** and **when it must abstain**.

Deliverable:
- regime classification (liquid vs frozen),
- mandatory abstention conditions,
- operational safe behavior.

## What clients receive
1) Regime map on their own data streams  
2) Abstention triggers  
3) Certificate format for compliance  
4) Roadmap for reducing frozen-regime frequency

## Why this matters
You can’t certify perfect prediction.
You can certify **when prediction is structurally invalid**.

