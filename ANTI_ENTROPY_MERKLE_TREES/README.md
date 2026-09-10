# Anti-Entropy with Merkle Trees

## The problem

Data gets replicated across nodes for availability. Over time, replicas
drift apart — a write gets dropped, a network hiccups, a node comes back
online after being down.

**Anti-entropy** is a background process that finds and fixes this drift so
replicas converge back to the same data.

## Why Merkle trees

Comparing every key on every replica works, but it's slow at scale. A
**Merkle tree** fixes that:

- Each leaf is the hash of one key-value pair.
- Each parent is the hash of its children's hashes.
- If two replicas match, their root hashes match too.
- If even one value differs, that difference bubbles all the way up to the
  root hash.

So two replicas only need to compare **one hash** to know if they match. If
they don't, they walk down only the branches that disagree — matching
subtrees are skipped entirely.

## The files

| File | What it does |
|---|---|
| `merkle_node.py` | `MerkleNode` — a tree node with a hash, optional `left`/`right` children, and a `key`/`value` for leaves. |
| `build_merkle_tree.py` | Builds the tree bottom-up: hash each key-value pair into a leaf, then repeatedly hash pairs of nodes together until one root remains. |
| `repair_replica.py` | `find_differences` walks two trees together and returns only the keys where hashes diverge. `repair_replica` copies those keys' values from the source replica into the target. |
| `main.py` | Entry point — builds two sample replicas, compares them, and repairs any drift. |

## Run it

```bash
python3 main.py
```

## Where this is used in the real world

Systems like Apache Cassandra and Amazon DynamoDB use this exact idea to
repair replicas without shipping full datasets across the network — only
the divergent keys get exchanged.
