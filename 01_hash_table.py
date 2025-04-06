# 01_Напишите класс HashTable, который реализует основные
# операции хеш-таблицы: insert (вставка элемента),
# search (поиск элемента) и delete (удаление элемента)

class HashTable:
    def __init__(self, size=10):
        self.size = size
        self.table = [[] for _ in range(size)]

    def _hash(self, key):
        return hash(key) % self.size

    def insert(self, key, value):
        index = self._hash(key)
        bucket = self.table[index]

        for i, (k, v) in enumerate(bucket):
            if k == key:
                bucket[i] = (key, value)
                return
        bucket.append((key, value))

    def search(self, key):
        index = self._hash(key)
        bucket = self.table[index]

        for k, v in bucket:
            if k == key:
                return v
        return None

    def delete(self, key):
        index = self._hash(key)
        bucket = self.table[index]

        for i, (k, v) in enumerate(bucket):
            if k == key:
                del bucket[i]
                return True
        return False

    def __str__(self):
        return "\n".join(f"{i}: {bucket}" for i, bucket in enumerate(self.table))

ht = HashTable()

ht.insert("apple", 10)
ht.insert("banana", 20)
ht.insert("orange", 30)

print(ht.search("banana"))
ht.insert("grape", 40)
ht.delete("banana")
print(ht.search("banana"))
print(ht)