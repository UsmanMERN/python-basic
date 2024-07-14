distance = input("Enter the Distance \n")
distance_in_int = int(distance)
if distance_in_int < 3:
    transport = "Go and walk"
elif distance_in_int <= 15:
    transport = "Go with Bike"
elif distance_in_int > 15:
    transport = "Go with a car"

print(transport)
