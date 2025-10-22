import threading
import time
from datetime import datetime, time as ttime

from core.emulator import Emulator
from core.memory import HybridMemory
from core.sensors import SensorManager
from core.sorter import TaskSorter
from modules.plugins import PluginManager

class Orchestrator:
    def __init__(self):
        self.emulator = Emulator()
        self.memory = HybridMemory()
        self.sensors = SensorManager()
        self.sorter = TaskSorter()
        self.plugins = PluginManager()
        self.running = True
        # NightOptimizer
        self.night_optimizer_active = False
        self.night_thread = None
        # Watchdog
        self.watchdog_active = False
        self.watchdog_thread = None

    def run(self):
        print("[Orchestrator] Запуск Jarvis-COS.")
        self._start_night_optimizer()
        self._start_watchdog()
        try:
            while self.running:
                tasks = self.sensors.fetch_tasks() + self.emulator.get_demo_tasks()
                sorted_tasks = self.sorter.sort(tasks)
                for task in sorted_tasks:
                    result = self.plugins.execute(task)
                    self.memory.store(task, result)
                time.sleep(2)  # Имитация цикла, можно убрать или уменьшить
        except KeyboardInterrupt:
            self.running = False
        self._stop_night_optimizer()
        self._stop_watchdog()
        print("[Orchestrator] Остановка Jarvis-COS.")

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
                print("[NightOptimizer] Оптимизация памяти/архива...")
                if len(self.memory.archive) > 0:
                    self.memory.archive.clear()
                    print("[NightOptimizer] archive cleared")
            time.sleep(60)

    # --- Watchdog ---
    def _start_watchdog(self):
        if not self.watchdog_active:
            self.watchdog_active = True
            self.watchdog_thread = threading.Thread(target=self._watchdog_loop, daemon=True)
            self.watchdog_thread.start()
            print("[Watchdog] Started")

    def _stop_watchdog(self):
        if self.watchdog_active:
            self.watchdog_active = False
            print("[Watchdog] Stopped")

    def _watchdog_loop(self):
        while self.watchdog_active:
            print("[Watchdog] Проверка активности...")
            # Пример: если очередь пуста, значит всё работает
            # Можно добавить любую доппроверку
            time.sleep(15)
