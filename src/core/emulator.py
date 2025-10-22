class Emulator:
    def get_demo_tasks(self):
        # Пример тестовых задач
        return [
            {"name": "demo_task_1", "type": "compute", "payload": "42"},
            {"name": "demo_task_2", "type": "sensor", "payload": "temp23"}
        ]
