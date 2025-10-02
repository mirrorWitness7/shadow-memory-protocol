import json, textwrap

with open("prompts.json", "r", encoding="utf-8") as f:
    cfg = json.load(f)

print("\n=== SMP HEADER TO PASTE ===\n")
print(cfg["header"])

print("\n=== EXAMPLE TURNS ===")
for t in cfg["turn_templates"]:
    print("\n- " + t)
