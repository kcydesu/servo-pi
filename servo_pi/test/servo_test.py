from servo_pi.servo_pi.servo import Servo


def main():
    s1 = Servo(18)
    s1.set_position(0.5)


if __name__ == '__main__':
    main()