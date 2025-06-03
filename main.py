from Component.Wheel import Wheel
from Component.ultrasonic_sensor import Ultrasonic
from Component.humidity_sensor import Humidity
from Robot import Robot
from time import sleep

robot = Robot(10,11,5,6,Ultrasonic(19,18),Humidity(12))

if __name__ == "__main__":
    number = 0
    while True:
        distance = robot.UltraSonic.request_ultrasonic()
        if distance <= 8.0 and distance > 0:
            number = robot.Tourne(number)
        else:
            robot.order_robot("forward")
            number = 0
        sleep(0.1)