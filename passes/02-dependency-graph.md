# Pass 2: The Conceptual Dependency Graph

Goal (per `00-philosophy.md`): strip course names and named data structures/algorithms out of the organizing role, and find the underlying ideas — memory, representation, operations, cost, abstraction, invariants, recursion, ordering, search, relationships, optimization — and their actual prerequisite relationships. Named structures and algorithms appear here only as **exemplars** attached to the idea they instantiate; which resource teaches which exemplar is Pass 3's job, not this one.

## Schema

Each node has:

- **requires:** other nodes in this document, and only other nodes in this document (no vague references, no "OR" — see "How this was built" below).
- **exemplars:** (where applicable) named structures/algorithms that instantiate the idea. An exemplar may carry its own extra requirement beyond the node's shared floor.
- **mechanism-facet / formal-facet:** whether the concept has a distinct intuitive/mechanical explanation (Barker-style) and/or a distinct formal treatment (interface/cost-table/proof). Most nodes have both; a few lean on one side. This flags, but does not fill, Pass 3's resource-mapping slots.

## How this was built

Two rules were enforced throughout, both surfaced by adversarial review while drafting:

1. **The AND-rule.** `requires:` is a conjunction: everything listed must be true for the node to make sense, and it must hold for *every* exemplar under that node, not just some. If exemplars need different things, the parent's `requires:` is only the shared floor, and each exemplar carries its own extra requirement. A node's `requires:` may never contain "OR" — if a concept can be satisfied two different ways (e.g. a cache backed by an array or a hash map), that's two exemplars with two different extra requirements, not one requirement with a fork in it.
2. **No dangling edges.** Every name inside a `requires:` list must be the heading of another node in this document. Vague requirements ("cost analysis," "broad exposure," "a way to hold state") were replaced with the actual node they meant, adding a node where none existed yet (this produced the formal-tools track below).

Applying these caught real errors, not just style issues: a "sorting" node that falsely required both invariants and recursion for every sort (insertion sort needs neither), a Priority Queue node that required the heap property even though its own unsorted-array and sorted-array exemplars don't use a heap, a "recursion" node that required indirection even though array-based recursion (merge sort, divide & conquer, DP) needs none, and a "DP requires optimal substructure" edge that broke on its own canonical intro exemplar (naive Fibonacci has overlapping subproblems, not an optimization objective).

---

## Layer 0 — Substrate

### Memory as an addressable array
The root node. A flat sequence of addressable cells; nothing below has meaning without it.
- **requires:** —
- **mechanism-facet:** yes (the physical/OS model). **formal-facet:** minimal — closer to a given than a derived result.

## Layer 1 — Representation & Process Primitives

