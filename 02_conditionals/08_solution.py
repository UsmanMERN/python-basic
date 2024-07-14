password = input("Enter Password to check strength \n")

password_length = len(password)

if password_length < 6:
    password_strength = "Week"
elif password_length <= 10:
    password_strength = "Medium"
elif password_length > 10:
    password_strength = "Strong"

print("Your password is", password_strength)
