import json
import os

BRAIN_PATH = "src/core/brain.json"
MEMORY_PATH = "src/core/memexp.json"

def load_brain():
    if os.path.exists(BRAIN_PATH):
        with open(BRAIN_PATH, encoding="utf-8") as f:
            return json.load(f)
    else:
        return {}

def save_brain(brain):
    with open(BRAIN_PATH, "w", encoding="utf-8") as f:
        json.dump(brain, f, ensure_ascii=False, indent=2)

def load_exp():
    if os.path.exists(MEMORY_PATH):
        with open(MEMORY_PATH, encoding="utf-8") as f:
            return json.load(f)
    return {}

def save_exp(exp):
    with open(MEMORY_PATH, "w", encoding="utf-8") as f:
        json.dump(exp, f, ensure_ascii=False, indent=2)

def fuzzy_find(u, brain_dict):
    # Фуззи: ищет подстроку из вопроса
    for key in brain_dict:
        if key in u or u in key:
            return brain_dict[key]
    return None

def show_memory(memory):
    print("=== Память Джарвиса ===")
    print("Cache:", memory.cache)
    print("Archive:", memory.archive)
    print("Weights:", memory.weights)
    print("========================")
    # показываем живой опыт (расширенные ответы)
    exp = load_exp()
    print("Живой опыт:", exp)
    print("========================\n")

def chat(memory):
    # brain.json — стартовая база знаний,
    # memexp.json (или память) — опыт, расширение, автообучение
    brain = load_brain()
    exp = load_exp()
    print("=" * 24)
    print("JARVIS‑COS: Интерактивный диалог (развитый интеллект)")
    print("=" * 24)
    print("Набери 'выход' или 'stop' для завершения.\n'память' — показать содержимое памяти.\n'опыт' — вывести добавленные знания.")
    print("Команда 'научи' — добавить новую связь (пример: научи вопрос:ответ)\n")
    while True:
        user = input("Ты: ").strip()
        u = user.lower()
        if u in ("выход", "stop", "exit"):
            print("Возвращаюсь в главное меню...")
            break
        elif u == "память":
            show_memory(memory)
        elif u == "опыт":
            exp = load_exp()
            print("Живой опыт:", exp)
        elif u.startswith("научи"):
            # научи вопрос:ответ
            try:
                s = user[len("научи"):].strip()
                key, val = map(str.strip, s.split(":", 1))
                # записать живой опыт не только в файл, но и в HybridMemory
                exp[key] = val
                save_exp(exp)
                memory.store({"name": key}, val)
                print(f"Jarvis: Теперь знаю — '{key}' даёт '{val}'.")
            except Exception:
                print("Jarvis: Формат — научи вопрос:ответ")
        else:
            # Ищем в brain.json, потом живой опыт, потом в HybridMemory (фуззи)
            answer = fuzzy_find(u, brain)
            if not answer:
                answer = fuzzy_find(u, exp)
            if not answer:
                # Фуззи по HybridMemory cache:
                for k, v in memory.cache.items():
                    if k in u or u in k:
                        answer = v
                        break
            if answer:
                print(f"Jarvis: {answer}")
            else:
                print(f"Jarvis: Я услышал — '{user}'. Научи меня новому через 'научи вопрос:ответ', и я не забуду! Уровень интеллекта растёт с твоим опытом.")
