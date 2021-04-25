#Accept user input and make sure that it's a valid integer, repeating the loop if invalid
while True:
    try:
        userinput = int(input("Please enter an integer: "))
    except ValueError:
        print("Invalid input, try again")
        continue
    else:
        break

#Check if the integer is divisible by 4, output that it is not a leap year if not
if userinput % 4 != 0:
    userinput = str(userinput)
    print(userinput + " is not a leap year")
    quit
else:
    #Check if integer is also divisible by 100, output that it is a leap year if it is not
    if userinput % 100 != 0:
        userinput = str(userinput)
        print(userinput + " is a leap year")
        quit
    else:
        #Check if integer is also divisble by 400, output that it is a leap year if so
        # and output that it is not a leap year if it is indivisible by 400
        if userinput % 400 != 0:
                userinput = str(userinput)
                print(userinput + " is not a leap year")
                quit
        else:
            userinput = str(userinput)
            print(userinput + " is a leap year")
            quit