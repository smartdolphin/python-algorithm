import unittest


class HashTable(object):
    def __init__(self, size):
        self.size = size
        self.hash_table = [[] for _ in range(self.size)]

    def hash_func(self, key):
        return key % len(self.hash_table)

    def insert(self, key, value):
        hash_key = hash(key) % len(self.hash_table)
        key_exists = False
        bucket = self.hash_table[hash_key]
        for i, kv in enumerate(bucket):
            k, v = kv
            if key == k:
                key_exists = True
                break
        if key_exists:
            bucket[i] = ((key, value))
        else:
            bucket.append((key, value))

    def lookup(self, key):
        hash_key = hash(key) % len(self.hash_table)
        bucket = self.hash_table[hash_key]
        for i, kv in enumerate(bucket):
            k, v = kv
            if key == k:
                return v

    def delete(self, key):
        hash_key = hash(key) % len(self.hash_table)
        key_exists = False
        bucket = self.hash_table[hash_key]
        for i, kv in enumerate(bucket):
            k, v = kv
            if key == k:
                key_exists = True
                break
        if key_exists:
            del bucket[i]
            print('Key {} deleted'.format(key))
        else:
            print('Key {} not found'.format(key))

    def __getitem__(self, key):
        return self.lookup(key)

    def __setitem__(self, key, data):
        self.insert(key, data)

    def __delitem__(self, key):
        self.delete(key)

    def __call__(self):
        print(self.hash_table)


class TestHashTable(unittest.TestCase):
    def test_hash_table(self):
        hash_table = HashTable(10)
        hash_table[10] = 'one'
        hash_table[20] = 'two'
        hash_table[25] = 'three'
        hash_table[30] = 'four'

        self.assertEqual(
            hash_table[10], 'one'
        )
        self.assertEqual(
            hash_table[20], 'two'
        )
        self.assertEqual(
            hash_table[25], 'three'
        )
        self.assertEqual(
            hash_table[30], 'four'
        )
        hash_table()


if __name__ == '__main__':
    unittest.TestCase()
