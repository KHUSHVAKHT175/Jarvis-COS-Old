class TaskSorter:
    def sort(self, tasks):
        # Самый простой: сортировка по типу (compute > sensor)
        return sorted(tasks, key=lambda x: x["type"], reverse=True)
