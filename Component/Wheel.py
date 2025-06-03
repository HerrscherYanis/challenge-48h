from machine import Pin

class Wheel():
    def __init__(self, wheel_Left_Back, wheel_Right_Back, wheel_Left_Prior, wheel_Right_Prior):
        self.wheel_Left_back = Pin(wheel_Left_Back, Pin.OUT)
        self.wheel_Right_back = Pin(wheel_Right_Back, Pin.OUT)
        self.wheel_Left_Prior = Pin(wheel_Left_Prior, Pin.OUT)
        self.wheel_Right_Prior = Pin(wheel_Right_Prior, Pin.OUT)

    def move(self, pin1, pin2):
        self.wheel_Left_back.value(pin1[1])
        self.wheel_Right_back.value(pin1[0])
        self.wheel_Left_Prior.value(pin2[1])
        self.wheel_Right_Prior.value(pin2[0])
