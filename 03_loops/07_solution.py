while True:
    number = input("Enter Value Between 1 and 10 \n")
    if 1 <= int(number) <= 10:
        print("Thanks")
        break
    else:
        print("Invalid Number")
