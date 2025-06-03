from Component.Wheel import Wheel
from Component.ultrasonic_sensor import Ultrasonic
from Component.humidity_sensor import Humidity

class Robot(Wheel, Ultrasonic, Humidity):
    def __init__(self, pin_wheel, pin_sonic, pin_humidity=None):
        Wheel.__init__(self, pin_wheel[0], pin_wheel[1], pin_wheel[2], pin_wheel[3])
        self.Addon(pin_sonic, pin_humidity)

    def Addon(self, pin_sonic, pin_humidity):
        #add other sensore in Robot.
        #self.addon = {add_class.name : add_class}
        try:
            Ultrasonic.__init__(self, pin_sonic[0],pin_sonic[1])
        except:
            print("module UltraSonic sensor not found !")
        try:
            Humidity.__init__(self, pin_sonic)
        except:
            print("module Humidity sensor not found !")

    def order_robot(self, direction):
        if direction is "forward":
            self.move([1,0], [1,0])
        elif direction is "backward":
            self.move([0,1], [0,1])
        elif direction is "left":
            self.move([1,0], [0,1])
        elif direction is "right":
            self.move([0,1], [1,0])
        elif direction is "stop" or direction is None:
            self.move(0, 0)

    def Tourne(self, number):
        distance = self.request_ultrasonic()
        if distance <= 8.0 and distance > 0 and number <= 25:
            self.order_robot("right")
        else:
            self.order_robot("left")
        return number + 1