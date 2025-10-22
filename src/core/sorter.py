class TaskSorter:
    def sort(self, tasks):
        # Явная приоритезация: 'compute' выше, чем 'sensor'
        priority = {'compute': 2, 'sensor': 1}
        return sorted(tasks, key=lambda x: priority.get(x['type'], 0), reverse=True)
