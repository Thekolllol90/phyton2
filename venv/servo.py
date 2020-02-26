import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)

GPIO.setup(7, GPIO.OUT)

p = GPIO.PWM(7, 50)
p.start(7.5)

try:
    while True:
        p.changeDutyCycle(7.5)
        time.sleep(1)
        p.changeDutyCycle(12.5)
        time.sleep(1)
        p.changeDutyCycle(2.5)
        time.sleep(1)
except KeyboardInterrupt:
    p.stop()

    GPIO.cleanup()
