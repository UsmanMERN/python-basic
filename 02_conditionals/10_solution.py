pet_specie = input("Enter the pet specie \n")
pet_age = input("Enter the pet age \n")

pet_age_to_int = int(pet_age)

if pet_specie == "Cat":
    if pet_age_to_int > 5:
        pet_food = "Senior cat food"
    else:
        pet_food = "junior cat food"
elif pet_specie == "Dog":
    if pet_age_to_int < 2:
        pet_food = "Puppy Food"
    else:
        pet_food = "adult Dog food"
else:
    pet_food = "These species are not yet categorize"

print(pet_food)
