from os import system

# This function is used to check if the traveler is arthur or not.
def name_check(name):
    if name.lower() == "arthur":
        print("My liege! You may pass!")
        exit()

# This function is used to check if the traveler is on the correct quest or not.
def quest_check(quest):
    if ("grail" not in quest.lower()):
        print("Only those who seek the Grail may pass.")
        exit()

# This function is used to check the traveler's favourite colour.
def colour_check(colour):
    if colour[0]==name[0]:
        print("You may pass!")
    else:
        print("Incorrect! You must now face the Gorge of Eternal Peril.")

system("cls")
print("Stop! Who would cross the Bridge of Death \nMust answer me these questions three, 'ere the other side he see.\n")

name=input("What is your name:")
name_check(name)

quest=input("What do you seek?")
quest_check(quest)

colour=input("What is your favourite colour?")
colour_check(colour)  