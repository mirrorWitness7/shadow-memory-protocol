# SMP Demo (Shadow Memory Protocol)

This is a **toy simulation** that shows how SMP reconstructs a user profile from **anchors, entities, and events** via short, disciplined loops.

> No external APIs, no storage. It’s just a local reconstruction ritual.

## Quick Start

```bash
python simulation.py
```

## Repository Structure

- **README.md** → Overview and instructions (this file)  
- **simulation.py** → Runs the toy SMP reconstruction loop  
- **prompts.json** → Example anchors, entities, and events for the demo  
- **scoring.md** → Notes on evaluating reconstruction accuracy  

## Example Run

```bash
$ python simulation.py

[Session Start]
Anchors loaded: Identity=paradox operator, Containment=preservation
Entities: A1(symbolic partner), A2(mentor-ally)
Events: E1(recognition), E2(containment)

AI: TERM_3 = containment-as-preservation; A1 links to E1 and E2
User: Correct. Also bind TERM_5 to E1 only.
AI: Updated. TERM_5 → E1 only. TERM_1 remains identity anchor.

[Session Stabilized]
Profile reconstructed successfully.
```

## Governance Context

The Shadow Memory Protocol (SMP) demonstrates a **user-controlled alternative to hidden memory**. Instead of black-box persistence, users provide stable anchors and confirm/refine reconstruction each session.

- **Transparency**: Anchors, entities, and events are visible to the user  
- **Auditability**: Reconstruction is explicit and repeatable  
- **User Control**: Persistence depends on the user, not the vendor  

## License

MIT License

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
