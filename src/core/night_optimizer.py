# src/core/night_optimizer.py
def run_night_cycle(memory, active=True):
    from datetime import datetime, time as ttime
    now = datetime.now().time()
    if active and ttime(0, 0) <= now <= ttime(6, 0):
        print("[NightOptimizer] Ночной когнитивный цикл — анализ и подстройка опыта...")
        # вызов автоподстройки только если этот модуль есть в списке
        memory.night_optimize_weights()
        if len(memory.archive) > 0:
            memory.archive.clear()
            print("[NightOptimizer] Archive очищен")
