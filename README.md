# servo-pi
This is a package that makes interfacing with servo motors using a Raspberry Pi straightforward.

Dependencies:

  *RPi.GPIO
  *time

## Installation
To install, start with cloning this repository. 
```
cd ~
git clone https://github.com/kcydesu/servo-pi.git
cd servo_pi/servo_pi
```
Once in this directory, you just need to use pip3 in order to install the package.
```
pip3 install -e .
```

## Usage
Before using this package, make sure that it was installed correctly by using the following command.
```
pip3 show servo_pi
```

If this was installed correctly, the next step is to wire your servo motor. Although all servo motors have a slightly different configuration, any PWM Analog Servo requires a power supply, ground, and a data pin. Using the datasheet for your particular servo and the Raspberry Pi GPIO shown below, connect your servo and remember the pin number for the data pin (the board pin not the GPIO pin!).

![Raspberry Pi 3 B+ GPIO](https://github.com/kcydesu/servo-pi/blob/master/pictures/introduction-to-raspberry-pi-3-b-plus-2.png)

After connecting your servo, the software part of this project is straightforward.

In order to use this class you must first import it into your document. Then, you can instantiate a Servo object and provide the control pin as an argument. There is then a ```set_position(val)``` method that allows you move the servo.

```
from servo_pi.servo import Servo
s1 = Servo(18)
s1.set_position(120)
```

Set position take a value from 0-180 and modified this to be the correct PWM width to move the servo. Due to some technical limitations, the servo will always move to center before making a move.
