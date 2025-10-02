# Scoring – SMP Demo

This is a **toy** scoring rubric to visualize SMP stability.

## Metrics
- **anchor_recall (0–1)**  
  How often the demo “dropped” anchors that the protocol recognized.
- **stability (0–1)**  
  Ratio of “kept” confirmations vs total corrections. Higher = more stable.
- **drift (0–1)**  
  Inverse proxy of stability/recall. Higher drift = worse SMP.

## Reading the Output
- **anchor_recall ≥ 0.7** → solid anchor discipline.
- **stability ≥ 0.6** → you’re confirming enough; corrections aren’t dominating.
- **drift ≤ 0.3** → reconstruction feels persistent to the user.

## Common Failures
- Too many vague anchors → recall drops, drift rises.
- No corrections → the map never tightens.
- Over-corrections with new terms every time → identity collapses into noise.

> SMP is a **ritual**, not a database. You earn stability through anchor discipline.
