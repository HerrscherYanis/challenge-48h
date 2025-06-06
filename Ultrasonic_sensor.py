import machine, time
from machine import Pin

class HCSR04:
    #Roberto Sánchez
    #Apache License 2.0. https://www.apache.org/licenses/LICENSE-2.0
    def __init__(self, trigger_pin, echo_pin, echo_timeout_us=500*2*30):
        self.echo_timeout_us = echo_timeout_us
        self.trigger = Pin(trigger_pin, mode=Pin.OUT, pull=None)
        self.trigger.value(0)
        self.echo = Pin(echo_pin, mode=Pin.IN, pull=None)
    def _send_pulse_and_wait(self):
        self.trigger.value(0)
        time.sleep_us(5)
        self.trigger.value(1)
        time.sleep_us(10)
        self.trigger.value(0)
        try:
            pulse_time = machine.time_pulse_us(self.echo, 1, self.echo_timeout_us)
            return pulse_time
        except OSError as ex:
            if ex.args[0] == 110:
                raise OSError('Out of range')
            raise ex
    def distance_mm(self):
        pulse_time = self._send_pulse_and_wait() 
        mm = pulse_time * 100 // 582
        return mm
    def distance_cm(self):
        pulse_time = self._send_pulse_and_wait()
        cms = (pulse_time / 2) / 29.1
        return cms


class Ultrasonic(HCSR04):
    def __init__(self, trigger, echo, echo_timeout_us=10000):
        HCSR04.__init__(self, trigger, echo, echo_timeout_us)
    
    def request_ultrasonic(self):
        distance = self.distance_cm()
        return distance
