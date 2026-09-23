# Pass 3: Resource Mapping

Goal (per `00-philosophy.md`): assign each of Pass 2's 42 concept nodes to the resource best suited for that job — **intuition / formal / implementation / visualization / exercises / problems** — using the mechanism-facet/formal-facet flags already attached to each node. Named structures/algorithms appear here only where a resource's coverage differs by exemplar (e.g. AVL vs. red-black).

## Method and ground rules

Every assignment below rests on what Passes 1/1b/1c actually verified from fetched material, plus one additional batched verification round run for this pass (8 claims, all fetched from real pages — MIT 6.006's full lecture list, CS 61B's later units, VisuAlgo's heap and red-black coverage, and whether Kleinberg-Tardos/Erickson teach exchange argument and reduction as named techniques, not just use them). Nothing below is assigned from recall alone. Where no source in the surveyed set was confirmed to cover a node, that is recorded as a **gap**, not papered over with a plausible-sounding guess — gaps are Pass 4's authoring workload, not a defect in this document.

Two corrections to Pass 2 fell out of this verification round:

1. **The heap-visualization gap is closed, not open.** Pass 2 flagged VisuAlgo as failing to show "it's one array underneath" for the binary heap, by analogy with its idealized linked-list view. Fetching VisuAlgo's heap page directly shows this analogy doesn't hold: it has an explicit toggle between "the visually more intuitive complete binary tree form" and "the compact array based implementation," with the index formulas (`parent(i)=i>>1`, `left(i)=i<<1`, `right(i)=(i<<1)+1`) stated on the page. The linked-list mechanism gap (Pass 1c) is real and stays open; the heap one does not.
2. **The formal-tools track isn't uniformly MIT 6.042.** Pass 2 filed Induction, Exchange argument, Probability/expectation, and Reduction together as "pull in 6.042 on demand." 6.042's confirmed table of contents (Proofs → Structures → Counting → Probability) supports Induction, Probability/expectation, and Ordering relation's total-order axioms — but has no greedy or NP-completeness content. Exchange argument and Reduction are taught, explicitly and by name, in Kleinberg-Tardos (Ch. 4, Ch. 8) and Erickson (Greedy chapter, NP-Hardness chapter) instead.

One item stays genuinely unresolved after a bounded check: no source in the surveyed set was confirmed to teach binary search's connection to the sorted+contiguous invariant as a named lesson (Barker explicitly skips it; VisuAlgo's confirmed page list from Pass 1c doesn't include it; Princeton/6.006's coverage is a TOC-level inference, not fetched). Recorded as a gap below rather than assumed.

Where CS 61B and ODS both cover a node, they're recorded as two different **roles** (concrete-first on-ramp vs. interface-first/cost-table treatment), per 1b's finding that both orderings are pedagogically valid — which comes first is Pass 4's sequencing call, not this pass's.

Any node whose experiment would compare array vs. linked-list performance in Java must pair **CS:APP Ch. 6** with the JVM-boxing/Project Valhalla explainer (`int[]` vs. `Integer[]`) — flagged once here, applies to Contiguity, Indirection, and Sequential vs. Linked representation below.

---

## Layer 0 — Substrate

