
class HashTable:

    def __init__(self, length: int):
        self.length = length
        self.hash_table = [[]] * length

    def __str__(self):
       return ''.join(map(str, self.hash_table))

    def hash_func(self, key):
        return key % self.length

    def add(self, key, value):
        index = self.hash_func(key)
        if not self.hash_table[index]:
            self.hash_table[index] = [key, value]
        else:
            self.hash_table[index].extend([key, value])

    def search(self, key):
        index = self.hash_func(key)
        if self.hash_table[index]:
            return self.hash_table[index][self.hash_table[index].index(key) + 1]
        else:
            return None

    def remove(self, key: int, data):
        index = self.hash_func(key)
        result = self.search(key)
        if result:
            if data in self.hash_table[index]:
                self.hash_table[index].remove(key)
                self.hash_table[index].remove(data)
            else:
                error = ValueError(f'Відсутнє значення \'{data}\' з ключем ({key}).')
                raise error
        else:
            error = KeyError(f'Відсутній ключ ({key}) у хеш-таблиці.')
            raise error


my_hash_table = HashTable(10)

my_hash_table.add(1, 'One')
my_hash_table.add(4, 'Four')
my_hash_table.add(7, 'Seven')
print(my_hash_table)

print(my_hash_table.search(4))

my_hash_table.remove(1, 'One')
print(my_hash_table)