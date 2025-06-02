from machine import Pin

class Component():
    def __init__(self, wheel_Left, wheel_Right):
        self.wheel_Left = wheel_Left
        self.wheel_Right = wheel_Right

class Robot(Component):
    def __init__(self,pin):
        super.__init__(pin)

    
    def move(self, value):
        self.wheel_Left.value(value)
        self.wheel_Right.value(value)
