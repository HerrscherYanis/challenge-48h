from machine import Pin
import dht

class Humidity():
    def __init__(self, sensor):
        self.sensor = dht.DHT11(Pin(sensor))
    
    def request_humidity(self):
        try:
            self.sensor.measure()
            print(f"Temperature : {self.sensor.temperature():.1f}")
            print(f"Humidite    : {self.sensor.humidity():.1f}")
        except OSError as e:
            print('Echec reception')