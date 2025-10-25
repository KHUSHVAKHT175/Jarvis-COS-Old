# src/core/orchestrator.py (или main.py)

from modules.module_list import module_registry, age_requirements

class HybridMemory:
    def __init__(self):
        self.cache = {}
        self.archive = {}
        self.weights = {}

    def store(self, task, result):
        self.cache[task["name"]] = result
        self.weights[task["name"]] = self.weights.get(task["name"], 1.0) + 0.1
        if len(self.cache) > 10:
            key, val = self.cache.popitem()
            self.archive[key] = val

    def get(self, key):
        if key in self.cache:
            return self.cache[key]
        if key in self.archive:
            return self.archive[key]
        return None

# функция для динамического импорта разрешённых модулей
def load_allowed_modules(user_age):
    allowed = {}
    for name, path in module_registry.items():
        if user_age >= age_requirements.get(name, 0):
            allowed[name] = __import__(path, fromlist=[""])
    return allowed

# основная инициализация системы
def main():
    user_age = int(input("Введите возраст пользователя: "))
    modules = load_allowed_modules(user_age)
    memory = HybridMemory()

    print(f"Доступные модули: {list(modules.keys())}")

    # Пример автоподстройки (если модуль разрешён)
    if "AutoWeights" in modules:
        print("[Orchestrator] Автоподстройка весов памяти...")
        modules["AutoWeights"].night_optimize_weights(memory)
        print(f"Веса памяти: {memory.weights}")

    # Ночной когнитивный цикл (если модуль разрешён)
    if "NightOptimizer" in modules:
        print("[Orchestrator] Запуск NightOptimizer")
        modules["NightOptimizer"].run_night_cycle(memory, active=True)

    # Дополнительно — запуск других модулей по необходимости
    # if "SensorManager" in modules:
    #     modules["SensorManager"].scan_sensors()

    # if "LanguageModel" in modules:
    #     user_query = input("Введи вопрос для LanguageModel: ")
    #     print("Ответ:", modules["LanguageModel"].respond(user_query))

if __name__ == "__main__":
    main()
