class Orchestrator:
    def __init__(self):
        from core.emulator import Emulator
        from core.memory import HybridMemory
        from core.sensors import SensorManager
        from core.sorter import TaskSorter
        from modules.plugins import PluginManager
        self.emulator = Emulator()
        self.memory = HybridMemory()
        self.sensors = SensorManager()
        self.sorter = TaskSorter()
        self.plugins = PluginManager()
        self.running = True

    def run(self):
        print("[Orchestrator] Запуск Jarvis-COS.")
        while self.running:
            tasks = self.sensors.fetch_tasks() + self.emulator.get_demo_tasks()
            sorted_tasks = self.sorter.sort(tasks)
            for task in sorted_tasks:
                result = self.plugins.execute(task)
                self.memory.store(task, result)
            # Можно добавить логику Watchdog, авто-очистки, адаптации и др.
            break  # Убрать break для постоянного цикла!
