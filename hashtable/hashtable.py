class LinkedList:
    """
    Linked list object to hold hash table entries
    """
    def __init__(self, start=None, end=None):
        self.start = start
        self.end = end

    def add_entry(self, entry):
        if not self.start:
            self.start = entry
            self.end = entry
        else:
            tmp = self.end
            tmp.next = entry
            self.end = tmp

        return

    def delete_entry(self, key):
        """Remove a specific entry"""
        if self.start is None:
            print("List is empty, key cannot exist")
            return
        target = self.start
        while target.key != key:
            if target.next is None:
                print("Final entry inspected, key not found.")
                return
            prv = target
            target = target.next

        # if there is only one item in list, set start and end to None
        if self.start is self.end:
            self.start = None
            self.end = None

            return

        if target is self.start:
            self.start = self.start.next

            return

        if target is self.end:
            prv.next = None
            self.end = prv

            return

    def retrieve_value(self, key):
        """Returns the value of a specific entry"""
        if not self.start:
            print("List is empty, key cannot exist")
            return
        target = self.start
        while target.key != key:
            if target.next is None:
                print("Key does not exist in list")
                return
            target = target.next

        return target.value


class HashTableEntry:
    """
    Linked List hash table key/value pair
    """
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None


# Hash table can't have fewer than this many slots
MIN_CAPACITY = 8


class HashTable:
    """
    A hash table that with `capacity` buckets
    that accepts string keys

    Implement this.
    """

    def __init__(self, capacity):
        self.capacity = capacity
        self.storage = [None] * self.capacity

    def get_num_slots(self):
        """
        Return the length of the list you're using to hold the hash
        table data. (Not the number of items stored in the hash table,
        but the number of slots in the main list.)

        One of the tests relies on this.

        Implement this.
        """
        # Your code here

    def get_load_factor(self):
        """
        Return the load factor for this hash table.

        Implement this.
        """
        # Your code here

    def fnv1(self, key):
        """
        FNV-1 Hash, 64-bit

        Implement this, and/or DJB2.
        """
        # 64-bit
        offset_basis = 14695981039346656037
        FNV_prime = 1099511628211

        hash = offset_basis
        for char in key.encode():
            hash = hash ^ char
            hash *= FNV_prime

        return hash

        # Your code here

    def djb2(self, key):
        """
        DJB2 hash, 32-bit

        Implement this, and/or FNV-1.
        """
        # Your code here

    def hash_index(self, key):
        """
        Take an arbitrary key and return a valid integer index
        between within the storage capacity of the hash table.
        """
        return self.fnv1(key) % self.capacity

    def put(self, key, value):
        """
        Store the value with the given key.

        Hash collisions should be handled with Linked List Chaining.

        Implement this.
        """
        hash_idx = self.hash_index(key)
        new_entry = HashTableEntry(key, value)

        if self.storage[hash_idx]:
            self.storage[hash_idx].add_entry(new_entry)

            return

        self.storage[hash_idx] = LinkedList()
        self.storage[hash_idx].add_entry(new_entry)


    def delete(self, key):
        """
        Remove the value stored with the given key.

        Print a warning if the key is not found.

        Implement this.
        """
        hash_idx = self.hash_index(key)

        if not self.storage[hash_idx]:
            print(f"No key for \"{key}\". Create one first")
            return

        self.storage[hash_idx].delete_entry(key)


    def get(self, key):
        """
        Retrieve the value stored with the given key.

        Returns None if the key is not found.

        Implement this.
        """
        hash_idx = self.hash_index(key)

        if self.storage[hash_idx]:
            return self.storage[hash_idx].retrieve_value(key)

        return self.storage[hash_idx]

    def resize(self, new_capacity):
        """
        Changes the capacity of the hash table and
        rehashes all key/value pairs.

        Implement this.
        """
        # Your code here


if __name__ == "__main__":
    ht = HashTable(8)

    ht.put("line_1", "'Twas brillig, and the slithy toves")
    ht.put("line_2", "Did gyre and gimble in the wabe:")
    ht.put("line_3", "All mimsy were the borogoves,")
    ht.put("line_4", "And the mome raths outgrabe.")
    ht.put("line_5", '"Beware the Jabberwock, my son!')
    ht.put("line_6", "The jaws that bite, the claws that catch!")
    ht.put("line_7", "Beware the Jubjub bird, and shun")
    ht.put("line_8", 'The frumious Bandersnatch!"')
    ht.put("line_9", "He took his vorpal sword in hand;")
    ht.put("line_10", "Long time the manxome foe he sought--")
    ht.put("line_11", "So rested he by the Tumtum tree")
    ht.put("line_12", "And stood awhile in thought.")

    print("")

    # Test storing beyond capacity
    for i in range(1, 13):
        print(ht.get(f"line_{i}"))

    # Test resizing
    old_capacity = ht.get_num_slots()
    ht.resize(ht.capacity * 2)
    new_capacity = ht.get_num_slots()

    print(f"\nResized from {old_capacity} to {new_capacity}.\n")

    # Test if data intact after resizing
    for i in range(1, 13):
        print(ht.get(f"line_{i}"))

    print("")
