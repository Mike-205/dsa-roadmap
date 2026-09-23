#!/usr/bin/env python3
"""
Verifies passes/04-curriculum.md's milestone sequencing against passes/02-dependency-graph.md's
actual dependency graph -- parsed from both files on disk, not a hand-transcribed copy.

Checks:
  1. Every node heading in 02 is placed in exactly one milestone in 04.
  2. Every requires: edge in 02 resolves at the same milestone or an earlier one.
  3. (Manually curated, see EXEMPLAR_EXTRAS below) every exemplar-level extra requirement
     resolves at the same milestone or an earlier one.

Node-level requires: edges (check 2) are parsed directly from 02's "- **requires:** ..."
lines, which are flat comma-separated lists in the source and safe to split directly.
Exemplar-level extras (check 3) are stated in free-form prose under 02's "**exemplars:**"
lines, in a "name (+ Requirement)" shape that varies too much to regex reliably -- they are
NOT machine-parsed here. They're transcribed by hand into EXEMPLAR_EXTRAS below, each keyed
by a label naming the parent node it was transcribed from, so a reviewer can go back to that
node's "**exemplars:**" line in 02-dependency-graph.md and spot-check the transcription.
"""
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
PASS2 = ROOT / "passes" / "02-dependency-graph.md"
PASS4 = ROOT / "passes" / "04-curriculum.md"

# Manually curated from 02's "**exemplars:**" prose (each entry cites its source line's node).
# label -> (parent node heading in 02, [extra requirement node headings])
EXEMPLAR_EXTRAS = {
    "dynamic array (exemplar of Sequential (contiguous) representation)":
        ("Sequential (contiguous) representation", ["Amortized cost"]),
    "chaining (exemplar of Collision resolution)":
        ("Collision resolution", ["Linked (indirect) representation"]),
    "open addressing (exemplar of Collision resolution)":
        ("Collision resolution", ["Sequential (contiguous) representation"]),
    "binary heap (exemplar of Priority Queue ADT)":
        ("Priority Queue ADT", ["Partial-order invariant (heap property)", "Contiguity"]),
    "Kruskal (exemplar of Shortest paths / MST)":
        ("Shortest paths / MST", ["Disjoint-set (union-find)"]),
    "hash-keyed cache (exemplar of Memoization)":
        ("Memoization", ["Hashing"]),
    "array-backed exemplar of Sequence ADT":
        ("Sequence ADT", ["Sequential (contiguous) representation"]),
    "linked-backed exemplar of Sequence ADT":
        ("Sequence ADT", ["Linked (indirect) representation"]),
    "merge sort / quicksort (exemplars of Divide & conquer)":
        ("Divide & conquer", ["Ordering relation"]),
    "unsorted array (exemplar of Priority Queue ADT)":
        ("Priority Queue ADT", ["Sequential (contiguous) representation"]),
    "sorted array (exemplar of Priority Queue ADT)":
        ("Priority Queue ADT", ["Sequential (contiguous) representation"]),
    "adjacency matrix (exemplar of Graph representation fork)":
        ("Graph representation fork", ["Contiguity"]),
    "adjacency list (exemplar of Graph representation fork)":
        ("Graph representation fork", ["Indirection"]),
}


def parse_pass2(text):
    """Returns {node_heading: [requires...]} parsed from 02's ### headings and requires: lines."""
    nodes = {}
    # Split on '### ' headings (Layer 0 substrate heading etc. are '## Layer N' -- skip those)
    heading_positions = [m.start() for m in re.finditer(r"^### (.+)$", text, re.MULTILINE)]
    headings = re.findall(r"^### (.+)$", text, re.MULTILINE)
    heading_positions.append(len(text))
    for i, name in enumerate(headings):
        name = name.strip()
        block = text[heading_positions[i]:heading_positions[i + 1]]
        m = re.search(r"\*\*requires:\*\*\s*(.+)", block)
        if not m:
            nodes[name] = []
            continue
        req_line = m.group(1).strip()
        if req_line in ("—", "-", ""):
            nodes[name] = []
        else:
            nodes[name] = [r.strip() for r in req_line.split(",")]
    return nodes


