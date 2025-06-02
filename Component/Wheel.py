from machine import Pin
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
