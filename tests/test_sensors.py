import pytest
from python_iot.sensors import DHTSensor, BH1750


def test_dht_read():
    dht = DHTSensor()
    reading = dht.read()
    assert "temperature" in reading
    assert "humidity" in reading
    assert isinstance(reading["temperature"], float)
    assert isinstance(reading["humidity"], float)


def test_bh_read():
    bh = BH1750()
    lux = bh.read_lux()
    assert isinstance(lux, float)
    assert 0 <= lux <= 1000
