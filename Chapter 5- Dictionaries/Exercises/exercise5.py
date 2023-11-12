# Make an empty list to store the pets in.
pets = []

# Make individual pets, and store each one in the list.
pet = {
    'animal type': 'snake',
    'name': 'rio',
    'owner': 'suneel',
    'age': 4,
    'eats': 'rats',
}
pets.append(pet)

pet = {
    'animal type': 'cat',
    'name': 'dolly',
    'owner': 'adnan',
    'age': 1,
    'eats': 'meat and chicken',
}
pets.append(pet)

pet = {
    'animal type': 'bird',
    'name': 'michael',
    'owner': 'franklin',
    'age': 2,
    'eats': 'seeds',
}
pets.append(pet)

# Display information about each pet.
for pet in pets:
    print("\nHere's what I know about " + pet['name'].title() + ":")
    for key, value in pet.items():
        print("\t" + key + ": " + str(value))