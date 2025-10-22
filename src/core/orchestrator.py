import threading
import time
from datetime import datetime, time as ttime

from core.emulator import Emulator
from core.memory import HybridMemory
from core.sensors import SensorManager
from core.sorter import TaskSorter
from modules.plugins import PluginManager
from core.efimera import EfimeraManager

class Orchestrator:
    def __init__(self):
        self.emulator = Emulator()
        self.memory = HybridMemory()
        self.sensors = SensorManager()
        self.sorter = TaskSorter()
        self.plugins = PluginManager()
        self.efimera = EfimeraManager(self.plugins)
        self.running = True
        self.night_optimizer_active = False
        self.night_thread = None

    def run(self):
        print("[Orchestrator] Запуск Jarvis‑COS.")
        self._start_night_optimizer()
        try:
            while self.running:
                tasks = self.sensors.fetch_tasks() + self.emulator.get_demo_tasks()
                sorted_tasks = self.sorter.sort(tasks)
                for task in sorted_tasks:
                    self.efimera.spawn(task)   # обрабатывается эфемерным воркером
                time.sleep(2)
        except KeyboardInterrupt:
            self.running = False
        self._stop_night_optimizer()
        print("[Orchestrator] Остановка Jarvis‑COS.")

    # --- NightOptimizer ---
    def _start_night_optimizer(self):
        if not self.night_optimizer_active:
            self.night_optimizer_active = True
            self.night_thread = threading.Thread(target=self._night_optimizer_loop, daemon=True)
            self.night_thread.start()
            print("[NightOptimizer] Started")

    def _stop_night_optimizer(self):
        if self.night_optimizer_active:
            self.night_optimizer_active = False
            print("[NightOptimizer] Stopped")

    def _night_optimizer_loop(self):
        while self.night_optimizer_active:
            now = datetime.now().time()
            if ttime(0, 0) <= now <= ttime(6, 0):
                print("[NightOptimizer] Ночной когнитивный цикл — анализ состояния и чистка памяти...")
                if len(self.memory.archive) > 0:
                    self.memory.archive.clear()
                    print("[NightOptimizer] Archive очищен")
            time.sleep(60)
