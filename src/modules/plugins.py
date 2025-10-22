class PluginManager:
    def execute(self, task):
        # Имитация обработки задачи
        print(f"[PluginManager] Выполнение: {task['name']} [{task['type']}]")
        return f"result_{task['payload']}"
