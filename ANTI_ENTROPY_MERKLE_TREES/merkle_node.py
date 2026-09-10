class MerkleNode:
    # each node in the Merkle tree has a hash value, and optionally left and right children, as well as a key-value pair for leaf nodes
    def __init__(self, hash_value, left=None, right=None, key=None, value=None):
        self.hash_value = hash_value
        self.left = left
        self.right = right
        self.key = key
        self.value = value
