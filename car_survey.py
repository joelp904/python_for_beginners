# Used Car survey title
#######################################################
print("!!!!!!!!!!!!!!!!!!!!!")
print("Blue Collar Used Cars")
print("!!!!!!!!!!!!!!!!!!!!!")
print()
print("Please fill out our in-depth Used car survey")
print("For multiple choice questions please enter the letter")
print("of the selection that you're looking for.")
print()
#######################################################

print("~Contact information section~")
# Ask the user to enter full name
firstName = input("Enter First name: ")
firstName = firstName.capitalize()
lastName = input("Enter Last name: ")
lastname = lastName.capitalize()
# Ask the user to enter email
email = input("Enter Email: ")
# Ask the user to enter phone number
phoneNumber = input("Please enter your phone number: ")
print()

# Ask the user to select Car Make
print("~Make~")
print("Select car make offered by Blue Collar: ")
print("    a. Honda")
print("    b. Toyota")
print("    c. Subaru")
print("    d. Mazda")
make = input("Enter your choice (a-d): ")
print()

# Ask the user to select Car type
print("~Type~")
print("Select car type: ")
print("    a. Sedan")
print("    b. SUV")
print("    c. Truck")
print("    d. Van")
type = input("Enter your choice (a-d): ")
print()

# Ask the user to select Trim type
print("~Trim~")
print("Select trim type")
print("    a. Economy")
print("    b. Upgraded")
print("    c. Luxury")
print("    d. Performance")
trim = input("Enter your choice (a-d): ")
print()

# Ask the user to select milage range
print("~Mileage~")
print("Select milage range")
print("    a. 0-25,000")
print("    b. 25,000-50,000")
print("    c. 50,000-75,000")
print("    d. 75,000+")
mileage = input("Enter your choice (a-d): ")
print()

# Ask the user to input color
print("~Color~")
color = input("Enter Color: ")
print()

# Print the survery summary
print("~Summary~")
print("Contact information: ")
print(f"Name: {firstName} {lastName}")
print(f"Email: {email}")
print(f"Phone number: {phoneNumber}")
print(f"Make: {make}")
print(f"Type: {type}")
print(f"Trim: {trim}")
print(f"Mileage: {mileage}")
print(f"Color: {color}")
