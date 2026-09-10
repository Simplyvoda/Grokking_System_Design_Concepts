#this gives access to hashing librabry
import hashlib
from merkle_node import MerkleNode

# function to hash data
def hash_function(data: str) -> str:
    return hashlib.sha256(data.encode()).hexdigest()

# always onstruct merkle tree in deterministic order

def build_leaves(replica_data: list) -> list:
    leaves = []
    for key in sorted(replica_data):
        value = replica_data[key]
        leaf_hash = hash_function(f"{key}:{value}")
        leaf = MerkleNode(hash_value=leaf_hash, key=key, value=value)
        # put the node in the leaves list
        leaves.append(leaf)
    return leaves

def build_parent(leaves: list) -> list:
    parents = []
    for i in range(0, len(leaves), 2):
        left = leaves[i]
        right = leaves[i + 1] if i + 1 < len(leaves) else left
        parent_hash = hash_function(f"{left.hash_value}:{right.hash_value}")
        parent = MerkleNode(hash_value=parent_hash, left=left, right=right)
        # put the node in the parent list
        parents.append(parent)
    return parents

# keep building parent until only one hash remains

def build_merkle_tree(data: dict) -> MerkleNode:
    leaves = build_leaves(data)
    parents = build_parent(leaves)

    while len(parents) > 1:
        parents = build_parent(parents)

    root = parents[0]
    return root