import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)

NUMPAD = [[1, 2, 3, 'A'],
          [4, 5, 6, 'B'],
          [7, 8, 9, 'C'],
          ['*', 0, '#', 'D']]

ROW = [7, 11, 13, 15]
COL = [12, 16, 18, 22]

for j in range(4):
    GPIO.setup(COL[j], GPIO.OUT)
    GPIO.output(COL[j], 1)

for i in range(4):
    GPIO.setup(ROW[i], GPIO.IN, pull_up_down=GPIO.PUD_UP)

password = "12345"
passwordLength = 5

currentAttempt = ""

changePassword = False
correctPassword = False


def numpadInput():
    while(True):
        for j in range(4):
            GPIO.output(COL[j], 0)
            for i in range(4):
                if GPIO.input(ROW[i]) == 0:
                    time.sleep(0.3)
                    return str(NUMPAD[i][j])
                    while(GPIO.input(ROW[i]) == 0):
                        pass
            GPIO.output(COL[j], 1)


def open():
    GPIO.setup(5, GPIO.OUT)

    p = GPIO.PWM(5, 50)

    p.start(12.5)
    time.sleep(1)

    p.stop()


def close():
    GPIO.setup(5, GPIO.OUT)

    p = GPIO.PWM(5, 50)

    p.start(2.5)
    time.sleep(1)

    p.stop()


close()
while True:
    current = numpadInput()
    if current == "C":
        currentAttempt = ""
        continue
    elif current == '*':
        changePassword = True
        correctPassword = False
        currentAttempt = ""
        continue

    currentAttempt += current

    if changePassword and correctPassword:
        if len(currentAttempt) == passwordLength:
            password = currentAttempt
            currentAttempt = ""
            changePassword = False
            correctPassword = False
    else:
        if len(currentAttempt) == passwordLength:
            if currentAttempt == password:
                open()
                currentAttempt = ""
                correctPassword = True
            else:
                close()
                currentAttempt = ""
                correctPassword = False
