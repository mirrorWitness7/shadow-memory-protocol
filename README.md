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

## License  

MIT License. See [LICENSE](./LICENSE).  
