import wiringpi as wp


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
        wp.wiringPiSetupGpio()

        # Sets the specified pin as an pwm output, and makes it millisecond mode
        wp.pinMode(pin, wp.GPIO.PWM_OUTPUT)
        wp.pwmSetMode(wp.GPIO.PWM_MODE_MS)

        # Sets the clock and range values to correctly divide the clock
        wp.pwmSetClock(192)
        wp.pwmSetRange(2000)


    def set_position(self, val):
        ####################################################
        # set_position(self, val) - Moves the servo to the specified position
        #
        # Inputs:
        #   val - Position to set the servo to, a value between 0 - 1

        pulse = (val * 200) + 50

        wp.pwmWrite(self.pin, int(pulse))