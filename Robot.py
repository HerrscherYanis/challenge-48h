from Wheel import Wheel
from Ultrasonic_sensor import Ultrasonic
from Humidity_sensor import Humidity
import json

class Robot(Wheel):
    def __init__(self):
        with open('data.json', 'r') as file:
            self.Addon(json.load(file))

    def Addon(self, data):
        try:
            Wheel.__init__(self, data["Wheel"][0], data["Wheel"][1], data["Wheel"][2], data["Wheel"][3])
        except:
            print("module Wheel not install !")
        try:
            self.ultrasonic = Ultrasonic(self, data["Ultrasonic"][0], data["Ultrasonic"][1])
        except:
            print("module UltraSonic sensor not install !")
        try:
            self.humidity = Humidity(self, data["Humidity"][0])
        except:
            print("module Humidity sensor not install !")

    def order_robot(self, direction):
        try:
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
        except:
            print("module Wheel not found !")

    def Tourne(self, number):
        try:
            distance = self.ultrasonic.request_ultrasonic()
            if distance <= 8.0 and distance > 0 and number <= 25:
                self.order_robot("right")
            else:
                self.order_robot("left")
            return number + 1
        except:
            print("module UltraSonic sensor not found !")

