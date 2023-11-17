import hashlib

class ConsistentHashing:
    def __init__(self, nodes=None, replicas=3):
        self.replicas = replicas
        self.ring = {}
        self.sorted_keys = []
        if nodes:
            for node in nodes:
                self.add_node(node)

    def add_node(self, node):
        for i in range(self.replicas):
            replica_key = self._generate_replica_key(node, i)
            self.ring[replica_key] = node
            self.sorted_keys.append(replica_key)
        self.sorted_keys.sort()

    def remove_node(self, node):
        for i in range(self.replicas):
            replica_key = self._generate_replica_key(node, i)
            del self.ring[replica_key]
            self.sorted_keys.remove(replica_key)

    def get_node(self, key):
        if not self.ring:
            return None

        hashed_key = self._hash_key(key)
        for ring_key in self.sorted_keys:
            if hashed_key <= ring_key:
                return self.ring[ring_key]

        # If the key is greater than all keys in the ring, return the first node
        return self.ring[self.sorted_keys[0]]

    def _hash_key(self, key):
        # Using MD5 for simplicity; you might choose a different hash function in practice
        hash_object = hashlib.md5(key.encode())
        return int(hash_object.hexdigest(), 16)

    def _generate_replica_key(self, node, replica_index):
        # Generate a unique key for each replica of a node
        return self._hash_key(f"{node}-{replica_index}")

# Example Usage:
nodes = ["Node1", "Node2", "Node3"]
consistent_hashing = ConsistentHashing(nodes=nodes, replicas=5)

# Get the node responsible for a key
key_to_lookup = "SomeKey"
responsible_node = consistent_hashing.get_node(key_to_lookup)

print(f"The node responsible for key '{key_to_lookup}' is: {responsible_node}")

# Add a new node
consistent_hashing.add_node("Node4")

# Remove a node
consistent_hashing.remove_node("Node2")

# Get the node responsible for a key
key_to_lookup = "SomeKey"
responsible_node = consistent_hashing.get_node(key_to_lookup)
print(f"The node responsible for key '{key_to_lookup}' is: {responsible_node}")


# Get the node responsible for a key
key_to_lookup = "SomeKey2"
responsible_node = consistent_hashing.get_node(key_to_lookup)
print(f"The node responsible for key '{key_to_lookup}' is: {responsible_node}")

# Get the node responsible for a key
key_to_lookup = "SomeKey3"
responsible_node = consistent_hashing.get_node(key_to_lookup)
print(f"The node responsible for key '{key_to_lookup}' is: {responsible_node}")


# Get the node responsible for a key
key_to_lookup = "SomeKey4"
responsible_node = consistent_hashing.get_node(key_to_lookup)
print(f"The node responsible for key '{key_to_lookup}' is: {responsible_node}")

# Get the node responsible for a key
key_to_lookup = "SomeKey5"
responsible_node = consistent_hashing.get_node(key_to_lookup)
print(f"The node responsible for key '{key_to_lookup}' is: {responsible_node}")