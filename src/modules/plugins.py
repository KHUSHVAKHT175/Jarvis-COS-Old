class PluginManager:
    def execute(self, task):
        print(f"[PluginManager] Выполнение: {task['name']} [{task['type']}]")
        return f"result_{task['payload']}"
