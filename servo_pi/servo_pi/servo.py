import RPi.GPIO as GPIO
import time


class Servo:
    pin = 18

    def __init__(self, pin):
        ####################################################
        # __inti__(self, pin) - Instantiates a new servo object, controlled
        # by the pin input
        #
        # Inputs:
        #   pin - Pin to control the servo with

        self.pin = pin

        GPIO.setmode(GPIO.BOARD)
        GPIO.setup(self.pin, GPIO.OUT)
        self.pwm = GPIO.PWM(pin, 100)
        self.pwm.start(5)

    def set_position(self, val):
        ####################################################
        # set_position(self, val) - Moves the servo to the specified position
        #
        # Inputs:
        #   val - Position to set the servo to, a value between 0 - 180

        duty = float(val) / 10.0 + 2.5
        self.pwm.ChangeDutyCycle(duty)
        time.sleep(0.5)
        self.pwm.ChangeDutyCycle(duty)
        time.sleep(0.5)