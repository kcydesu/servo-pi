from setuptools import setup, find_packages

setup(name='servo_pi',
      version='3.0.1',
      author='Casey Bruno',
      author_email='cabruno98@gmail.com',
      description='Library for controlling a servo using python and a Raspberry Pi',
      license='MIT',
      url='https://github.com/adafruit/Adafruit_Python_BNO055/',
      dependency_links=['https://github.com/adafruit/Adafruit_Python_GPIO/tarball/master#egg=Adafruit-GPIO-0.9.3'],
      install_requires=['RPi.GPIO'],
      packages=find_packages()
      )
