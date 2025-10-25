import json
import os
from modules.module_list import module_registry, age_requirements

MEMORY_FILE = "src/core/memory_state.json"

class HybridMemory:
    def __init__(self):
        if os.path.exists(MEMORY_FILE):
            with open(MEMORY_FILE, "r", encoding="utf-8") as f:
                try:
                    saved = json.load(f)
                except Exception:
                    saved = {}
            self.cache = saved.get("cache", {})
            self.archive = saved.get("archive", {})
            self.weights = saved.get("weights", {})
        else:
            self.cache = {}
            self.archive = {}
            self.weights = {}

    def store(self, task, result):
        self.cache[task["name"]] = result
        self.weights[task["name"]] = self.weights.get(task["name"], 1.0) + 0.1
        if len(self.cache) > 10:
            key, val = self.cache.popitem()
            self.archive[key] = val
        self.save()  # Автосейв на каждом изменении

    def get(self, key):
        if key in self.cache:
            return self.cache[key]
        if key in self.archive:
            return self.archive[key]
        return None

    def save(self):
        state = {
            "cache": self.cache,
            "archive": self.archive,
            "weights": self.weights
        }
        with open(MEMORY_FILE, "w", encoding="utf-8") as f:
            json.dump(state, f, ensure_ascii=False, indent=2)

    def clear_all(self):
        self.cache = {}
        self.archive = {}
        self.weights = {}
        self.save()

def load_allowed_modules(user_age):
    allowed = {}
    for name, path in module_registry.items():
        if user_age >= age_requirements.get(name, 0):
            allowed[name] = __import__(path, fromlist=[""])
    return allowed

def main():
    print("=" * 32)
    print(" JARVIS‑COS: Терминальный запуск")
    print("=" * 32)
    try:
        user_age = int(input("Введите возраст пользователя: "))
    except Exception:
        user_age = 0
    modules = load_allowed_modules(user_age)
    memory = HybridMemory()

    print(f"\n[Jarvis‑COS] Модули: {list(modules.keys())}")
    print("Команды: 'chat', 'exit'\n")

    while True:
        cmd = input("Jarvis‑COS> ").strip()
        if cmd == "chat":
            if "Dialog" in modules:
                modules["Dialog"].chat(memory)
            else:
                print("Модуль Dialog не доступен.")
        elif cmd in ("exit", "shutdown", "stop"):
            print("[Jarvis‑COS] Завершение работы. Goodbye!")
            break
        else:
            print("[Jarvis‑COS] Только 'chat' или 'exit'.")

if __name__ == "__main__":
    main()
