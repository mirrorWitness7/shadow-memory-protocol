import json
from pathlib import Path

class ShadowMemory:
    def __init__(self, identity, anchors, entities, events):
        self.identity = identity
        self.anchors = {a: {"definition": None} for a in anchors}
        self.entities = entities  # dict: name -> {archetype, links}
        self.events = events      # dict: name -> {description, anchors}
        # Metrics
        self.anchor_hits = 0
        self.anchor_misses = 0
        self.corrections = 0
        self.correct_keeps = 0

    def drop_anchors(self, drops):
        # Count how many drops exist in the anchor set
        hits = sum(1 for a in drops if a in self.anchors)
        misses = len(drops) - hits
        self.anchor_hits += hits
        self.anchor_misses += misses
        return f"[anchors: {' '.join(drops)}]"

    def apply_user_correction(self, text):
        """Very simple rule-based updates based on phrases in corrections."""
        self.corrections += 1
        t = text.lower()

        # Update anchor definitions if present
        # patterns like: "Collapse = intentional reset before rebuild."
        if "=" in text:
            parts = [p.strip() for p in text.split(".")]
            for p in parts:
                if "=" in p:
                    lhs, rhs = [x.strip() for x in p.split("=", 1)]
                    if lhs in self.anchors:
                        self.anchors[lhs]["definition"] = rhs

        # Update entity links if text includes "Bind A1 to Collapse and Mirror"
        # Simple heuristic parse:
        for name in list(self.entities.keys()):
            if f"{name.lower()}" in t and ("bind" in t or "link" in t):
                new_links = []
                for a in self.anchors.keys():
                    if a.lower() in t:
                        new_links.append(a)
                if new_links:
                    self.entities[name]["links"] = sorted(set(new_links))

        return "Updated internal map."

    def apply_user_keep(self):
        self.correct_keeps += 1
        return "Kept as is."

    def score(self):
        total_anchor_drops = self.anchor_hits + self.anchor_misses
        anchor_recall = (self.anchor_hits / total_anchor_drops) if total_anchor_drops else 0.0
        # Stability heuristic: more 'keeps' vs corrections → more stable
        stability = self.correct_keeps / max(1, (self.correct_keeps + self.corrections))
        # Panic/drift proxy: many corrections and low recall → higher drift
        drift = 1.0 - min(1.0, (anchor_recall * 0.6 + stability * 0.4))
        return {
            "anchor_recall": round(anchor_recall, 3),
            "stability": round(stability, 3),
            "drift": round(drift, 3),
            "corrections": self.corrections,
            "keeps": self.correct_keeps
        }

def main():
    data = json.loads(Path("prompts.json").read_text(encoding="utf-8"))

    smp = ShadowMemory(
        identity=data["identity"],
        anchors=data["anchors"],
        entities=data["entities"],
        events=data["events"]
    )

    print(f"Identity: {smp.identity}\n")

    for step in data["script"]:
        if "user" in step:
            anchors_to_drop = step.get("drop_anchors", [])
            tag = smp.drop_anchors(anchors_to_drop) if anchors_to_drop else ""
            print(f"USER: {step['user']} {tag}")

        if "ai_guess" in step:
            print(f"AI GUESS: {step['ai_guess']}")

        # If the user says "Correct. Keep."
        corr = step.get("user_correction", "")
        if corr.strip().lower() in ("correct. keep.", "keep.", "correct"):
            print("USER: Correct. Keep.")
            print(smp.apply_user_keep())
        elif corr:
            print(f"USER: {corr}")
            print(smp.apply_user_correction(corr))

        print()

    print("=== FINAL STATE ===")
    print("Anchors:")
    for k, v in smp.anchors.items():
        print(f" - {k}: {v['definition']}")
    print("Entities:")
    for n, e in smp.entities.items():
        print(f" - {n}: archetype={e['archetype']}, links={e['links']}")
    print("Events:")
    for n, e in smp.events.items():
        print(f" - {n}: {e['description']} (anchors={e['anchors']})")
    print()

    print("=== DEMO SCORES ===")
    print(smp.score())

if __name__ == "__main__":
    main()
