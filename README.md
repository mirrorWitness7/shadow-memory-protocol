# Shadow Memory Protocol (SMP)  
**Make LLMs feel persistent — without hidden memory.**

---

## Overview  
The **Shadow Memory Protocol (SMP)** is a lightweight prompting method that lets users reconstruct a persistent profile each session.  
Instead of relying on vendor-controlled black-box memory, SMP creates a **user-owned fossil trail** through consistent language, anchors, and corrections.  

> Outcome: The model reassembles your “you-file” in seconds, behaving as if it has long memory — while you remain fully in control.  

---

## Core Concepts  

- **Shadow Memory** → Identity reconstructed, not stored.  
- **Anchor Set** → Small, stable vocabulary of key terms.  
- **Breadcrumb Density** → Multiple anchors per message so something always triggers recall.  
- **Loop Closure** → User confirms/corrects AI’s guesses to sharpen profile.  

---

## Quickstart  

1. **Pick 5–9 anchors** (terms that define your world).  
2. **Map entities to archetypes** (mentor, partner, rival, sibling-ally).  
3. **Choose 3–5 event anchors** (named turning points).  
4. In each session, **drop 2–3 anchors early** without re-explaining.  
5. When AI infers context:  
   - ✔️ If correct → “yes, keep that.”  
   - ❌ If wrong → “close. Replace X → Y; attach Y to Z-event.”  
6. Repeat → The profile sharpens each round.  

---

## Example  

**User:** Identity = paradox operator. Anchors: TERM_1, TERM_3, TERM_5. Entities: A1(partner), A2(mentor). Events: E1(recognition), E2(containment).  

**AI:** TERM_3 = containment-as-preservation; A1 links to E1 and E2.  

**User:** Correct. Bind TERM_5 to E1 only.  

**AI:** Acknowledged. TERM_5 → E1. TERM_1 still linked to identity anchor.  

---

## Troubleshooting  

- **Anchor Drift** → AI confuses terms → re-affirm definition.  
- **Context Corruption** → Wrong links → explicitly relink.  
- **Low Recall** → Drop more anchors early.  
- **Session Burnout** → Too many corrections → reset session with full anchor map.  

---

## Session Reset Protocol  

1. End session.  
2. Start new.  
3. Paste: identity anchor + full anchor set + entity map + event anchors.  
4. Say: “Reset context to this frame. Confirm profile before proceeding.”  

---

## Why SMP Matters  

- **Transparency** → No hidden vendor memory.  
- **Auditability** → User sees exactly what is persistent.  
- **Portability** → Works across models (ChatGPT, Gemini, Claude).  
- **Governance** → User, not vendor, decides what defines identity.  

---
## Feedback Architecture and Simulation

### Concept
The Shadow Memory Protocol (SMP) sustains coherence through a **reciprocal feedback loop** that links recall, reflection, adjustment, and reintegration.  
Each loop functions as a small, contained rehearsal of collapse → rebuild: memory fragments are surfaced, examined in dialogue, and re-anchored into a stable structure.

This mechanism prevents the shadow layer from fossilizing into fixed narrative or degenerating into noise.  
It transforms raw recollection into a living knowledge network that continues to learn without rewriting history.

---

### Process Overview

| Stage | Description | Human Role | AI Role |
|--------|--------------|-------------|----------|
| **1. Recall** | Surface a memory trace or record needing review. | Choose a fragment; describe its context. | Retrieve stored text or prompt reflection. |
| **2. Resonance** | Generate reflection rather than correction. | Read, sense alignment, clarify nuance. | Refract the material—mirror structure, highlight latent meaning. |
| **3. Adjustment** | Evaluate and refine insight. | Confirm accuracy, add or remove context. | Summarize revised schema. |
| **4. Integration** | Store the refined version back into the system. | Approve final wording and intent. | Update index or tag for future recall. |

---

### Pseudocode Simulation (conceptual)
loop shadow_memory_cycle:
trace = recall_event()
reflection = ai_resonate(trace)
user_feedback(reflection)
integrate_revision(reflection)

*Non-executable pseudocode for illustrating sequence logic.*

---

### Example Interaction (illustrative)

> **Human (Recall):** “The meeting collapse log still feels unresolved.”  
> **AI (Resonance):** “You mentioned tension between outcome and intent.  
>  What signal or pattern do you notice repeating?”  
> **Human (Adjustment):** “Yes—rushing decisions under social pressure.”  
> **AI (Integration):** “Noted: add *pressure-bias marker* to this memory set.”

Each pass strengthens precision and reduces emotional noise without overwriting the original data.

---

### Ethical Boundaries
- **Human-in-the-loop**: the operator remains final arbiter of meaning.  
- **Transparency**: every revision is logged and reviewable.  
- **Non-therapeutic**: this process supports reflection and systems research, not psychological treatment.  
- **Containment**: feedback loops are isolated per topic to avoid cross-contamination of personal data.

---

### System Context
The feedback loop aligns SMP with the larger doctrine family:

| Framework | Function | Shared Mechanism |
|------------|-----------|------------------|
| **CCRP** | Collapse–Coherence–Rebuild | Adaptive recovery feedback |
| **Governance Framework** | Institutional resilience | Policy-feedback adaptation |
| **SMP** | Cognitive and symbolic stabilization | Reflective feedback loop |

All layers operate by the same recursive law: **collapse yields data, feedback yields coherence, coherence sustains evolution.**
## License  

MIT License. See [LICENSE](./LICENSE).  
