# Pass 1b: Gap-check on sources (2026-09-24)

Follow-up to `01-pedagogy.md`, prompted by "what else got left out, even Wikipedia is useful." Four sources investigated in parallel, each verified from real material, not recall. This file also records what's still *not* covered.

## 1. Learning science — does research actually support friction-first teaching?

Three threads, reconciled:

- **Productive failure (Kapur).** Learners given a hard problem *before* instruction, using only prior knowledge, tie direct instruction on basic recall but significantly beat it on **transfer to novel problems** — provided direct instruction follows the struggle. Kapur's own caveat: not every failure is productive; task design matters.
- **Schwartz & Bransford, "A Time for Telling" (1998).** Having learners analyze contrasting cases first prepares them to *receive* an explanation — it's explicitly not an argument for pure discovery, it's about timing when direct instruction lands.
- **Kirschner, Sweller & Clark (2006).** Minimally-guided instruction underperforms for novices (cognitive-load argument: no schema to hold unguided exploration in working memory), but the guidance advantage recedes as prior knowledge rises. Hmelo-Silver et al.'s 2007 rebuttal argues KSC conflated real, heavily-scaffolded PBL with pure discovery — exchange never resolved to consensus.

**Verdict — this is the load-bearing finding of the whole gap-check:** all three threads agree struggle doesn't work by itself. Kapur's protocol always ends in direct instruction; Schwartz & Bransford's contrasting cases exist to set up telling; KSC's target is guidance-*free* discovery specifically. **The condition the literature actually attaches: friction/struggle works IF it's a tightly scaffolded, well-designed problem (not open-ended exploration) AND is followed by explicit, direct formalization that names what the struggle surfaced.**

**Implication for this project:** every curriculum unit (Pass 4) needs two designed parts, not one — the friction-inducing problem *and* the formalization that follows it. A unit that stops at "now you've felt the pain of array-list insertion" without then explicitly naming and formalizing what linked lists trade away is exactly the failure mode KSC describes. Pass 5's stress-test should check for this explicitly: does every unit have a consolidation step, not just a struggle step?

## 2. Berkeley CS 61B (Josh Hug, Java, free — sp19/fa20)

Order: Intro → references/arrays → **IntList → SLList → DLList → AList** → interfaces (`List61B`) → inheritance → ... → **Asymptotics I/II (lec13/15)**.

Confirmed with a direct quote: IntList (a bare recursive list) is introduced and then explicitly criticized — *"IntLists are hard to use. In order to use an IntList correctly, the programmer must understand and utilize recursion even for simple list related tasks"* — and can't cleanly represent an empty list. SLList fixes this with a **sentinel node**, eliminating null-checks. This is a genuinely concrete, quotable "naive → named limitation → fix" story for the very first data structure a student meets — arguably a better on-ramp than ODS's more abstract interface-first opening.

Two structural differences from Pass 1's other sources, both worth carrying into Pass 2/4:
- **Interfaces come *after* concrete implementations here** (`List61B` is introduced once SLList/AList already exist), the reverse of ODS's interface-first sequencing. Two valid orders exist in the wild, not one.
- **Asymptotic analysis is notably late** (lecture 13/15, after the entire Lists unit and even after inheritance) — sharply later than MIT 6.006 and Princeton, which front-load Big-O before or alongside the first structure.

Not found: any treatment of Java's `Integer[]` vs `int[]` / reference-array cache-locality distinction — the gap flagged against Barker's C-level intuition in `01-pedagogy.md` is not resolved by this source either.

**Verdict:** complementary to ODS, not a replacement. Best used as the *concrete-implementation-first* counterpoint to ODS's *interface-first* structure — likely the better source for the very first lesson (a single naive structure, quotably criticized, immediately fixed), with ODS taking over once the project wants formal interface/cost-table treatment.

## 3. Invention history (Wikipedia + pointers to primary sources)

