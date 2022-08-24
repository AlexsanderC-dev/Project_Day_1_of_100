# 1. Greating.
print("This is your brand name generator\n")

# 2. Ask the user for the city that they grew up in.
grew_up_country = input("What's the name of country you grew up in?\n\n")

# 3. Ask if the user for the name of a pet.
have_pet = input("\nDo you have a pet? Y/N: \n\n")

# 4. If you have_pet = yes. Ask the user for the name of a pet.
if 'Y'.lower() == have_pet:
    pet_name: str = input("\nWhat's your pet name?\n\n")
if 'N'.lower() == have_pet:
    pet_name: str = input("\nSorry, you don't deserve a brand name :-(, but let's see what we can get for you, "
                          "keep going \n\n")

# 5 .Ask the user for the name of their favorite food.
food_name = input("\nWhat's your favorite food or drink?\n\n")

# 6. Combine the name of their city and pet and show them their band name.
# noinspection PyUnboundLocalVariable
band_name = f"{pet_name} {grew_up_country} {food_name}"
print("\nYour brand name could be :\n\n {0}".format(band_name))
