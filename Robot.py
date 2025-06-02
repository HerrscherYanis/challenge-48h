from Component.Wheel import Wheel
from Component.ultrasonic_sensor import Ultrasonic
from Component.humidity_sensor import Humidity

class Robot(Wheel):
    def __init__(self,wheel_Left_Back, wheel_Right_Back, wheel_Left_Prior, wheel_Right_Prior):
        Wheel.__init__(wheel_Left_Back, wheel_Right_Back, wheel_Left_Prior, wheel_Right_Prior)

    def Addon(self, add_class):
        self.addon = {add_class.name : add_class}
        
    def order_robot(self, direction):
        if direction is "Forward":
            self.move(1, 1)
        elif direction is "backward":
            self.move(-1, -1)
        elif direction is "left":
            self.move(-1, 1)
        elif direction is "right":
            self.move(1, -1)
        
        
