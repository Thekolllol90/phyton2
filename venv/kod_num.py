
import Rpi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)

NUMPAD = [[1, 2, 3, 'A'],
          [4, 5, 6, 'B'],
          [7, 8, 9, 'C'],
          ['*', 0, '#', 'D']]

ROW = [7, 11, 13, 15]
COL = [12, 16, 18, 22]

password = "12345"
passwordLength = 5

currentAttempt = ""

changePassword = False
correctPassword = False

for  j in range(4) :
    GPIO.setup(COL[j], GPIO.OUT)
    GPIO.output(COL[j], 1)

for i in range(4) :
    GPIO.setup(ROW[i], GPIO.IN, pull_up_down = GPIO.PUD_UP)

def numpadInput():
    while (True):
        for j in range(4):
            GPIO.output(COL[j], 0)
            for i in range(4):
                if GPIO.input(ROW[i]) == 0:
                    return NUMPAD[i][j]
                    time.sleep(0.3)
                    #GPIO.cleanup()
                    while (GPIO.input(ROW[i]) == 0):
                        pass

            GPIO.output(COL[j], 1)


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
                currentAttempt = ""
                correctPassword = True
            else:
                print("Incorrect")
                currentAttempt = ""
                correctPassword = False
