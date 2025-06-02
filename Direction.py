from machine import Pin
from time import sleep
import dht

class ultrasonic():
    def __init__(self, sensor):
        self.sensor = Pin(sensor)

    def request_ultrasonic():
        pass
    
class humidity():
    def __init__(self, sensor):
        self.sensor = dht.DHT11(Pin(sensor))
    
    def request_humidity(self):
        try:
            self.sensor.measure()
            print(f"Temperature : {self.sensor.temperature():.1f}")
            print(f"Humidite    : {self.sensor.humidity():.1f}")
        except OSError as e:
            print('Echec reception')

class Wheel():
    def __init__(self, wheel_Left_Back, wheel_Right_Back, wheel_Left_Prior, wheel_Right_Prior):
        self.wheel_Left_back = Pin(wheel_Left_Back)
        self.wheel_Right_back = Pin(wheel_Right_Back)
        self.wheel_Left_Prior = Pin(wheel_Left_Prior)
        self.wheel_Right_Prior = Pin(wheel_Right_Prior)

    def move(self, Value_Left, Value_Right):
        self.wheel_Left.value(Value_Left)
        self.wheel_Right.value(Value_Right)
        self.wheel_Left.value(Value_Left)
        self.wheel_Right.value(Value_Right)

class Robot(Wheel):
    def __init__(self,wheel_Left_Back, wheel_Right_Back, wheel_Left_Prior, wheel_Right_Prior):
        super.__init__(wheel_Left_Back, wheel_Right_Back, wheel_Left_Prior, wheel_Right_Prior)

    def order_robot(self, direction):
        if direction is "Forward":
            self.move(1, 1)
        elif direction is "backward":
            self.move(-1, -1)
        elif direction is "left":
            self.move(-1, 1)
        elif direction is "right":
            self.move(1, -1)
        
        
