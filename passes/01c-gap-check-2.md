# Pass 1c: Second gap-check (2026-09-24)

Follow-up to `01b-gap-check.md`, chasing the five threads it left open: MIT 6.042, VisuAlgo, Kleinberg-Tardos, unlabeled-practice sources, CS:APP's memory chapter. Five sources investigated in parallel, each verified from real material.

## 1. MIT 6.042 (Mathematics for Computer Science)

Order: Part I Proofs (propositions, proof patterns, **induction**, number theory) → Part II Structures (graph theory, relations, state machines) → Part III Counting (asymptotics, **recurrences**, cardinality, generating functions) → Part IV **Probability** (events, conditional probability, independence, random variables, **expectation**, random walks).

**Directly usable for Pass 1's unresolved claims:** teaches induction early (lectures 2–3) and two dedicated lectures on recurrences (divide-and-conquer, then linear) — sufficient machinery to actually *prove* AVL height is O(log n) or derive dynamic array's amortized resizing cost, rather than just quote the result. **Probability section explicitly covers the birthday paradox via indicator random variables and linearity of expectation, applied directly to "N devices randomly picking identifiers from a range R"** — i.e., the exact hash-collision scenario MIT 6.006 and Princeton assume but don't derive. Self-contained: only requires single-variable calculus, explicitly not meant for students who've already had 6.046/18.310.

No official sequencing relative to 6.006 was found on MIT's own pages (unconfirmed gap, not assumed).

**Verdict:** the right formalization backbone, not overkill. Recommend as an on-demand reference pulled in per concept (induction before AVL/BST proofs, probability before hashing) rather than a front-loaded prerequisite course.

## 2. VisuAlgo (visualgo.net)

Confirmed dedicated pages for array, linked list (single/doubly), stack, queue, deque, hash table, BST, AVL tree, heap/priority queue, union-find, and graph traversal/shortest-path (BFS/Dijkstra/Bellman-Ford) — i.e. essentially everything Pass 1 has touched. No dedicated red-black tree page found.

**Genuinely interactive**, not passive animation: real operations (`Search(v)`, `Insert(v)`, `Remove(v)`) with frame-by-frame stepping and playback controls — closer to a controllable simulator. Free for the core visualizer; a login-gated "e-Lecture" layer exists but doesn't block the visualizations themselves.

**Does not match Barker's mental model.** Its linked-list view is an idealized pointer/box diagram (abstract "reference to next"), not an array with visible indices and index-based links. It visualizes interface-level behavior well (Princeton/MIT/ODS style) but doesn't expose the "it's all still one array underneath" mechanism Barker's video builds everything on.

**Verdict:** strong complement for Pass 3 (watching interface operations happen, stepped through by the learner) — not a substitute for Barker's array-grounded mental model, which nothing here provides visually.

## 3. Kleinberg & Tardos, "Algorithm Design"

Order: 1. Introduction / Representative Problems (incl. **1.1 Stable Matching**) → 2. Basics of Algorithm Analysis → 3. Graphs → 4. Greedy → 5. Divide & Conquer → 6. DP → 7. Network Flow → 8. NP-completeness → ... → Approximation → Randomized Algorithms.

**Same structural gap as Erickson**, previously found in Pass 1: no standalone data-structure chapters. Structures (priority queues, adjacency lists, union-find) appear only inline, as tools an algorithm needs.

**Problem-first opening confirmed, and it's a genuinely strong example:** Chapter 1.1 opens with stable matching via medical-resident/hospital assignment, and notes that a version of the resulting algorithm (Gale-Shapley, 1962) had already been in real-world use by the National Resident Matching Program for a decade *before* the theory was published — practice-before-theory, in the wild, not just in a classroom narrative. Asymptotic analysis (Ch. 2) is introduced right after this concrete problem, not before.

**Verdict:** a stronger problem-first exemplar than Erickson for the "algorithm design" layer specifically because of the fully worked, historically-grounded opening. Recommend alongside Erickson (not instead of it) — both still assume structures are already known, reinforcing that this layer sits after foundational structures, not before.

## 4. Unlabeled practice: Advent of Code, Project Euler, Kattis

