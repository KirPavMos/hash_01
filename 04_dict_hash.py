# 04 Используйте написанную хеш-функцию для создания словаря,
# в котором ключами являются строки, а значениями — их хешзначения.
# Реализуйте функции добавления элемента в словарь и поиска
# значения по ключу

def simple_string_hash(s):
    hash_value = 0
    for char in s:
        hash_value += ord(char)
    return hash_value

class CustomDict:
    def __init__(self, size=100):
        self.size = size
        self.table = [[] for _ in range(size)]

    def _get_index(self, key):
        return simple_string_hash(key) % self.size

    def insert(self, key, value):
        index = self._get_index(key)
        bucket = self.table[index]

        for i, (k, v) in enumerate(bucket):
            if k == key:
                bucket[i] = (key, value)
                return
        bucket.append((key, value))

    def search(self, key):
        index = self._get_index(key)
        bucket = self.table[index]

        for k, v in bucket:
            if k == key:
                return v
        return None

    def __str__(self):
        items = []
        for bucket in self.table:
            for key, value in bucket:
                items.append(f"'{key}': {value}")
        return "{" + ", ".join(items) + "}"

my_dict = CustomDict()

my_dict.insert("apple", simple_string_hash("apple"))
my_dict.insert("banana", simple_string_hash("banana"))
my_dict.insert("orange", simple_string_hash("orange"))

print("Хеш для 'apple':", my_dict.search("apple"))
print("Хеш для 'banana':", my_dict.search("banana"))
print("Хеш для 'grape':", my_dict.search("grape"))

print("\nСодержимое словаря:")
print(my_dict)