get_age = input("Enter your age: \n")
get_day = input("Enter your day: \n")

age_in_int = int(get_age)
ticket_price = 12 if age_in_int >= 18 else 8

if get_day == "wednesday":
    # ticket_price = ticket_price - 2
    ticket_price -= 2

print("you ticket price $", ticket_price)
