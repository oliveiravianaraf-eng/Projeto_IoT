from python_iot.sensors import DHTSensor, BH1750
import time


def setup():
    """Perform initialization that would normally occur in Arduino setup()."""
    print("Initializing sensors...")
    dht = DHTSensor()
    bh = BH1750()
    return {"dht": dht, "bh": bh}


def loop(context):
    """Simulate a single iteration of the Arduino loop()."""
    dht = context["dht"]
    bh = context["bh"]
    data = {}
    data.update(dht.read())
    data["lux"] = bh.read_lux()
    print("Sensor data:", data)
    return data


if __name__ == "__main__":
    ctx = setup()
    # run a few iterations as a demonstration
    for _ in range(3):
        loop(ctx)
        time.sleep(1)
