# 02 Добавьте в класс HashTable метод resize, который увеличивает
# размер хеш-таблицы вдвое и перераспределяет все элементы.
# Протестируйте работу метода на примере хеш-таблицы с начальным
# размером 5, добавив в неё 10 элементов

class HashTable:
    def __init__(self, size=5):
        self.size = size
        self.table = [[] for _ in range(size)]
        self.count = 0

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
        self.count += 1

        if self.count > self.size * 0.7:
            self._resize()

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
                self.count -= 1
                return True
        return False

    def _resize(self):
        old_table = self.table
        self.size *= 2
        self.table = [[] for _ in range(self.size)]
        self.count = 0

        for bucket in old_table:
            for key, value in bucket:
                self.insert(key, value)

    def __str__(self):
        return "\n".join(f"{i}: {bucket}" for i, bucket in enumerate(self.table))

    def get_load_factor(self):
        return self.count / self.size


ht = HashTable(size=5)

for i in range(10):
    ht.insert(f"key{i}", i * 10)
    print(f"После вставки key{i}:")
    print(f"Размер таблицы: {ht.size}")
    print(f"Коэффициент загрузки: {ht.get_load_factor():.2f}")
    print(ht)
    print("-" * 30)

print("Поиск key5:", ht.search("key5"))
print("Поиск key9:", ht.search("key9"))