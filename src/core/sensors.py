class SensorManager:
    def fetch_tasks(self):
        # Пример генерации новых задач
        return [
            {"name": "sensor1_temp", "type": "sensor", "payload": "25.6"},
            {"name": "sensor2_humidity", "type": "sensor", "payload": "60%"}
        ]