| Structure | Inventor(s) / year | Motivating problem | Friction framing? |
|---|---|---|---|
| Hash table | Hans Peter Luhn (IBM memo, 1953); Amdahl et al. for IBM 701 | Fast symbol lookup in an assembler | Concrete, but not narrated as "X failed" |
| B-tree | Bayer & McCreight, 1970 (Boeing) | Large ordered indices on slow random-access disk storage; minimize disk reads via high branching factor | **Crispest of the six** — problem stated up front as the reason for the design |
| AVL tree | Adelson-Velsky & Landis, 1962 | First self-balancing BST | Implied by "first," not spelled out as before/after |
| Red-black tree | Bayer (1972, as "symmetric binary B-tree"); reformulated by Guibas & Sedgewick, 1978 | Not "fix a limitation" — **simplify an existing structure** (binary encoding of B-tree's balance guarantees) | Different motivation pattern entirely — worth keeping distinct from "limitation → fix" |
| Linked list | Simon, Newell & Shaw, 1955–56 (RAND, inside IPL) | Early AI programs (Logic Theory Machine, GPS, a chess program) needed to manipulate variable-size symbolic lists; era's fixed-size arrays couldn't | Concrete application-driven origin |
| Binary heap | J.W.J. Williams, 1964 (CACM "Algorithm 232: Heapsort") | Built specifically as heapsort's engine | Clear, stated purpose |

**Verdict:** productive vein, but raw material, not finished narrative — none of the six Wikipedia articles narrate "X failed because Y, so Z" in prose; that framing has to be authored by us from the facts. B-tree, linked list, and binary heap have the strongest primary-source stories. For B-tree and red-black tree specifically, the original papers (Bayer & McCreight 1970; Guibas & Sedgewick 1978) state the motivation better than Wikipedia's summary — worth pulling directly for Pass 4. Knuth's TAOCP Vol. 3 has deeper historical notes on hashing/trees generally.

## 4. Programming Pearls (Jon Bentley), Column 1 "Cracking the Oyster"

Problem (confirmed, corrected from the initial guess): sort up to n ≤ 10,000,000 distinct positive integers, each less than n, using ~1MB of RAM. Naive approaches (load into memory as an array of integers, or a conventional external sort) fail the memory constraint. Solution: a **bit vector** — one bit per possible value — exploits the fact that the range is bounded even though the count of values is too large to hold conventionally. The "800-number" framing is a second illustration of the same idea, not the original motivating example.

This is a clean, explicit instance of the target pattern: problem → naive approach → named bottleneck (memory) → change representation → derive algorithm. The book's broader structure (≈15 columns, e.g. Column 2 "Aha! Algorithms" on binary search / "power of primitives") appears to repeat this device.

**Verdict:** slots into the **problem-solving** layer of the philosophy doc's stack (intuition → implementation → experiment → analysis → formalization → **problem solving** → algorithm design) — it assumes fundamentals are already known and drills the "what's actually happening, what's the bottleneck, what representation fixes it" reasoning directly. Not a substitute for foundational material; a strong fit once that foundation exists.

## Net effect on the project

1. **Pedagogical validity is no longer just assumed.** The friction-first approach has real support, with a specific, non-optional condition attached: struggle must be followed by explicit formalization. This is now a design constraint for Pass 4, not just a stylistic preference.
2. **Two valid orderings for interface-vs-implementation exist** (ODS: interface-first; CS 61B: concrete-first, interface-retrofitted) — Pass 2 should decide per-concept which fits better rather than picking one convention globally. CS 61B's IntList→SLList story is likely the best on-ramp for the very first lesson specifically.
3. **Invention history and Programming Pearls are both real material for Pass 4**, not just color — B-tree/linked-list/heap have strong primary-source origin stories; Pearls Column 1 is a ready-made worked example for the problem-solving layer.
4. **Still open / not chased in this pass:** MIT 6.042 (math background), VisuAlgo (visualization role, still unverified), Kleinberg–Tardos (problem-first algorithm text, skipped by the Erickson fork), Advent of Code/Project Euler/Kattis as "practice without labels" for Pass 5's stress-test, CS:APP's memory-hierarchy chapter, and Barker's own "Memory Management, Explained Simply" series.
