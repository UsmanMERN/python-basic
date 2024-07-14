age = input("Enter your age: \n")

# age = 25
age_in_int = int(age)

if age_in_int < 13:
    print("YOU ARE A CHILD HAHA...!")
elif age_in_int < 20:
    print("YOU ARE A teenager...!")
elif age_in_int < 60:
    print("YOU ARE A adult...!")
else:
    print("YOU ARE A SENIOR CITIZEN...!")
