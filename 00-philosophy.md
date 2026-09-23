# DSA Learning Philosophy & Roadmap Project

Origin: synthesized from a conversation with ChatGPT (2026-09-23), continued here for actual research and curriculum design.

## Core principle

> Don't organize DSA education around the list of data structures/algorithms to memorize; organize it around the problems, representations, operations, constraints, and trade-offs that cause those structures and algorithms to exist.

> Don't learn the answer before understanding the problem that produced the answer.

## What's explicitly rejected

The conventional interview-prep pipeline:

```
roadmap.sh → watch a roadmap video → learn Array → learn Linked List →
learn HashMap → solve 500 LeetCode problems → call yourself "good at DSA"
```

This risks producing pattern-matching ("this looks like a HashMap problem") rather than the ability to reason about an unfamiliar problem from first principles: what's happening, what information is needed, how to represent it, what's expensive, how to make it cheaper.

## Preferred learning pattern (primitive before abstraction)

```
simple implementation → actually use it → encounter its limitations →
understand the problem → discover/introduce abstraction → understand why it exists
```

Applied to data structures specifically (the "Nic Barker pattern"):

```
UNDERLYING MECHANISM (memory)
  → SIMPLE REPRESENTATION (e.g. array)
  → WHAT DOES IT MAKE EASY?
  → WHAT DOES IT MAKE HARD?
  → ENCOUNTER FRICTION
  → NEW IDEA / REPRESENTATION
  → IMPLEMENT IT
  → ANALYZE THE TRADE-OFF
```

Key reframe that triggered this project: **a data structure is a strategy for organizing data and controlling how it's read/written/accessed, underneath which is memory.** Not "a data structure with indexed elements" but "why does laying elements out contiguously make indexed access cheap, and what does that same layout make expensive?"

Every data structure is a trade-off (array: cheap indexed access, expensive middle insert; linked list: cheap insert/delete given a reference, expensive random access; hash table: ~O(1) average lookup at the cost of hashing/collisions/load factor/resizing; BST: ordering, but degrades to a linked list without balancing — which is *why* balanced trees exist).

Data structures and algorithms are connected, not separate subjects:

```
representation → available operations → cost of those operations → algorithm design
```

## Why not LeetCode-as-curriculum

Not anti-LeetCode — anti making it the *center*. Conventional: learn pattern X → grind X-shaped problems → learn pattern Y → grind Y-shaped problems (produces pattern recognition, not problem-solving). Preferred: problem → understand it → naive approach → find the bottleneck → ask what information matters → change representation → derive algorithm → implement → test → analyze complexity → consider alternatives → reflect. LeetCode becomes practice material after understanding, not the education itself.

## The layered education (intuition isn't enough on its own)

Nic Barker-style intuition is necessary but not sufficient. Needs to combine with formal rigor (Big-O/Theta/Omega, worst/average/best case, amortized analysis, space complexity, invariants, correctness proofs, recurrence relations, algorithmic paradigms, lower bounds):

```
INTUITION → IMPLEMENTATION → EXPERIMENT → ANALYSIS → FORMALIZATION →
PROBLEM SOLVING → ALGORITHM DESIGN
```

## Candidate resources (each assigned a job, not merged into one checklist)

- **Nic Barker** ("Data Structures, Explained Simply") — intuitive, bottom-up mental models
- **MIT 6.006** — formal algorithmic thinking, correctness, efficiency
- **Open Data Structures** — implementation + analysis (useful given interest in Java)
- **Princeton Algorithms (Sedgewick/Wayne)** — rigor, implementation, experimentation, performance
- **VisuAlgo** — dynamic visualization
- Possibly: CLRS, other university curricula, textbooks, papers, curated exercises/projects

Explicitly rejected approach: `MIT syllabus + Princeton syllabus + CLRS + ODS + YouTube + LeetCode` merged into one giant checklist. Instead: find the conceptual dependency graph underneath these sources, then attach named structures/algorithms to that graph.

## The 5-pass research process

1. **Pedagogy** — how do strong courses/books actually sequence and motivate concepts? (done — see `passes/01-pedagogy.md`)
2. **Conceptual dependency graph** — strip course names, find the underlying ideas and their dependencies (memory, representation, operations, cost, abstraction, invariants, recursion, ordering, search, relationships, optimization)
3. **Resource mapping** — assign each concept's best resource by job (intuition / formal / implementation / visualization / exercises / problems)
4. **Curriculum build** — sequence, milestones, implementation tasks, experiments, readings, projects, review mechanisms
5. **Stress-test** — does this actually teach reasoning about unfamiliar problems, or is it a disguised LeetCode roadmap in different clothes?

A rough (explicitly non-final) example progression discussed: memory → arrays → dynamic storage → ADTs/operations → stacks+queues → linked structures → complexity/analysis → recursion → searching → sorting → hashing → trees → heaps/priority queues → graphs → divide & conquer → greedy → DP → graph algorithms → algorithm design → advanced CS.