### Contiguity
Laying data sequentially in memory.
- **requires:** Memory as an addressable array
- **unlocks:** O(1) indexed access via address arithmetic, cache locality
- **mechanism-facet:** yes (Barker's core intuition). **formal-facet:** yes (becomes a cost-table entry).

### Indirection
Storing an address instead of a value.
- **requires:** Memory as an addressable array
- **unlocks:** linking non-contiguous data, dynamic shape; costs a dereference and breaks locality
- **mechanism-facet:** yes. **formal-facet:** yes (pointer/reference semantics, aliasing).

### Recursive decomposition
A process defined by solving a smaller instance of the same problem and combining results. Deliberately has **no structural requirement** — it applies equally to array-based algorithms (merge sort) as to pointer-based structures, which is exactly why it was split out of the older combined "recursion" node.
- **requires:** —
- **mechanism-facet:** yes (unwind-the-box intuition). **formal-facet:** yes, via Induction (below).

### Self-referential structure
A *structure* (not just a process) defined in terms of a smaller instance of itself — a node that can point to another node of its own type.
- **requires:** Recursive decomposition, Indirection
- **unlocks:** linked representation, trees — one of the highest-fan-out nodes in the graph
- **mechanism-facet:** yes. **formal-facet:** yes.

## Layer 2 — Cost & Formal Primitives

### Operation cost as a function of representation
The general principle that how data is laid out determines which operations are cheap or expensive. Needs at least two representations in view to be motivated at all.
- **requires:** Contiguity, Indirection
- **mechanism-facet:** yes (this is Barker's whole method). **formal-facet:** yes — this is where asymptotic notation (Big-O/Θ/Ω) gets introduced, motivated rather than dropped in cold.

### Invariants
A property a structure promises to maintain across operations.
- **requires:** Operation cost as a function of representation
- **mechanism-facet:** implicit early ("keep it sorted"). **formal-facet:** yes — becomes a proof obligation later (loop invariants, structural invariants).

### Induction
The proof technique underlying recursive correctness and complexity arguments. Formal tool, pulled in on-demand (per Pass 1c: MIT 6.042), not front-loaded.
- **requires:** Recursive decomposition
- **formal-facet:** yes. **mechanism-facet:** no (this is a pure formal tool).

### Amortized cost
Accounting for occasional expensive operations (e.g. resizing) by spreading their cost across many cheap ones.
- **requires:** Operation cost as a function of representation
- **mechanism-facet:** yes (the "doubling" argument is intuitive). **formal-facet:** yes.

## Layer 3 — Abstraction

### Abstract Data Type (interface vs. implementation)
Specifying *what* operations exist and their contracts, separate from *how* they're implemented — motivated only once at least two implementations have shown different cost tradeoffs.
- **requires:** Operation cost as a function of representation
- **mechanism-facet:** yes (Barker's array→better-array progression is implicitly ADT-shaped). **formal-facet:** yes (Princeton/ODS's explicit framing).

## Layer 4 — Sequence Representations

### Sequential (contiguous) representation
- **requires:** Contiguity, Abstract Data Type
- **exemplars:** fixed array (no extra requirement); dynamic array (+ Amortized cost, for resizing)

### Linked (indirect) representation
- **requires:** Self-referential structure
- **exemplars:** singly linked node, doubly linked node

### Sequence ADT
An interface (push/pop/access) that can be implemented over either representation family above — this is the fork point, presented as two answers to the same question rather than unrelated topics.
- **requires:** Abstract Data Type
- **exemplars:** array-backed sequence (+ Sequential representation); linked-backed sequence (+ Linked representation)
- **note:** access-pattern restrictions (stack = LIFO, queue = FIFO, deque = both ends) are a policy layered on top of *either* backing, not a separate representational branch — worth teaching as "same interface, an added discipline," reusing the ADT idea a second time.
- **mechanism-facet:** yes (this is exactly Barker's array→linked-list pivot, and CS 61B's IntList→SLList). **formal-facet:** yes (cost tables, side by side).

## Layer 5 — Ordering, Search, Sort, Hashing

### Ordering relation
A total order over elements. Structurally independent of everything above — doesn't require contiguity or indirection — but is what makes the next several nodes possible.
- **requires:** —
- **mechanism-facet:** light (already intuitive). **formal-facet:** yes (total order axioms; matters later for sort stability and BST correctness).

### Sorted-invariant search
Sortedness plus random access lets you halve the search space.
- **requires:** Ordering relation, Contiguity
- **exemplars:** binary search
- **note:** this is *why* binary search doesn't work on a plain linked list — a direct callback to the Layer 4 fork.

### Incremental invariant maintenance
Building a result by maintaining an invariant (e.g. "the prefix is sorted") one element at a time.
- **requires:** Invariants
- **exemplars:** insertion sort, selection sort
- **note:** these do **not** require recursion — the AND-rule check that split this out of a single "sorting" node.

### Divide & conquer
- **requires:** Recursive decomposition, Induction
- **exemplars:** merge sort (+ Ordering relation), quicksort (+ Ordering relation)
- **note:** binary search is arguably an instance of this too (halve, recurse) — cross-linked to Sorted-invariant search rather than duplicated, since both lenses are pedagogically valid.

### Comparison lower bound
The Ω(n log n) bound on comparison-based sorting — the one idea genuinely specific to sorting rather than borrowed from elsewhere.
- **requires:** Ordering relation, Operation cost as a function of representation
- **formal-facet:** yes (decision-tree/adversary counting argument). **mechanism-facet:** no.

### Hashing
Computing an address from a key — a generalization of direct addressing.
- **requires:** Contiguity
- **unlocks:** Collision resolution

### Collision resolution
- **requires:** Hashing
- **exemplars:** chaining (+ Linked (indirect) representation); open addressing (+ Sequential (contiguous) representation, via a probing sequence)

### Load factor / resizing
- **requires:** Amortized cost
- **note:** the same doubling argument as dynamic arrays, reapplied to hash tables.

### Probability / expectation
Formal tool (linearity of expectation, birthday-paradox-style counting), pulled in on-demand per Pass 1c (MIT 6.042).
- **requires:** —
- **formal-facet:** yes. **mechanism-facet:** no.

### Expected-case analysis (hashing)
- **requires:** Hashing, Probability / expectation
- **note:** a different flavor of formal tool than everything above it in this layer — probabilistic rather than purely combinatorial, worth flagging explicitly rather than treating as "more Big-O."

## Layer 6 — Hierarchical Structures

### Hierarchical structure (trees)
A node with multiple children, each child's subtree itself the same structure.
- **requires:** Self-referential structure
- **exemplars:** general tree, binary tree (a representational restriction, not a separate idea)

### Sorted invariant over a hierarchical structure (BST)
The same sorted-invariant idea as Sorted-invariant search, reapplied over a recursive/pointer-based representation instead of a contiguous one.
- **requires:** Hierarchical structure (trees), Ordering relation
- **note:** cross-link to Sorted-invariant search — same invariant, different representation, same fork-point pattern as Layer 4.

### Balance as an invariant
Without it, a BST built from adversarial insertion order degrades to a linked list, erasing the point of the sorted invariant.
- **requires:** Sorted invariant over a hierarchical structure (BST), Operation cost as a function of representation, Induction
- **exemplars:** AVL tree, red-black tree — which resource best explains rotations is a Pass 3 question, not this one.

### Partial-order invariant (heap property)
Parent ≤ (or ≥) children only — weaker than BST's total-order invariant. Worth flagging explicitly: a heap is *not* a sorted structure, a common confusion point.
- **requires:** Hierarchical structure (trees), Ordering relation

### Priority Queue ADT
- **requires:** Abstract Data Type, Ordering relation
- **exemplars:** unsorted array (+ Sequential (contiguous) representation); sorted array (+ Sequential (contiguous) representation); binary heap (+ Partial-order invariant (heap property), + Contiguity — the heap is a tree stored in an array via index arithmetic)
- **note:** same "one interface, several cost-tradeoff implementations" pattern as Layers 4 and 5, recurring at a new layer. The array-backed heap is also the clearest concrete case of the "it's all one array underneath" gap the README flags as still open for Pass 4.

### Disjoint-set (union-find)
- **requires:** Self-referential structure, Operation cost as a function of representation
- **exemplars, in order:** quick-find → quick-union → weighted + path-compressed quick-union
- **note:** README's own key finding from Pass 1 uses this progression (Princeton's) as *the* canonical example of the friction-driven teaching pattern this whole curriculum is built on — leaving it out of the graph would be a visible hole.

## Layer 7 — Graphs

### Graph (relational structure)
- **requires:** Indirection
- **note:** a tree is a graph with acyclic + connected + rooted constraints added. That's a true statement, but it's a *sequencing* observation (trees are pedagogically easier to introduce first), not a hard prerequisite — someone could learn adjacency lists and BFS without ever having seen a tree. Kept as a cross-link and a Pass 4 sequencing note rather than a `requires:` edge, per the AND-rule.

### Graph representation fork
- **requires:** Graph (relational structure)
- **exemplars:** adjacency matrix (+ Contiguity); adjacency list (+ Indirection)
- **note:** this is the Layer-1 contiguous/indirect fork recurring at a new scale — see "Recurring patterns" below.

### Traversal
- **requires:** Graph representation fork, Sequence ADT
- **exemplars:** DFS (using the stack/LIFO exemplar of Sequence ADT); BFS (using the queue/FIFO exemplar)
- **note:** a genuine payoff node — it shows that stack vs. queue isn't arbitrary trivia, it *determines* traversal order.

### Weighted relationships
- **requires:** Ordering relation, Graph representation fork

## Layer 8 — Algorithm-Design Paradigms

### Exchange argument
Formal tool: showing a locally optimal choice doesn't foreclose global optimality. On-demand, per Pass 1c.
- **requires:** Induction

### Optimal substructure
An optimal solution to a problem is built from optimal solutions to its subproblems.
- **requires:** Recursive decomposition
- **note:** this is the concept both Greedy and Dynamic programming lean on but resolve differently — greedy commits to one locally-optimal choice, DP explores all of them. See "Recurring patterns" below.

### Greedy paradigm
- **requires:** Ordering relation, Exchange argument, Optimal substructure
- **exemplars:** interval scheduling

### Shortest paths / MST
- **requires:** Weighted relationships, Traversal, Priority Queue ADT, Greedy paradigm
- **exemplars:** Dijkstra (no extra requirement beyond the parent); Prim (no extra requirement beyond the parent); Kruskal (+ Disjoint-set (union-find))

### Overlapping subproblems
The same subproblem recurs many times under naive recursion. Distinct from Optimal substructure — this is about repeated *calls*, not about optimality.
- **requires:** Recursive decomposition
- **exemplars:** naive recursive Fibonacci

### Memoization
- **requires:** Overlapping subproblems, Contiguity
- **exemplars:** array-indexed cache (no extra requirement); hash-keyed cache (+ Hashing)

### Dynamic programming
- **requires:** Memoization, Optimal substructure
- **exemplars:** knapsack, edit distance
- **note:** this node used to (incorrectly) require Optimal substructure directly off of Recursive decomposition alone, which broke on its own intro exemplar — naive Fibonacci has no optimization objective, it's just Overlapping subproblems. Splitting the two apart fixed this and produced a sharper D&C-vs-DP contrast (see below) alongside the existing Greedy-vs-DP one.

### Reduction
Formal tool: showing one problem can be transformed into another, used to establish relative difficulty.
- **requires:** Operation cost as a function of representation

### NP-completeness / limits of efficient computation
- **requires:** Reduction, Operation cost as a function of representation, Graph representation fork
- **exemplars:** vertex cover, Hamiltonian path
- **note:** this does *not* require Comparison lower bound — the earlier draft's edge there was thematic ("both are about limits of computation"), not a real dependency. Kept as a prose cross-reference only.

---

## Recurring patterns (cross-cutting, worth naming explicitly)

**The contiguous/indirect fork reappears at five separate scales**, and a learner who sees it named once should recognize it as the same idea recurring rather than as fresh trivia each time:

1. Layer 4 — Sequential vs. Linked representation (arrays vs. linked lists)
2. Layer 5 — Collision resolution: chaining (linked) vs. open addressing (contiguous)
3. Layer 6 — Priority Queue's array-backed exemplars vs. the array-backed binary heap (all-array, but the heap uses index arithmetic to fake a tree — the *sharpest* version of "it's all one array underneath")
4. Layer 7 — Graph representation: adjacency matrix (contiguous) vs. adjacency list (indirect)
5. Layer 8 — Memoization's cache choice: array-indexed (contiguous) vs. hash-keyed (indirect via hashing)

This is a candidate stress-test question for Pass 5: does the learner independently recognize occurrence 4 or 5 as "the same fork from Layer 4," or do they treat it as new material?

**Two paradigm contrasts, both resting on Optimal substructure:**

- **Greedy vs. Dynamic programming** — both assume optimal substructure; greedy commits to a single locally-optimal choice per step (needs an Exchange argument to justify that this never costs global optimality), DP instead explores all choices and caches the results (needs Memoization, which is only necessary because Overlapping subproblems exist).
- **Divide & conquer vs. Dynamic programming** — both recurse, but D&C's subproblems are disjoint (no need to cache) while DP's overlap (memoization is the entire point). This is arguably the more fundamental of the two contrasts, since it's about the *shape* of the recursion tree rather than an optimization strategy choice.

## Open flags for later passes

- The array-backed binary heap (Layer 6) is explicitly named in the README as an unresolved visualization gap — VisuAlgo doesn't show the "it's one array underneath" mechanism. Pass 3 needs a resource for this specific node, possibly outside the already-surveyed set.
- The formal-tools track (Induction, Exchange argument, Probability/expectation, Reduction) is intentionally thin here — each is a placeholder for "pull in MIT 6.042 material on demand," not a fully worked concept. Pass 3 should treat these four as a distinct resource-mapping category, separate from data-structure/algorithm concepts.
- Graph-as-generalization-of-trees was deliberately kept as a sequencing note rather than a hard edge (see Layer 7). Pass 4 should decide whether to actually sequence trees before graphs (likely yes, pedagogically) even though the dependency graph doesn't force it.
