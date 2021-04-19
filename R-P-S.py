import random

ai = ["R", "P", "S"]

aich = random.choice(ai)

ipick = input("pick R-P-S  :")
print("i pick " + aich)

if ipick == "R":
    if aich == "R":
        print("ti")
    elif aich == "P":
        print("you los")
    elif aich == "S":
        print("you win")
elif ipick == "P":
    if aich == "P":
        print("ti")
    elif aich == "S":
        print("you los")
    elif aich == "R":
        print("you win")
elif ipick == "S":
    if aich == "S":
        print("ti")
    elif aich == "R":
        print("you los")
    elif aich == "P":
        print("you win")
    else:
        print("invaled anser cap R-P-S")
else:
    print("invaled anser cap R-P-S")
input("pres enter")
