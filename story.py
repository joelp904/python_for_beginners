# Title
print("~Zombie Apocalypse~")
print()

# Inital setup
print("It's year 2027, two years after the the inital outbreak of the infection.")
print("You suddenly awake to a loud thud that echoes off in the distance.")
print("As you awake you slowly acclimate to your surrounds, you're in your house that")
print("has been fortified from the outside; a zombie must be attempting to break into your house!!")
print()

# Storyline selection
print("You quickly think about what to do: ")
print("    1. Go outside and attempt to kill the zombie to protect your house")
print("    2. Do nothing")
print("    3. Stay inside and attempt to kill the zombie from the safety of your house")
storyline = input("Enter 1-3: ")
storyline= int(storyline)
print()

# Storyline 1
if (storyline == 1):
  # Weapon Selection
  print("As you are leaving your room, you see some weapons at your disposal")
  print("Which weapon will you choose?")
  print("    1. Shotgun")
  print("    2. Hachet")
  print("    3. Samurai Sword")
  print("    4. Pistol")
  weapon  = input("Enter 1-4: ")
  weapon = int(weapon)
  print()
  if (weapon == 1):
     weapon_str = "shotgun"
     gun = True
  if (weapon == 2):
     weapon_str = "hachet"
     gun = False
  if (weapon == 3):
     weapon_str = "samurai sword"
     gun = False
  if (weapon == 4):
     weapon_str = "pistol"
     gun = True
  print("You go down the stairs and go toward the front door where the sound was originating")
  print("You unbarricade and unlock the door to engage with the zombie")
  print("as you approach the zombie seems unphased by your movement, unaware you are approaching")
  if(gun == True):
    print("You notice a brick on the ground that could be used as a weapon")
    print("    1. Use gun?") 
    print("    2. Pickup brick?")
    decision = input("Enter 1-2: ")
    decision = int(decision)
    print()
    if(decision == 1):
      print(f"You raise your {weapon_str}, aim, and fire!")
      print(f"You continue to fire your {weapon_str}, but it seems to continue to attract more and more zombies")
      print("The zombies overcome you")
      print()
      print("You're now walking flesh - you've become a zomie")
    else:
      print("You slowly sneak-up on the zombie and smash it over the head with the brick")
      print("The zombie dies")
      print()
      print("You fight to live another day in this ~Zombie Apocalypse~!")
  else:
      print(f"You slowly sneak-up on the zombie using your {weapon_str} you slice its head off clean")
      print("The zombie dies")
      print()
      print("You fight to live another day in this ~Zombie Apocalypse~!")

# Storyline 2
if (storyline == 2):
  # Storyline 2 intro
  print("You sit there in your bed scared, frozen, hearing bang after bang, what is going to happen next?")
  print("bang BANG BANG - it seems as though zombies are starting to collect from the noise")
  print("The zombies finally break through the makeshift barrier you orignally setup")
  print("Do you still want to do nothing?")
  print("    1. Do nothing")
  print("    2. Get up and fight!")
  decision2_1 = input("Enter 1-2: ")
  decision2_1 = int(decision2_1)
  print()
  if (decision2_1 == 1):
    print("The zombies devour you in an instant")
    print()
    print("You're now walking flesh - you've become a zombie")
  else:
    # Weapon Selection
    print("As you are leaving your room, you see some weapons at your disposal")
    print("Which weapon will you choose?")
    print("    1. Shotgun")
    print("    2. Hachet")
    print("    3. Samurai Sword")
    print("    4. Pistol")
    weapon  = input("Enter 1-4: ")
    weapon = int(weapon)
    print()
    if (weapon == 1):
       weapon_str = "shotgun"
       gun = True
    if (weapon == 2):
       weapon_str = "hachet"
       gun = False
    if (weapon == 3):
       weapon_str = "samurai sword"
       gun = False
    if (weapon == 4):
       weapon_str = "pistol"
       gun = True
    print("You meet the zombies at the staircase as they make their way up.")
    if (gun == True):
      print(f"You raise your {weapon_str}, aim, and fire!")
      print(f"You continue to fire your {weapon_str}, but it seems to continue to attract more and more zombies")
      print("The zombies overcome you")
      print()
      print("You're now walking flesh - you've become a zomie")
    else:
      print(f"You draw your {weapon_str}, and start to slaughter each zombie one-by-one")
      print("You finally kill what looks to be the last zombie")
      print()
      print("You fight to live another day in this ~Zombie Apocalypse~!")

# Storyline 3
if (storyline == 3):
  # Weapon Selection
  print("As you are leaving your room, you see some weapons at your disposal")
  print("Which weapon will you choose?")
  print("    1. Shotgun")
  print("    2. Hachet")
  print("    3. Samurai Sword")
  print("    4. Pistol")
  weapon  = input("Enter 1-4: ")
  weapon = int(weapon)
  print()
  if (weapon == 1):
     weapon_str = "shotgun"
     gun = True
  if (weapon == 2):
     weapon_str = "hachet"
     gun = False
  if (weapon == 3):
     weapon_str = "samurai sword"
     gun = False
  if (weapon == 4):
     weapon_str = "pistol"
     gun = True
  print("You slowly make your way down stairs and over to the window")
  print("[Narrator]: Alright, don't let this break the immersion of the ~Zombie Apacolypse~ storyline,")
  print("            but if you'd like, you can choose to kill the next zombie by solving a riddle!")
  print("            Enter 1: Solve riddle")
  print("            Enter 2: To use weapon")
  decision = input("            :")
  decision = int(decision)
  if (decision == 1):
    print("Beets, bears, Battlestar Galactica?")  
    print("  1. Beets")
    print("  2. Bears")
    print("  3. Battlestart Galactica")
    print("  4. Michael!!!")
    decision = input("Enter 1-4: ")
    decision = int(decision)
    print("")
    if (decision == 1 or decision == 2 or decision == 3):
      print("Incorrect! Your not an Office fan?!")
      print("The zombies sense that you're not an Office Fan and overcome you")
      print()
      print("You're now walking flesh - you've become a zomie")
    else:
      print("Correct!")
      print("The Zombie suddenly falls over, dead")
      print()
      print("You fight to live another day in this ~Zombie Apocalypse~!")
  else:
    if (weapon == 4):
      print(f"You raise your {weapon_str} through the barricade of the window, aim, and fire!")
      print(f"The house absorbs most of the noise from the gun")
      print()
      print("You fight to live another day in this ~Zombie Apocalypse~!")
    elif(weapon == 2 or weapon == 3):
      print(f"You swing your {weapon_str} through the barricade of the window and stab the zombie in the head")
      print()
      print("You fight to live another day in this ~Zombie Apocalypse~!")
    else:
      print(f"You raise your {weapon_str} through the barricade of the window, aim, and fire!")
      print(f"The noise of the {weapon} seems to attract more zombies")
      print()
      print("You fight to live another day in this ~Zombie Apocalypse~!")
      print("The zombies overcome you")
      print()
      print("You're now walking flesh - you've become a zomie")