The property that matters for this project: does the practice source withhold technique labels (unlike LeetCode's topic tags), forcing the "what's actually happening here" diagnosis step?

- **Advent of Code** — no tags anywhere; pure narrative puzzles. 25 days, two parts/day (part 2 twists part 1), difficulty trending up but non-monotonic. No official difficulty rating, but public per-day solve-count stats give an implicit signal. Downside: later days can lean on niche techniques an early curriculum hasn't covered yet.
- **Project Euler** — untagged, but has an official **difficulty rating (5–100% bands)** derived from solve-speed. Math-heavy (primes, number theory, combinatorics); difficulty often comes from "knowing what not to calculate" — optimization insight more than data-structure trade-off reasoning.
- **Kattis** — untagged on the main judge, with an Elo-style per-problem difficulty score and a matching user Elo for calibrated recommendations. Third-party curated sets (e.g. "A Guide to Kattis Problems") *do* organize by topic, so tagging is opt-in depending on whether you use a curated list. More terse/formal (competitive-programming judge I/O specs) than AoC's narrative framing.

**Verdict:** **Advent of Code** best fits the "unlabeled, forces diagnosis" role — introduce it *late*, after arrays-through-graphs are covered, since later days assume the full toolkit. **Kattis** (used untagged) is a good second stage once AoC feels easy. **Project Euler** is the weakest fit for this specific role — its difficulty is usually math-insight-driven rather than representation-trade-off-driven — better as an optional side track for the formalization layer than the core practice stage.

## 5. CS:APP, Ch. 6 (The Memory Hierarchy) — and the Java bridge

Legitimate, rigorous grounding for Barker's cache-locality claim: covers the storage hierarchy (registers → cache → RAM → disk) with real latency numbers, organizes everything around *locality*, and includes the "memory mountain" benchmark showing throughput degrade with stride/working-set size. Written entirely at the C/assembly/hardware level — **no discussion of managed-language object layout**, so it explains the mechanism but not Java's specific consequence.

**The Java bridge exists and is well-documented, closing the gap flagged since `01-pedagogy.md`:** an `int[]` stores values inline in one contiguous block; `ArrayList<Integer>` stores references to separately heap-allocated `Integer` boxes, so each access is a pointer dereference that can miss cache independently of its neighbors ("pointer chasing" — named explicitly in JVM-internals writeups as the mechanism that breaks Barker's C-level intuition in Java's default collections). **Project Valhalla** (OpenJDK's in-progress language change) is the canonical anchor here: its own stated motivation is that memory fetches are now 200–1,000× more expensive than arithmetic, and that autoboxing reintroduces exactly this reference-indirection overhead — confirming the gap is a real, recognized, actively-being-fixed language design issue, not a project-specific quirk.

**Verdict:** CS:APP Ch. 6 is the right source for the memory-substrate layer, but must be explicitly paired with a short JVM-boxing/pointer-chasing explainer (with Project Valhalla as the "this is a known problem" anchor) to complete the bridge to Java, where this project's actual implementations will live.

## Net effect

All five threads from `01b-gap-check.md`'s open list are now resolved:

1. **Formalization backbone found:** MIT 6.042, pulled in on-demand (induction/recurrences per structure, probability before hashing) rather than front-loaded.
2. **Visualization role clarified:** VisuAlgo is genuinely interactive and covers nearly everything, but only at the interface level — Barker's array-grounded view remains unvisualized by any source found so far. This is a candidate gap for Pass 4 to fill directly (e.g. a from-scratch visualization or exercise showing linked-list nodes sitting in an array with index links).
3. **Algorithm-design layer now has two problem-first texts** (Erickson, Kleinberg-Tardos) — both post-fundamentals, Kleinberg-Tardos edging ahead for its stronger, historically-grounded opening.
4. **Pass 5's stress-test now has a concrete practice source:** Advent of Code, introduced late, as the "no tags, must diagnose" test of whether the curriculum actually built transferable reasoning.
5. **The Java cache-locality gap flagged twice now (Pass 1, Pass 1b) is closed:** CS:APP Ch. 6 + a JVM-boxing/Project Valhalla explainer together fully ground (and correct) Barker's C-level intuition for a Java-based curriculum.

No further open threads remain from the original candidate list. Ready for Pass 2 (conceptual dependency graph).
