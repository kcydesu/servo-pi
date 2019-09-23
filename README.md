# servo-pi
This is a package that makes interfacing with servo motors using a Raspberry Pi straightforward.

## Installation
To install, start with cloning this repository. 
```
cd ~
git clone https://github.com/kcydesu/servo-pi.git
cd servo_pi/servo_pi
```



## Usage
In order to use this class you must first import it into your document. Then, you can instantiate a Servo object and provide the control pin as an argument. There is then a ```set_position(val)``` method that allows you move the servo.

```
from servo_pi.servo import Servo
s1 = Servo(18)
s1.set_position(0.5)
```

Set position take a value from 0-1 and scales that value to represent the entire scope of possible values for the servo to take.
