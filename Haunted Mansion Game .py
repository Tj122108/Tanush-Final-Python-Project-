
print("Welcome to the Haunted Mansion!")
print("While you were walking home from school one day, you stumbled upon a mysterious mansion and decided to explore it!!!")
print("The house is dated back to the 1900s and is said to be haunted and you walk to the front door.")
print("Do you want to enter the living room or dining room?")
print("Type living room or dining room")


roomChoice = input("> ")

if(roomChoice == "living room"):
  print("You enter the living room.")
  print("As you walk in, you see a sleeping dragon guarding some gold jewelry.")
  print("Do you want to steal the jewelry from the dragon?")

  dragonChoice = input("> ")

  if(dragonChoice == "yes"):
    print("You attempt to steal the jewelry, but suddenly a trap door opens up")
    print("There are stairs and you go down it and you see a red lever")
    print("When you pull the lever the stairs than turns into a slide and you find yourself in a secret basement")
    print(" In the secret basement you suddenly find a treasure chest when you open it is full of gold")
    
          
    print
  elif(dragonChoice == "no"):
    print("You decide to not steal the dragon's jewelry.")
    print("You turn around and leave the house safely.")
    
  else:
    print("Invalid choice. Please enter yes or no.")
elif(roomChoice == "dining room"):
  print("You chose to go into the dining room.")
  print("As you walk in, you see a shiny vase on the table.")
  print("Do you want to open the vase?")


  vaseChoice = input("> ")

  if(vaseChoice == "yes"):
    print("You open the vase and find a pile of bones and You see a skull and out of the skulls eyes spiders comes out")
    print("The spiders come at you and kills you now you are dead")
  elif(vaseChoice == "no"):
    print("You decide not to open the shiny vase.")
    print("As you turn to leave, you hear a cracking sound coming from the corner.")
    print("A dark figure with glowing red eyes launches at you, knocking you unconcious")
    print("You wake up in your bed. It was all a dream.")
  else:
    print("Invalid choice. Please enter yes or no.")
else:
  print("Invalid choice. Please enter living room or dining room.")
