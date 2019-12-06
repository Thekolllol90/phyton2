password = "12345"
passwordLength = 5

currentAttempt = ""

changePassword = False
correctPassword = False

while True:
    current = input("Write: ")[0]
    if current == "C":
        currentAttempt = ""
        continue
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
