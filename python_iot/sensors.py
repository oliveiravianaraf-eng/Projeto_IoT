import random

class DHTSensor:
    """Simulated DHT22 sensor returning temperature and humidity."""
    def __init__(self, name="DHT22"):
        self.name = name

    def read(self):
        # return temperature (°C) and humidity (%) as a dict
        temp = round(random.uniform(15, 35), 1)
        hum = round(random.uniform(20, 90), 1)
        return {"temperature": temp, "humidity": hum}


class BH1750:
    """Simulated light sensor returning lux values."""
    def __init__(self):
        pass

    def read_lux(self):
        return round(random.uniform(0, 1000), 1)
