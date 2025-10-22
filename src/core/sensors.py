class SensorManager:
    def __init__(self):
        self.sensors = []

    def register(self, func):
        self.sensors.append(func)

    def fetch_tasks(self):
        tasks = []
        # Встроенные тестовые сенсоры, можно добавлять свои
        def temp_sensor():
            return [{"name": "sensor_temp", "type": "sensor", "payload": "28.1"}]
        def humidity_sensor():
            return [{"name": "sensor_hum", "type": "sensor", "payload": "60%"}]
        # Регистрируем встроенные при запуске
        if not self.sensors:
            self.register(temp_sensor)
            self.register(humidity_sensor)
        for s in self.sensors:
            tasks.extend(s())
        return tasks
