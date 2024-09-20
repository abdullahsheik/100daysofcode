import random

friends = ["Kalam", "Abdullah", "Salauddin", "Shahid", "Minqad"]
#option 1:
print(random.choice(friends)+" Pays the bill")

#option 2:
random_index=(random.randint(0,4))
print(friends[random_index]+" Pays the bill")


