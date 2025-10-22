import threading
import time
import uuid

class EfimeraWorker(threading.Thread):
    """Эфемерный воркер: кратковременно живёт, обрабатывает задачу и самоуничтожается."""
    def __init__(self, task, handler):
        super().__init__(daemon=True)
        self.task = task
        self.handler = handler
        self.id = str(uuid.uuid4())[:8]

    def run(self):
        print(f"[EfimeraWorker-{self.id}] Запуск для задачи {self.task['name']}")
        try:
            result = self.handler(self.task)
            time.sleep(0.2)
            print(f"[EfimeraWorker-{self.id}] Завершён, результат: {result}")
        except Exception as e:
            print(f"[EfimeraWorker-{self.id}] Ошибка: {e}")

class EfimeraManager:
    """Создаёт и управляет эфирными потоками (воркерами)."""
    def __init__(self, plugin_manager):
        self.plugin_manager = plugin_manager
        self.active = {}

    def spawn(self, task):
        worker = EfimeraWorker(task, self.plugin_manager.execute)
        self.active[worker.id] = worker
        worker.start()
        # автоочистка завершённых
        threading.Thread(target=self._cleanup, daemon=True).start()

    def _cleanup(self):
        for wid, worker in list(self.active.items()):
            if not worker.is_alive():
                del self.active[wid]
