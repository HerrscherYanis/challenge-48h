from machine import Pin

class Component():
    def __init__(self, wheel_Left_Back, wheel_Right_Back, wheel_Left_Prior, wheel_Right_Prior):
        self.wheel_Left_back = wheel_Left_Back
        self.wheel_Right_back = wheel_Right_Back
        self.wheel_Left_Prior = wheel_Left_Prior
        self.wheel_Right_Prior = wheel_Right_Prior

class Robot(Component):
    def __init__(self,pin):
        super.__init__(pin)

    
    def move(self, Value_Left, Value_Right):
        self.wheel_Left.value(Value_Left)
        self.wheel_Right.value(Value_Right)
        self.wheel_Left.value(Value_Left)
        self.wheel_Right.value(Value_Right)

    def Commend_Robot(self, direction):
        if direction is "Forward":
            self.move(1, 1)
        elif direction is "backward":
            self.move(-1, -1)
        elif direction is "left":
            self.move(-1, 1)
        elif direction is "right":
            self.move(1, -1)
        
        
