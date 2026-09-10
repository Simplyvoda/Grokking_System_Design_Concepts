from build_merkle_tree import build_merkle_tree
from repair_replica import repair_replica, find_differences


def main():
    replica_a = {
        "user1": "Vodina",
        "user2": "Angela",
        "user3": "James",
        "user4": "Daniel",
    }

    replica_b = {
        "user1": "Vodina",
        "user2": "Angela",
        "user3": "John",
        "user4": "Daniel",
    }

    root_a = build_merkle_tree(replica_a)
    root_b = build_merkle_tree(replica_b)

    print("Replica A Root:", root_a.hash_value)
    print("Replica B Root:", root_b.hash_value)

    differing_keys = find_differences(root_a, root_b)
    print("Differing Keys:", differing_keys)

    repaired_replica = repair_replica(replica_a, replica_b, differing_keys)
    print("Replica A and B after repair:", repaired_replica)


if __name__ == "__main__":
    main()