### Memory as an addressable array
- **intuition:** Barker (the video's entire method opens from "it's all one array")
- **formal/substrate:** CS:APP Ch. 6 — storage hierarchy (registers → cache → RAM → disk) with real latency numbers, organized around locality; the only source in the surveyed set that treats memory itself as an object of study rather than a given
- **visualization:** none confirmed — no source visualizes raw address space directly
- **note:** pairs with the JVM-boxing/Valhalla explainer wherever a Java experiment touches this node

## Layer 1 — Representation & Process Primitives

### Contiguity
- **intuition:** Barker (core intuition — confirmed thesis, "a data structure is a strategy for finding something in an array")
- **formal:** MIT 6.006 (Word-RAM model + asymptotic notation, L1, taught before the first data structure) — primary; Princeton 1.4 Analysis of Algorithms (placed right before the Union-Find case study) — secondary, more example-driven
- **experiment:** CS:APP Ch. 6 + JVM-boxing explainer, if benchmarking in Java

### Indirection
- **intuition:** Barker (the linked-list link in his chain)
- **implementation/on-ramp:** CS 61B (SLList's pointer mechanics, taught via the sentinel-node fix)
- **formal:** ODS Ch. 3 (reference/pointer semantics as part of Linked Lists' interface+cost treatment)
- **experiment:** CS:APP Ch. 6 + JVM-boxing explainer — this node *is* the reason `ArrayList<Integer>` breaks Barker's C-level cache-locality intuition in Java

### Recursive decomposition
- **formal:** Erickson — Recursion chapter exists per confirmed table of contents; depth/framing not independently fetched this pass (unverified beyond TOC)
- **proof tool:** correctness argument comes from Induction (below), not this node itself
- **gap:** no confirmed source gives a clean recursion-*mechanism* explainer. Barker's chain has no recursion treatment at all (explicit gap, Pass 1). CS 61B's IntList uses recursion but frames it as a problem to escape, not a taught mechanism. Pass 4 likely has to author this directly, or repurpose CS 61B's IntList critique despite its negative framing.

### Self-referential structure
- **problem/friction:** CS 61B — IntList → SLList, confirmed and quotable ("IntLists are hard to use... must understand and utilize recursion even for simple list related tasks"), fixed via a sentinel node. Strongest confirmed friction narrative in the entire graph's early layers.
- **implementation:** CS 61B (SLList/DLList) for the on-ramp; ODS Ch. 3 (Linked Lists, Java) for the fuller interface+cost treatment once formalized
- **intuition:** Barker (array's insert/delete cost problem → linked list, confirmed chain link)
- **formal:** ODS

## Layer 2 — Cost & Formal Primitives

### Operation cost as a function of representation
- **intuition:** Barker ("this is Barker's whole method," per Pass 2)
- **formal:** MIT 6.006 (asymptotic notation motivated in L1) + Princeton (1.4, placed immediately before Union-Find)
- **problem:** cross-link only — see Disjoint-set below for the README's own canonical friction narrative (quick-find → quick-union → weighted+path-compressed); not duplicated here

### Invariants
- **gap:** no source in the surveyed set names "invariant" as a formal object of study — 6.042's Part I is proofs/induction generally, not invariants specifically. This node is thin. Pass 4 will likely have to author it explicitly, using Princeton/ODS's implicit "keep it sorted" framing (insertion sort, BST) as the running example rather than pointing at a citable lecture.
- **intuition:** implicit early, no dedicated resource (per Pass 2's own facet note)

### Induction
- **formal:** MIT 6.042 — confirmed, Part I Proofs, lectures 2–3 on induction; explicitly sufficient to prove AVL height is O(log n) and derive the dynamic array's amortized resizing cost
- no intuition slot — pure formal tool (per Pass 2's facet flag)

### Amortized cost
- **problem/intuition:** MIT 6.006 L2 — confirmed, dynamic array explicitly motivated as fixing the fixed array's capacity limit; the "doubling" argument is taught here. **Not Barker** — his chain has no resizing/amortized-cost treatment at all (explicit gap, Pass 1).
- **formal:** MIT 6.042 (recurrences — capable of deriving the actual amortized bound, confirmed)
- reapplied later at hash-table load-factor/resizing (same argument, cross-link, per Pass 2)

## Layer 3 — Abstraction

### Abstract Data Type (interface vs. implementation)
- **formal:** ODS (primary — most explicit statement in the surveyed set: "an interface describes what... an implementation describes how," six interfaces defined up front, confirmed) + MIT 6.006 (secondary — simpler two-interface Sequence/Set framing, confirmed)
- **intuition:** Barker (implicitly ADT-shaped array→better-array progression, per Pass 2's own characterization)
- **sequencing note, not a resource pick:** CS 61B does this in reverse order — concrete implementations first, interface (`List61B`) retrofitted after (confirmed, 1b). A second valid order; which to use where is Pass 4's call.

## Layer 4 — Sequence Representations

### Sequential (contiguous) representation
- **implementation:** ODS Ch. 2 (Array-Based Lists, Java) — primary; CS 61B's `AList` — secondary, confirmed later in its List sequence
- **intuition:** Barker (array → array-list step of his chain)
- exemplar dynamic array: friction = MIT 6.006 L2 (confirmed) + Amortized cost node

### Linked (indirect) representation
- **problem/friction:** CS 61B — IntList → SLList (confirmed, strongest, quotable) — primary
- **implementation:** ODS Ch. 3 (singly/doubly linked, Java, interface+cost) for the formal treatment; CS 61B for the on-ramp
- **intuition:** Barker (array's insert cost → linked list, confirmed chain link)

### Sequence ADT
- **intuition:** Barker — confirmed, "exactly Barker's array→linked-list pivot"
- **formal:** ODS (Queue/Stack/Deque/List interfaces defined up front, confirmed) — primary; MIT 6.006 (Sequence interface across L2/L7) — secondary
- **alternate on-ramp:** CS 61B (concrete-first, interfaces retrofitted — confirmed alternate valid order)
- **visualization:** VisuAlgo — stack, queue, deque pages confirmed to exist (Pass 1c)

## Layer 5 — Ordering, Search, Sort, Hashing

### Ordering relation
- **formal:** MIT 6.042 — Part II Structures covers relations; total-order axioms fit here. (This closes a citation Pass 2 left unnamed.)
- no dedicated intuition resource needed — facet flag says "light, already intuitive"

### Sorted-invariant search
- **correction:** Barker does **not** cover this — confirmed explicit gap ("the video never introduces binary search at all," Pass 1). Do not assign Barker here despite the temptation from adjacency to Contiguity.
- **problem:** Programming Pearls, Column 2 "Aha! Algorithms" — described (Pass 1b) as covering binary search / "power of primitives." Best-fit confirmed problem-solving angle, but this is a title/topic-level confirmation, not a fetched deep-dive — treat as a lead, not a settled citation.
- **formal:** proof of O(log n) via MIT 6.042's divide-and-conquer recurrences (cross-link to Divide & conquer below)
- **gap:** no confirmed VisuAlgo page for binary search specifically (Pass 1c's enumerated list doesn't include it), and no independently-fetched Princeton/6.006/ODS citation for this exact node. Pass 4 should verify directly before building this unit, or write the connective explainer itself (why this doesn't work on a linked list, tying back to the Layer 4 fork).

### Incremental invariant maintenance
- **formal:** MIT 6.006 L3 "Sorting" (confirmed lecture) — primary; Princeton Ch. 2 Sorting (confirmed TOC entry) — secondary
- **implementation:** ODS Ch. 11 Sorting (confirmed TOC entry)
- **gap — no friction source confirmed.** These are usually taught as the first sorting examples without a strong "limitation of the prior thing" story in the surveyed sources; consistent with the AND-rule finding that split them out (they need neither invariants-as-formal-proof nor recursion). Pass 4 may need to author the motivating problem itself.

### Divide & conquer
- **formal:** MIT 6.006 L3 Sorting (confirmed) + MIT 6.042 (recurrences for T(n)=2T(n/2)+O(n), confirmed capability) + Induction (correctness)
- **implementation:** ODS Ch. 11 Sorting; Princeton Ch. 2 (TOC-confirmed to include mergesort/quicksort, not independently deep-fetched)
- cross-link to binary search (same halve-and-recurse shape, per Pass 2) — no separate resource needed

### Comparison lower bound
- **formal only** (no intuition-facet, per Pass 2): MIT 6.006 — decision-tree/adversary argument is standard content adjacent to its confirmed L3–L5 sorting sequence. **Mark unverified at this granularity**: the lecture sequence's existence is confirmed, but whether the Ω(n log n) bound is proved there specifically was not independently fetched.

### Hashing
- **intuition:** Barker — confirmed, "hash map = chaining reuses linked lists inside a second array"
- **formal:** MIT 6.006 L4 Hashing (confirmed) + ODS Ch. 5 Hash Tables (confirmed TOC)
- **problem/history:** invention history — Hans Peter Luhn's 1953 IBM memo, "fast symbol lookup in an assembler" (confirmed, Pass 1b) — a genuine motivating-problem narrative for Pass 4

### Collision resolution
- exemplar **chaining**: intuition = Barker (confirmed — his hashmap explanation is chaining specifically); implementation = ODS Ch. 5 `ChainedHashTable` (confirmed named, Pass 1: "gets O(1) expected find")
- exemplar **open addressing**: **gap** — Barker does not cover open addressing at all (only chaining is confirmed in his transcript). Formal home = ODS/MIT 6.006 (both TOC-confirmed to cover hash tables generally; open-addressing depth not independently verified this pass).

### Load factor / resizing
- same doubling argument as dynamic arrays (Pass 2's own note) — MIT 6.006 (same L2 argument, reapplied) + MIT 6.042 (same recurrence machinery)

### Probability / expectation
- **formal:** MIT 6.042 — confirmed, Part IV Probability, explicit birthday-paradox-via-indicator-random-variables-and-linearity-of-expectation section, applied directly to "N devices randomly picking identifiers from a range R" — i.e. exactly the hash-collision scenario. No intuition-facet.

### Expected-case analysis (hashing)
- **formal:** MIT 6.042's probability machinery (confirmed) applied to Hashing's expected-case results, which MIT 6.006/Princeton state but don't derive (per Pass 1c)

## Layer 6 — Hierarchical Structures

### Hierarchical structure (trees)
- **intuition:** Barker (linked list generalized to multiple children, confirmed chain link)
- **implementation/formal:** ODS Ch. 6 Binary Trees (confirmed TOC) + CS 61B (trees confirmed at ~L16 this pass)
- **visualization:** VisuAlgo — general tree/BST page confirmed to exist

### Sorted invariant over a hierarchical structure (BST)
- **gap:** Barker does not cover BSTs — confirmed explicit gap ("his 'trees' are hierarchies... not search trees... never derives a BST," Pass 1)
- **implementation/formal:** ODS Ch. 6 (binary trees); CS 61B (BSTs confirmed ~L16 this pass)
- **visualization:** VisuAlgo's BST page (confirmed to exist; note AVL content is folded *inside* this same page rather than a separate module — confirmed this pass)

### Balance as an invariant
- exemplar **AVL tree**:
  - **formal/implementation:** MIT 6.006 L6–L7 "Binary Trees / AVL" (confirmed explicit lecture)
  - **problem/friction:** MIT 6.006's own framing — "explicitly framed as fixing unbalanced-BST degradation via AVL balancing" (confirmed, Pass 1) — a strong, directly-usable friction narrative
  - **proof:** MIT 6.042 Induction (confirmed capable of proving AVL height O(log n))
  - **visualization:** VisuAlgo — folded into the BST page, confirmed present this pass
  - **history:** Adelson-Velsky & Landis, 1962, "first self-balancing BST" (confirmed, Pass 1b) — thin narrative, "implied by 'first,' not spelled out as before/after"
- exemplar **red-black tree**:
  - **implementation/formal:** ODS Ch. 9 Red-Black Trees (confirmed) + CS 61B (confirmed ~L18 this pass)
  - **visualization:** **none** — confirmed absence of any VisuAlgo red-black module this pass (not folded into another page either, unlike AVL)
  - **history:** Bayer 1972 ("symmetric binary B-tree"), reformulated by Guibas & Sedgewick 1978 — motivation is "simplify an existing structure," a genuinely different narrative shape than "fix a limitation" (confirmed, Pass 1b) — keep distinct in Pass 4, don't force it into the friction-first template
  - **which resource best explains rotations (Pass 2's open question) — resolved:** ODS Ch. 9's Java rotation code is the concrete answer for red-black; MIT 6.006 doesn't cover red-black at all (its lecture list stops at AVL). So: AVL → 6.006 + VisuAlgo; red-black → ODS + CS 61B, unvisualized.

### Partial-order invariant (heap property)
- **gap:** Barker does not cover heaps at all — confirmed explicit gap, Pass 1
- **formal:** MIT 6.006 L8 Binary Heaps (confirmed)
- **visualization:** VisuAlgo's heap page — confirmed this pass to expose *both* the idealized tree view and the array/index-arithmetic view via an explicit toggle, with the index formulas stated on the page. **This closes the heap-visualization gap Pass 2 flagged as open** (see "Corrections to Pass 2" above).

### Priority Queue ADT
- **formal:** ODS (same "one interface, several implementations" pattern) + MIT 6.006 (heaps, confirmed)
- exemplar **binary heap:** visualization = VisuAlgo (resolved gap, see above); formal/implementation = MIT 6.006 L8 + ODS
- exemplar **unsorted/sorted array:** implementation = ODS (reuses Sequential representation)
- **history:** J.W.J. Williams, 1964, built specifically as heapsort's engine (confirmed, Pass 1b, "clear, stated purpose") — usable friction/history narrative

### Disjoint-set (union-find)
- **problem/friction:** Princeton's own three-act case study (quick-find → quick-union → weighted+path-compressed quick-union) — confirmed, explicit, citable cost-table progression. **This is the README's own canonical friction narrative for the whole curriculum** — the strongest, least-ambiguous resource pick in this entire document.
- **implementation:** Princeton (algs4 code + booksite page, confirmed)
- **visualization:** VisuAlgo — union-find page confirmed to exist (Pass 1c)
- **note:** ODS has no union-find chapter (absence confirmed against its TOC) — don't cite ODS for this node, despite it being the default implementation source elsewhere in this layer

## Layer 7 — Graphs

### Graph (relational structure)
- **intuition:** Barker (tree generalized to multiple parents, confirmed final link of his chain)
- **formal/implementation:** ODS Ch. 12 Graphs (confirmed TOC) + MIT 6.006 (from L9 BFS onward, confirmed) + CS 61B (graphs confirmed ~L23–24 this pass)

### Graph representation fork
- **formal/implementation:** ODS Ch. 12 + MIT 6.006 — both confirmed to cover graph representations generally at the TOC/lecture-list level; adjacency-matrix-vs-list depth specifically was not independently fetched (standard content of any "Graphs" unit, low-risk inference, but flagged for completeness)
- cross-link: this is the same contiguous/indirect fork as Layers 4–5 (Pass 2's own cross-cutting note) — Pass 4 should call this back explicitly rather than re-teach it as new material

### Traversal
- **formal/implementation:** MIT 6.006 L9 BFS + L10 DFS — both confirmed explicit lectures this pass. Strongest, most precise citation available for this node.
- **visualization:** VisuAlgo — graph traversal/BFS/Dijkstra/Bellman-Ford page (confirmed, Pass 1c)
- payoff framing (stack vs. queue determines traversal order, per Pass 2) reuses Sequence ADT's exemplars — no new resource needed

### Weighted relationships
- **formal:** MIT 6.006 L11 "Weighted Shortest Paths" (confirmed explicit lecture this pass) as the entry point

## Layer 8 — Algorithm-Design Paradigms

### Exchange argument
- **formal:** Kleinberg-Tardos Ch. 4 — **primary**. Confirmed this pass (fetched and text-extracted): explicitly names "Exchange argument. Gradually transform any solution to the one found by the greedy algorithm without hurting its quality" as one of three named greedy-analysis strategies.
- **secondary:** Erickson's Greedy chapter — confirmed this pass (12 occurrences of "exchange," a dedicated closing section, applied across tape-storage/scheduling/stable-matching examples) — good for breadth of worked examples once K-T names the technique.
- **correction to Pass 2:** filed under "pull in 6.042 on demand" there; 6.042's confirmed TOC has no greedy content. This tool comes from K-T/Erickson.

### Optimal substructure
- implicit in both K-T's and Erickson's DP/Greedy chapters (TOC-confirmed presence in both) — no single clean citation exists in the surveyed set; treat as a concept introduced in-context by whichever paradigm text is in use, not a standalone lecture (thin — Pass 4 note)

### Greedy paradigm
- **problem:** Kleinberg-Tardos Ch. 1.1 Stable Matching — confirmed, strong, historically grounded: the Gale-Shapley algorithm was in real-world use by the National Resident Matching Program for a decade before the theory was published. Best-fit problem-first opening for this entire paradigm layer.
- **formal:** K-T Ch. 4 (exchange argument, confirmed) — primary; Erickson's Greedy chapter — secondary

### Shortest paths / MST
- **formal/implementation:** MIT 6.006 — the most precise, lecture-level citation in this document: L11 Weighted Shortest Paths, L12 Bellman-Ford, L13 Dijkstra, L14 Johnson's (all confirmed this pass)
- exemplar **Kruskal**: requires Disjoint-set — cite Princeton's union-find (already this graph's canonical resource for that node) as the dependency
- exemplar **Prim/Dijkstra**: no extra requirement beyond the parent (per Pass 2) — MIT 6.006 suffices
- **secondary, for the correctness angle specifically:** K-T Ch. 4 covers MST algorithms as greedy applications (TOC-confirmed) — use this when the question is *why* Prim/Kruskal's greedy choice is safe (Exchange argument), not for the algorithms themselves

### Overlapping subproblems
- **formal:** MIT 6.006 L15 "Dynamic Programming Part 1" — confirmed this pass to open with "recursion, subproblems"
- exemplar naive Fibonacci: standard intro example, implicitly covered by the same lecture — no separate citation needed

### Memoization
- **formal/implementation:** MIT 6.006 L15–L16 (confirmed, DP Parts 1–2)
- exemplar hash-keyed cache: cross-link to Hashing/ODS
- exemplar array-indexed cache: cross-link to Contiguity

### Dynamic programming
- **formal:** MIT 6.006 L15–L18 — the strongest, most granular citation in the whole document (confirmed this pass: four full lecture parts — "recursion, subproblems, APSP/parens/piano, pseudopolynomial." Knapsack maps to the pseudopolynomial lecture; edit distance maps to the parens/piano-style string-DP lecture.)
- **secondary, for breadth:** Kleinberg-Tardos Ch. 6 DP (TOC-confirmed to exist) + Erickson's DP chapter (TOC-confirmed) for additional worked problems
- D&C-vs-DP contrast (Pass 2's own framing) needs no new resource — reuses Divide & conquer + Overlapping subproblems

### Reduction
- **formal:** Kleinberg-Tardos Ch. 8 — **primary**. Confirmed this pass (fetched and text-extracted): titled "Intractability I: Polynomial-Time Reductions," defines Cook reductions, states "reductions classify problems according to relative difficulty" (57 occurrences of "reduc-" in the source text).
- **secondary:** Erickson's NP-Hardness chapter — confirmed this pass (123 occurrences of "reduc-," explicit Turing/Cook vs. many-one/Karp reduction definitions, framed via proof-by-contradiction)
- **correction to Pass 2:** same correction as Exchange argument — this is K-T/Erickson territory, not 6.042.

### NP-completeness / limits of efficient computation
- **formal:** K-T Ch. 8 (confirmed) — primary; Erickson's NP-Hardness chapter (confirmed) — secondary; MIT 6.006 L19 "Complexity" (confirmed this pass: "explicitly covers P/NP/EXP/R, hardness/completeness, reductions") — tertiary
- **note:** MIT 6.006 has no standalone NP-completeness lecture (folds it into general "Complexity," confirmed this pass) and no standalone greedy lecture at all (confirmed absence in its lecture calendar). Don't assume 6.006 carries this layer as deeply as K-T/Erickson do — it's the weaker of the three sources here, useful mainly for connecting back to material already taught in L1–L18.

---

## Cross-cutting jobs (not per-node)

**Exercises (build-it-yourself):** ODS (Java, every chapter has a working implementation to extend) is the default; CS 61B for the earliest, most concrete on-ramp; Princeton's algs4 codebase where experimentation/benchmarking is the point (its stated strength per Pass 1: "rigor, implementation, experimentation, performance").

**Problems (unlabeled, forces diagnosis — Pass 5 territory, not Pass 4):**
- Advent of Code — confirmed best fit (no tags, narrative puzzles); introduce *late*, after arrays-through-graphs are covered (per Pass 1c)
- Kattis, used untagged — confirmed second-stage fit once AoC feels easy
- Project Euler — confirmed weakest fit for this project's specific goal (math-insight-driven, not representation-trade-off-driven); optional side track only
- Programming Pearls Column 1 ("Cracking the Oyster," the bit-vector problem) — confirmed, a ready-made worked example for the "problem-solving" layer once fundamentals exist, distinct from AoC/Kattis in that it's a single fully-narrated example rather than a practice set

None of the above are assigned per-node; inventing a per-concept problem set beyond what's confirmed would recreate exactly the merged-checklist approach `00-philosophy.md` rejects.

---

## Resource-to-role index

| Resource | Primary role(s) in this graph |
|---|---|
| **Nic Barker video** | Intuition/mechanism for Layers 0–6 up through Hashing and Trees (confirmed gaps: no binary search, no BST, no balancing, no heaps, no sorting, no recursion, no amortized cost) |
| **Berkeley CS 61B** | Concrete-first on-ramp (IntList→SLList friction story) and full-course implementation coverage confirmed through BSTs, red-black trees, hashing, heaps, and graphs |
| **Open Data Structures** | Interface-first formal treatment + Java implementation; default for exercises. No AVL chapter, no union-find chapter (confirmed absences) |
| **Princeton (Sedgewick/Wayne)** | Union-find (canonical friction case study), cost-table analysis, experimentation |
| **MIT 6.006** | Formal backbone: asymptotics, dynamic arrays, hashing, AVL, heaps, BFS/DFS, weighted shortest paths, Dijkstra/Bellman-Ford, DP (4 lecture-parts), general Complexity. No standalone greedy or NP-completeness lecture (confirmed) |
| **MIT 6.042** | On-demand formal tools: Induction, Probability/expectation, Ordering-relation axioms, recurrences. **Not** Exchange argument or Reduction (correction to Pass 2) |
| **VisuAlgo** | Visualization: arrays/lists/stack/queue/deque/hash table/BST(+AVL folded in)/heap(array+tree toggle)/union-find/graph traversal. No red-black page, no confirmed binary-search page |
| **Kleinberg-Tardos** | Algorithm-design paradigms: stable matching (greedy problem-first opening), Exchange argument (named), Reduction (named), DP, NP-completeness |
| **Erickson** | Secondary paradigm text: recursion (unverified depth), Exchange argument, Reduction — both confirmed by name, good for breadth |
| **CS:APP Ch. 6 + JVM-boxing/Valhalla explainer** | Required pairing for any Contiguity/Indirection experiment run in Java |
| **Invention history (Wikipedia + primary sources)** | Motivating-problem narratives: hash table (Luhn 1953), AVL (Adelson-Velsky & Landis 1962), red-black (Bayer 1972 / Guibas-Sedgewick 1978 — a "simplify" story, not a "fix" story), linked list (Simon/Newell/Shaw 1955–56), binary heap (Williams 1964) |
| **Programming Pearls** | Problem-solving layer: Column 1 (bit vector) as a worked example; Column 2 as a binary-search lead (unverified depth) |
| **Advent of Code / Kattis / Project Euler** | Pass 5 stress-test practice, introduced late, cross-cutting not per-node |

---

## Gaps carried forward to Pass 4

1. **Invariants** (Layer 2) — no source names this as a formal object of study; author directly.
2. **Recursive decomposition**'s mechanism/intuition — no clean explainer confirmed anywhere in the surveyed set.
3. **Sorted-invariant search (binary search)** — no confirmed formal/visualization source at the needed precision; Pearls Col. 2 is a lead, not a settled citation. Verify directly before building this unit.
4. **Incremental invariant maintenance** (insertion/selection sort) — no confirmed friction narrative.
5. **Open addressing** (collision resolution exemplar) — Barker doesn't cover it; formal depth from ODS/6.006 not independently verified.
6. **Comparison lower bound** — MIT 6.006's coverage confirmed only at the lecture-sequence level, not that the Ω(n log n) proof itself appears there.
7. **Red-black tree** has no visualization anywhere in the surveyed set (confirmed absence, not just unchecked).
8. **Optimal substructure** has no standalone citation — it's taught in-context inside whichever paradigm text is used.

These are authoring gaps, not blockers — Pass 4 should decide, per gap, whether to search further, write the material directly, or accept a thinner treatment for that specific node.
