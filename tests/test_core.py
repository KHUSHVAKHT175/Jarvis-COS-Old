# tests/test_core.py

from src.core.memory import HybridMemory
from src.core.sorter import TaskSorter
from src.core.emulator import Emulator

def test_memory_store_and_get():
    mem = HybridMemory()
    task = {"name": "t1", "type": "compute", "payload": "1"}
    mem.store(task, "res1")
    assert mem.get("t1") == "res1"

def test_task_sorting():
    sorter = TaskSorter()
    tasks = [
        {"name":"a","type":"sensor"}, 
        {"name":"b","type":"compute"}
    ]
    sorted_tasks = sorter.sort(tasks)
    assert sorted_tasks[0]["type"] == "compute"

def test_emulator_generation():
    emu = Emulator()
    demo = emu.get_demo_tasks()
    assert isinstance(demo, list)
    assert len(demo) > 0

# Запуск: python -m pytest
