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
        # Your code here
        self.capacity = capacity
        self.table = [None] * self.capacity
        self.number_of_items = 0

    def get_num_slots(self):
        """
        Return the length of the list you're using to hold the hash
        table data. (Not the number of items stored in the hash table,
        but the number of slots in the main list.)

        One of the tests relies on this.

        Implement this.
        """
        # Your code here
        return self.capacity

    def get_load_factor(self):
        """
        Return the load factor for this hash table.

        Implement this.
        """
        # Your code here
        return self.number_of_items / self.capacity

    def fnv1(self, key):
        """
        FNV-1 Hash, 64-bit

        Implement this, and/or DJB2.
        """

        # Your code here

    def djb2(self, key):
        """
        DJB2 hash, 32-bit

        Implement this, and/or FNV-1.
        """
        # Your code here
        hash = 5381
        for i in key:
            hash = ((hash << 5) + hash) + ord(i)
        return hash & 0xFFFFFFF

    def hash_index(self, key):
        """
        Take an arbitrary key and return a valid integer index
        between within the storage capacity of the hash table.
        """
        # return self.fnv1(key) % self.capacity
        return self.djb2(key) % self.capacity

    def put(self, key, value):
        """
        Store the value with the given key.

        Hash collisions should be handled with Linked List Chaining.

        Implement this.
        """
        # Your code here
        index = self.hash_index(key)
        current_node = self.table[index]

        if current_node is not None:
            # Search the linked list for a Node with the same KEY as the one we are inserting
            while current_node is not None:
                # If it exists, change the value of the node
                if current_node.key == key:
                    current_node.value = value
                current_node = current_node.next
            # if key is not found in the while loop
            # the first item in the hash_array is the HEAD of the linked list which is the current_node
            # Create a new hashTableEntry and add it to the HEAD of the linked list
            new_node = HashTableEntry(key, value)
            # set head as next node the new entry
            new_node.next = current_node
            # Make the new entry the new HEAD
            self.table[index] = new_node
            self.number_of_items += 1
        else:
            self.table[index] = HashTableEntry(key, value)
            self.number_of_items += 1

        # check load factor
        if self.get_load_factor() > 0.7:
            self.resize(self.capacity * 2)

    def delete(self, key):
        """
        Remove the value stored with the given key.

        Print a warning if the key is not found.

        Implement this.
        """
        # Your code here
        index = self.hash_index(key)
        current_node = self.table[index]
        prev = None

        # Search the linked list for a Node with the same KEY as the one we are inserting
        if current_node is not None:
            while current_node is not None:
                # If it exists, change the value of the node
                if current_node.key == key:
                    # if current node is the key, assign the previous node NEXT to the current node NEXT
                    if prev is not None:
                        prev.next = current_node.next
                    else:  # if this is head
                        self.table[index] = current_node.next
                    self.number_of_items -= 1
                # move the nodes if key is not found
                prev = current_node
                current_node = current_node.next
        else:
            print('Key not found')

    def get(self, key):
        """
        Retrieve the value stored with the given key.

        Returns None if the key is not found.

        Implement this.
        """
        # Your code here
        index = self.hash_index(key)
        current_node = self.table[index]
        # Search / Loop through the linked list at the hashed index
        while current_node is not None:
            # Compare the key to search to the keys in the nodes
            if current_node.key == key:
                # if you find it, return the value
                return current_node.value
            current_node = current_node.next
        # if not, return None
        return None

    def resize(self, new_capacity):
        """
        Changes the capacity of the hash table and
        rehashes all key/value pairs.

        Implement this.
        """
        old_table = self.table
        self.table = [None] * new_capacity
        self.capacity = new_capacity

        for item in old_table:
            while item is not None:
                self.put(item.key, item.value)
                item = item.next


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