def parse_pass4(text):
    """Returns {node_heading: milestone_number} by checking, for each 02 node name, which
    milestone's **Nodes:** line contains it as a substring (robust to embedded parens like
    "(contiguous)" or appended "(exemplars: ...)" suffixes that a naive comma-split would choke on).
    Raises via the caller-visible `duplicate_errors` list (not just a printed warning) if any
    node's name matches more than one milestone's **Nodes:** line -- "exactly once" is enforced,
    not just checked for absence."""
    milestone_blocks = []
    for m in re.finditer(r"^## (M\d+) — .+$", text, re.MULTILINE):
        milestone_blocks.append((int(m.group(1)[1:]), m.start()))
    milestone_blocks.append((None, len(text)))

    placements = {}
    duplicate_errors = []
    for i in range(len(milestone_blocks) - 1):
        mnum, start = milestone_blocks[i]
        _, end = milestone_blocks[i + 1]
        block = text[start:end]
        nodes_line_match = re.search(r"\*\*Nodes:\*\*\s*(.+)", block)
        nodes_line = nodes_line_match.group(1) if nodes_line_match else ""
        for node_name in ALL_NODE_NAMES:
            short_form = re.sub(r"\s*\([^)]*\)\s*$", "", node_name).strip()
            if node_name in nodes_line or (short_form and short_form in nodes_line):
                if node_name in placements:
                    duplicate_errors.append(
                        f"'{node_name}' appears in >1 milestone's **Nodes:** line "
                        f"(M{placements[node_name]} and M{mnum}) -- not placed exactly once")
                placements[node_name] = mnum
    return placements, duplicate_errors


pass2_text = PASS2.read_text()
pass4_text = PASS4.read_text()

nodes = parse_pass2(pass2_text)
ALL_NODE_NAMES = list(nodes.keys())  # used by parse_pass4 via closure below
milestone, duplicate_errors = parse_pass4(pass4_text)

# 02's own requires: lines sometimes reference a node by a short form of its full heading
# (e.g. heading "Abstract Data Type (interface vs. implementation)" is referred to elsewhere
# simply as "Abstract Data Type"). Build an alias index so short-form references resolve to
# the canonical heading instead of failing to match.
def canonicalize(name, canonical_names):
    if name in canonical_names:
        return name
    stripped = re.sub(r"\s*\([^)]*\)\s*$", "", name).strip()
    for full in canonical_names:
        if full == name or re.sub(r"\s*\([^)]*\)\s*$", "", full).strip() == stripped:
            return full
    return name  # unresolved -- will surface as a real error below

canonical_names = set(nodes.keys())
nodes = {k: [canonicalize(r, canonical_names) for r in v] for k, v in nodes.items()}
milestone = {canonicalize(k, canonical_names): v for k, v in milestone.items()}

errors = list(duplicate_errors)

if len(nodes) != 42:
    errors.append(f"Expected 42 nodes parsed from 02, found {len(nodes)}: {sorted(nodes)}")

missing = [n for n in nodes if n not in milestone]
if missing:
    errors.append(f"Nodes from 02 not found placed in any 04 milestone: {missing}")

for node, reqs in nodes.items():
    if node not in milestone:
        continue
    m = milestone[node]
    for r in reqs:
        if r not in milestone:
            errors.append(f"{node}: requirement '{r}' not found placed in any milestone")
        elif milestone[r] > m:
            errors.append(f"{node} (M{m}) requires {r} (M{milestone[r]}) -- FORWARD REFERENCE")

for label, (parent, extras) in EXEMPLAR_EXTRAS.items():
    parent = canonicalize(parent, canonical_names)
    if parent not in milestone:
        errors.append(f"Exemplar extra '{label}': parent node '{parent}' not placed")
        continue
    m = milestone[parent]
    for r in extras:
        r = canonicalize(r, canonical_names)
        if r not in milestone:
            errors.append(f"Exemplar extra '{label}': requirement '{r}' not placed")
        elif milestone[r] > m:
            errors.append(f"{label} at M{m} needs {r} (M{milestone[r]}) -- FORWARD REFERENCE")

print(f"Parsed {len(nodes)} nodes from 02-dependency-graph.md")
print(f"Placed {len(milestone)} nodes across milestones M0..M{max(milestone.values()) if milestone else '?'}")
print(f"Checked {len(EXEMPLAR_EXTRAS)} manually-curated exemplar-extra edges")

if errors:
    print(f"\n{len(errors)} ERROR(S):")
    for e in errors:
        print(" -", e)
    sys.exit(1)
else:
    print("\nALL CHECKS PASSED.")
