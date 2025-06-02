from machine import Pin

class Component():
    def __init__(self, pin):
        self.pin = pin

class Robot(Component):
    def __init__(self,pin):
        super.__init__(pin)

    
    def move(self, value):
        self.pin.value(1)
