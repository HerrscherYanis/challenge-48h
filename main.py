from Wheel import Wheel
from Ultrasonic_sensor import Ultrasonic
from Humidity_sensor import Humidity
from Robot import Robot
from time import sleep


if __name__ == "__main__":
    robot = Robot()
    number = 0
    while True:
        distance = robot.request_ultrasonic()
        if distance <= 8.0 and distance > 0:
            number = robot.Tourne(number)
        else:
            robot.order_robot("forward")
            number = 0
        sleep(0.1)