# Research Pass 1: How strong DSA sources actually sequence and motivate concepts

Method: fetched real syllabi/booksite/table-of-contents pages rather than relying on recall. Sources verified below; each claim is cited.

## 1. Princeton Algorithms (Sedgewick & Wayne)

Sources: [algs4.cs.princeton.edu/home](https://algs4.cs.princeton.edu/home/), [algs4.cs.princeton.edu/15uf](https://algs4.cs.princeton.edu/15uf/)

**Order (Ch. 1 Fundamentals):** 1.1 Programming Model → 1.2 **Data Abstraction** → 1.3 Stacks and Queues → 1.4 Analysis of Algorithms → 1.5 Case Study: Union-Find. Then Ch. 2 Sorting, Ch. 3 Searching (Symbol Tables → BST → Balanced Search Trees → Hash Tables), Ch. 4–6 Graphs/Strings/Context.

**Motivation pattern — confirmed, explicit "friction → new representation":** Union-Find is taught as three successive attempts, each hitting a wall:
1. **Quick-find** — O(1) find, but union costs O(n) (must rewrite the whole array).
2. **Quick-union** — fixes union cost, but trees can grow tall/unbalanced → find degrades.
3. **Weighted quick-union + path compression** — fixes tree height, gives near-O(1) amortized for both operations.

The page presents the **API/interface separately** from the implementations, and includes an explicit **operation-cost comparison table** across all three versions. This is a direct, textbook example of the "naive → bottleneck → better → bottleneck → best" pattern you want the whole curriculum built around.

**Asymptotic analysis** (1.4) is introduced *right after* data abstraction/stacks-queues but *right before* union-find — i.e., students get the vocabulary to describe cost just before the first real "compare implementations" case study.

**Verdict:** Excellent model lesson for the friction-driven pattern, but it's *one case study early on* (union-find), not the organizing principle of the whole course — sorting and searching chapters are more topic-listy.

## 2. MIT 6.006 (Spring 2020 OCW)

Sources: [ocw.mit.edu .../lecture-2-data-structures-and-dynamic-arrays](https://ocw.mit.edu/courses/6-006-introduction-to-algorithms-spring-2020/resources/lecture-2-data-structures-and-dynamic-arrays/), [syllabus](https://ocw.mit.edu/courses/6-006-introduction-to-algorithms-spring-2020/pages/syllabus/)

**Order:** L1 Introduction → L2 Data Structures & Dynamic Arrays → L3 Sorting → L4 Hashing → L5 Linear Sorting → L6–7 Binary Trees / AVL → L8 Binary Heaps → L9 BFS → ...

**Interface framing — confirmed:** Lecture 2 states explicitly: *"Data structures are ways to store data with algorithms that support operations on the data. These collections of operations are interfaces."* The course names two governing interfaces, **Sequence** and **Set**, taught across multiple lectures (Sequence: L2, L7; Set: L3–L8), with specific structures (arrays, hash tables, trees, heaps) as competing implementations of those interfaces.

**Confirmed (merged from the original MIT-specific research pass, which read Lecture 1 and Lecture 2 directly, incl. the L1 PDF):** Lecture 1 opens with the "document distance" problem before any data structure appears — problem-first from minute one. Lecture 2 motivates the dynamic array explicitly as a fix for a plain array's fixed-capacity limitation (amortized-cost resizing), and Binary Trees Part 2 is explicitly framed as fixing unbalanced-BST degradation via AVL balancing — the same bottleneck-driven pattern as Princeton's union-find. Asymptotic analysis (Word-RAM model, O/Ω/Θ) is taught in Lecture 1, before the first data structure in Lecture 2.

**Verdict:** Confirms the formal "interface vs. implementation" backbone your Nic Barker intuition needs, *and* independently confirms the friction-driven motivation pattern (dynamic array from fixed array; AVL from unbalanced BST) — not just interface/implementation separation. Strong candidate for the "formalization" layer of the curriculum.

## 3. Open Data Structures (Pat Morin, Java edition)

Sources: [opendatastructures.org/ods-java](https://opendatastructures.org/ods-java/), [1.2 Interfaces](https://opendatastructures.org/ods-java/1_2_Interfaces.html)

**Order:** 1 Introduction (incl. 1.2 Interfaces) → 2 Array-Based Lists → 3 Linked Lists → 4 Skiplists → 5 Hash Tables → 6 Binary Trees → 7 Random BSTs → 8 Scapegoat Trees → 9 Red-Black Trees → 10 Heaps → 11 Sorting → 12 Graphs → 13 Integer structures → 14 External Memory.

**Interface framing — most explicit of all four sources.** Section 1.2 states directly: *"An interface describes what a data structure does, while an implementation describes how the data structure does it."* It defines six interfaces up front (Queue, Stack, Deque, List, USet, SSet) *before any implementation chapter*, and explicitly previews that Ch. 2 implements List with arrays and Ch. 3 implements List with pointers — i.e., **the book is structured as "one interface, several competing implementations,"** with an explicit statement that choice of implementation is a performance trade-off (e.g., ChainedHashTable USet gets O(1) expected find vs. most SSet implementations' O(log n), so "use USet unless you need SSet's extra ordering operations").

**Verdict:** Strongest fit for someone who wants to *implement* each structure (Java, matches your interest) and see the interface/implementation split made explicit before writing any code. Best source to anchor Research Pass 2's "interface vs. implementation" node.

## 4. Nic Barker video — fully confirmed (2026-09-24, via transcript)

Sources: [YouTube: "Data Structures, Explained Simply"](https://www.youtube.com/watch?v=KwBuV7YZido); full transcript reviewed and summarized in [`../sources/nic-barker-transcript.md`](../sources/nic-barker-transcript.md).

Confirmed, from the actual transcript, not inference: the video's stated thesis is "a data structure is a strategy for finding something in an array," and it builds a genuine dependency chain — array → sorted array → array list → stack → queue (circular buffer via modulo) → linked list → hash map (chaining reuses linked lists inside a second array) → tree (linked list generalized to multiple children) → graph (tree generalized to multiple parents) — where each structure is introduced by naming a specific limitation of the previous one. The "memory → limitation → new representation" framing was accurate, not an overreach.

Notable addition beyond what Princeton/MIT/ODS show: Barker's chain operates one level lower than "interface vs. implementation" — it grounds *why* an implementation's cost profile is what it is in the physical layout of the backing array, rather than starting from a defined interface and comparing implementations against it. See `../sources/nic-barker-transcript.md` for the full mapping and the resulting two-layer suggestion for Pass 2.

**Correction — don't take Barker's chain as complete.** It's a real dependency chain, but a narrow one: the "is Z present" example is answered by checking the sorted array's last element, not by generalizing to binary search — the video never introduces binary search at all. His "trees" are hierarchies (UI parent/child), not search trees, so the video never derives a BST or explains why ordering + tree shape enables logarithmic search. The chain also has no treatment of resizing/amortized cost analysis, heaps, sorting, or recursion. Those gaps are exactly where Princeton/MIT/ODS's formal treatment has to do real work Barker's video doesn't attempt — Pass 2 shouldn't treat his sequence as sufficient on its own.

**A stated-but-unaddressed constraint worth carrying into Pass 2/4:** Barker's cost intuition (contiguous array = cache-friendly, pointer-chasing = cache-hostile) is a C-level claim about raw memory. In Java — the implementation language this project favors, per ODS — `ArrayList<Integer>` and most non-primitive arrays store *references*, not inline values, so the "array beats linked list on cache locality" experiment can fail to reproduce or even reverse unless primitive arrays (`int[]`) are used deliberately. Any later experiment/benchmark step needs to address this explicitly or it will contradict the intuition it's trying to teach.

## 5. Problem-first algorithm texts

Source: [Jeff Erickson, *Algorithms*](https://jeffe.cs.illinois.edu/teaching/algorithms/)

Erickson's free book's chapter list: Intro → Recursion → Backtracking → Dynamic Programming → Greedy → Basic Graph Algorithms → DFS → MST → Shortest Paths → All-Pairs Shortest Paths → Max-Flow/Min-Cut → NP-Hardness.

**Important finding:** this book **does not cover basic data structures at all** — no arrays/lists/trees/hash tables chapters. It's purely an *algorithmic-paradigm* text (recursion, DP, greedy, graph algorithms). Its PDFs weren't machine-readable via WebFetch, so the "does it open each topic with a concrete problem" question is unverified — flagged as a gap, not assumed.

**Verdict:** Not a substitute for a data-structures-motivation source — it's the natural *next layer* after structures are established, for the "algorithm design" end of your dependency graph (section 6/13 of the philosophy doc), not the "why does this structure exist" end.

## Cross-source synthesis (the actual finding)

All three of the rigorous, citable sources (Princeton, MIT, ODS) **independently converge on the same structural move**: separate the **interface/ADT** (what operations, what they mean) from the **implementation** (how, at what cost) — then teach multiple implementations of one interface side by side with a cost comparison. That is a formal, textbook-grade version of exactly the intuition Nic Barker's video gave you informally. None of them, however, organize their *entire* syllabus around "friction → new representation" the way Princeton's union-find case study does for one topic — that pattern shows up as an occasional set-piece, not the whole course's spine.

This suggests a concrete answer for Research Pass 2: the recurring unit of your curriculum shouldn't be "a data structure" — it should be **"an interface + the sequence of implementations that interface accumulates as each one's bottleneck is discovered,"** exactly mirroring union-find's three-act structure, generalized to List, Set/Map, Priority Queue, Graph, etc. ODS's interface list (Queue, Stack, Deque, List, USet, SSet) is a ready-made starting set of interfaces to build that structure around; MIT's Sequence/Set framing is a simpler two-interface version of the same idea for a first pass.

## Open gaps (not chased further in this pass, per plan to stop after Pass 1)

- Full lecture transcripts for MIT 6.006 (to confirm whether L2 shows a cost table / motivates dynamic arrays by a stated array limitation).
- Kleinberg–Tardos and Skiena tables of contents (not reached this pass).
- A rewatch of the Nic Barker video to check its actual on-screen structure against this pass's more rigorous sources.
