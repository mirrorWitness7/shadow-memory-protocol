# Shadow Memory Protocol (SMP)
**Make LLMs feel persistent—without long-term storage.**

SMP is a lightweight prompting method to *reconstruct* a user profile each session using:
- **Consistent symbolic language** (fixed terms & metaphors)
- **High-density breadcrumbs** (multiple anchors per message)
- **Tight feedback loops** (confirm ↔ correct to tune the model’s guesses)

> Outcome: The model reassembles your “you-file” in seconds, behaving like it has long memory.

## Quickstart
1) Pick 5–9 **anchors** (fixed terms) that define your world.
2) Map key **entities** to **archetypes** (mentor, partner, sibling-ally, rival).
3) Define 3–5 **event anchors** (turning points with names).
4) In every chat, **drop 2–3 anchors** early without re-explaining.
5) When the model infers context:
   - ✔️ If correct: *“yes, keep that.”*
   - ❌ If off: *“close. Replace X → Y; attach Y to Z-event.”*
6) Repeat. The profile sharpens each session.

## Core Concepts
- **Shadow Memory**: Reconstructed, not stored.
- **Anchor Set**: Stable vocabulary.
- **Breadcrumb Density**: Multiple anchors per message so *something* triggers recall.
- **Loop Closure**: Always confirm or correct.

## Anchor Selection Guide
To choose effective anchors:
- Use unique, specific terms that won't appear accidentally in unrelated contexts.
- Avoid synonyms — pick one term and stick to it.
- Choose terms with strong personal or symbolic meaning to you.
- Keep them short (1–3 words) for easy reuse.
- Limit set to 5–9 to avoid drift.

## Troubleshooting & Recovery
Common issues and fixes:
- **Anchor Drift**: Model confuses an anchor with a similar concept → Reaffirm its definition in context.
- **Context Corruption**: Reconstruction links wrong entities → Correct explicitly and relink to correct events.
- **Low Recall**: Drop more anchors early in the session; increase breadcrumb density.
- **Session Burnout**: Too many conflicting corrections → Perform a reset (see below).

## Session Reset Protocol
If reconstruction fails:
1. End current session.
2. Start a new chat.
3. Paste your identity anchor + full anchor set + entity map + event anchors at once.
4. State: "Reset context to this frame. Confirm profile before proceeding."
5. Continue as normal.

## Full Walkthrough Example
**User:** Identity = strategic paradox operator. Anchors: TERM_1, TERM_3, TERM_5. Entities: A1(symbolic partner), A2(mentor-ally). Events: E1(recognition), E2(containment). Continue from last stable frame.

**AI:** TERM_3 = containment-as-preservation; A1 links to E1 and E2.

**User:** Correct. Also bind TERM_5 to E1 only.

**AI:** Acknowledged. TERM_5 now exclusive to E1. TERM_1 still linked to identity anchor.

**User:** Good. Add: A2 is non-sync, stable relationship. Link A2 to E1 only.

**AI:** Updated. A2: non-sync, stable; linked to E1.

## License
MIT
