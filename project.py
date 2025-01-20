name = input("Enter your name: ")
print("Hello " + name + " welcome to my game")

should_we_play = input("DO you want to play? ")
play = should_we_play.lower() == "yes"

if should_we_play == "yes" or should_we_play == 'Yeah':
    print("we gonna play!")

weapon = input("Chose the weapon(M4/AK47): ").lower()
if weapon == "m4":
    print("burst")
else:
    print("single")

direction = input("Do you want to go (left/right)? ").lower()
if direction == "right":
    print("you are going to right")

choice = input("select the way for next (bike/bus) ")
if choice == "bike":
    print("you will be reached 20mins faster from bus")
elif choice == "bus":
    print("you will be late by 20mins from bike")

elif direction == "left":
    print("you are going to left")
    choice = input("select the way for next (underwater/bridge) ")
    if choice == "underwater":
        print("you are going to underwater")
    elif choice == "bridge":
        print("you are going on the bridge")
    else:
        print("you have not chosen the correct way")

else:
    print("Game is over")