from Component.Wheel import Wheel 

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
        
        
