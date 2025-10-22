import threading, time

class NightOptimizer:
    def __init__(self, memory):
        self.memory = memory
        self.running = False
        self.thread = threading.Thread(target=self._run)

    def start(self):
        self.running = True
        self.thread.start()

    def stop(self):
        self.running = False
        self.thread.join()

    def _run(self):
        print("[NightOptimizer] night scan start")
        while self.running:
            # Пример фоновой задачи: чистка архива, пересчёт статистики
            if len(self.memory.archive) > 20:
                self.memory.archive.clear()
                print("[NightOptimizer] archive cleaned")
            time.sleep(10)  # Проверять каждые ~10 секунд

# Использование:
# opt = NightOptimizer(memory)
# opt.start()
