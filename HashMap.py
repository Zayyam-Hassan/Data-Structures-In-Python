class HashMap:
    def __init__(self, size=10):
        self.size = size
        self.map = [None] * self.size

    def _get_hash(self, key):
        return hash(key) % self.size

    def _probe(self, hash_value):
        return (hash_value + 1) % self.size

    def insert(self, key, value):
        key_hash = self._get_hash(key)
        start_hash = key_hash

        while self.map[key_hash] is not None:
            if self.map[key_hash][0] == key:
                break
            key_hash = self._probe(key_hash)
            if key_hash == start_hash:
                raise Exception("Hash map is full")

        self.map[key_hash] = (key, value)

    def get(self, key):
        key_hash = self._get_hash(key)
        start_hash = key_hash

        while self.map[key_hash] is not None:
            if self.map[key_hash][0] == key:
                return self.map[key_hash][1]
            key_hash = self._probe(key_hash)
            if key_hash == start_hash:
                return None
        return None

    def delete(self, key):
        key_hash = self._get_hash(key)
        start_hash = key_hash

        while self.map[key_hash] is not None:
            if self.map[key_hash][0] == key:
                self.map[key_hash] = None
                return
            key_hash = self._probe(key_hash)
            if key_hash == start_hash:
                return None