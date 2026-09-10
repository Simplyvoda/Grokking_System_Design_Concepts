from merkle_node import MerkleNode

def find_differences(nodeA: MerkleNode, nodeB: MerkleNode):
    if nodeA.hash_value == nodeB.hash_value:
        # no differences found, return empty list
        return []

    if nodeA.left is None and nodeA.right is None and nodeB.left is None and nodeB.right is None:
        # both nodes are leaves, return the key of the differing leaf
        return [nodeA.key]

    differences = []

    #if differences found , we wnat to check for parents
    if nodeA.left.hash_value != nodeB.left.hash_value:
        differences.extend(
            find_differences(nodeA.left, nodeB.left)
        )

    if nodeA.right.hash_value != nodeB.right.hash_value:
        differences.extend(
            find_differences(nodeA.right, nodeB.right)
        )

    return differences

"""
Algorithm to repair replica B using replica A:
1. Find the keys that differ.
2. For every differing key:
      get the value from A
      put that value into B
3. B is now repaired.
"""

def repair_replica(source, target, differing_keys):
    for key in differing_keys:  
        target[key] = source[key]
    return target, source
