class HybridMemory:
    def __init__(self):
        self.cache = {}
        self.archive = {}

    def store(self, task, result):
        self.cache[task["name"]] = result
        # Пример: по размеру/давности выбрасываем в архив
        if len(self.cache) > 10:
            key, val = self.cache.popitem()
            self.archive[key] = val

    def get(self, key):
        if key in self.cache:
            return self.cache[key]
        if key in self.archive:
            return self.archive[key]
        return None
