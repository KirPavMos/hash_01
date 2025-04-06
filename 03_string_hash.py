# 03 Напишите функцию, которая принимает строку и возвращает
# её хеш-значение. Для этого используйте простой алгоритм:
# сложение ASCII-кодов всех символов строки


def simple_string_hash(s):
    hash_value = 0
    for char in s:
        hash_value += ord(char)
    return hash_value

print(simple_string_hash("hello"))
print(simple_string_hash("world"))
print(simple_string_hash(""))