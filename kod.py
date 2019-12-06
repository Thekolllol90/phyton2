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


