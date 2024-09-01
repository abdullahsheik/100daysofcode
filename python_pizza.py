from zipfile import sizeEndCentDir

print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M or L: ")
bill=0
if size=="S":
    bill+=15
elif size=="M":
    bill+=20
elif size=="L":
    bill+=25
else:
    print("you have chosen an invalid size")
pepperoni = input("Do you want pepperoni on your pizza? Y or N: ")
if pepperoni == "Y":
    bill+=3
elif pepperoni == "N":
    bill+=0
else:
    print("You have chosen a wrong option")

extra_cheese = input("Do you want extra cheese? Y or N: ")
if extra_cheese == "Y":
    bill+=1
elif extra_cheese == "N":
    bill+=0
else:
    print("Wrong option")
print("Your final bill is:", {bill})