#creating the hashtable 
class HashTable:
    def __init__(self, size=100):
        self.array = [None] * size
        self.size = size

    def hash_function(self, key):
        return hash(key) % self.size

    def add(self, key, value):
        index = self.hash_function(key)
        self.array[index] = value

    def remove(self, key):
        index = self.hash_function(key)
        self.array[index] = None

    def search(self, key):
        index = self.hash_function(key)
        return self.array[index]

# Example usage:

hash_table = HashTable()

# Add some data to the hash table.
hash_table.add("name", "Alice")
hash_table.add("age", 25)

# Search for data in the hash table.
name = hash_table.search("name")
age = hash_table.search("age")

# Print the results.
print(name) # Alice
print(age) # 25


def hash_function(key):
    """Returns a hash value for the given key.

    Args:
    key: The key to hash.

    Returns:
    A hash value for the given key.
    """

    hash_value = 0
    for character in key:
        hash_value += ord(character)
        return hash_value % 100
