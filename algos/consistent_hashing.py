import hashlib

class ConsistentHashing:

    def __init__(self, nodes, num_replicas):
        self.ring = {}
        self.sorted_keys = []
        self.num_replicas = num_replicas
        for node in nodes:
            self.add_node(node)
    
    def add_node(self, node):
        for replica in range(self.num_replicas):
            hash_key = self._get_hash_for_node(node, replica)
            self.sorted_keys.append(hash_key)
            self.ring[hash_key] = node
        
        self.sorted_keys.sort()    
    
    def remove_node(self, node):
        print(f"removing node {node}")
        for replica in range(self.num_replicas):
            hash_key = self._get_hash_for_node(node, replica)
            del self.ring[hash_key]
            self.sorted_keys.remove(hash_key)
        
    
    def get_node(self, key): 
        hash_key = self._get_hash(key)
        for key in self.sorted_keys:
            if hash_key <= key:
                return self.ring[key]
        
        # if not found, just use the 1st node
        return self.ring[self.sorted_keys[0]]
    
    def _get_hash(self, key):
        hash_obj = hashlib.md5(key.encode())
        return int(hash_obj.hexdigest(), 16)
    
    def _get_hash_for_node(self, node, replica):
        return self._get_hash(f"{node}-{replica}")

consistent_hashing = ConsistentHashing(
    [
        "Node 1",
        "Node 2",
        "Node 3",
        "Node 4",
        "Node 5"
    ],
    2
)

if __name__ == "__main__":
    for n in range(5):
        print(consistent_hashing.get_node(f"my_key_{n}"))
    consistent_hashing.remove_node("Node 1")
    for n in range(5):
        print(consistent_hashing.get_node(f"my_key_{n}"))    