import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)

password = "12345"
passwordLength = 5

currentAttempt = ""

changePassword = False
correctPassword = False

while True:
    current = input("Write: ")[0]
    if current == "C":
        continue
        currentAttempt = ""
    elif current == "*":
        changePassword = True
        correctPassword = False
        currentAttempt = ""
        continue

    currentAttempt += current

    print("Current: " + currentAttempt)

    if changePassword and correctPassword:
        if len(currentAttempt) == passwordLength:
            password = currentAttempt
            currentAttempt = ""
            print("Changed password to " + password)
            changePassword = False
            correctPassword = False
    else:
        if len(currentAttempt) == passwordLength:
            if currentAttempt == password:
                print("Correct")
                GPIO.setup(7, GPIO.OUT)

                p = GPIO.PWM(7, 50)

                p.start(12.5)
                time.sleep(1)

                p.stop()
                GPIO.cleanup()

                currentAttempt = ""
                correctPassword = True
            else:
                print("Incorrect")
                currentAttempt = ""
                correctPassword = False
