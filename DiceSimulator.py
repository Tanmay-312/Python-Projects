import random

roll_or_not = input("Do you want to roll the dice , y or n?? ")
while roll_or_not == "y":
    number = random.randint(1, 6)
    if number == 1:
        print("[-----]")
        print("[     ]")
        print("[  0  ]")
        print("[     ]")
        print("[-----]")
    elif number == 2:
        print("[-----]")
        print("[0    ]")
        print("[     ]")
        print("[    0]")
        print("[-----]")
    elif number == 3:
        print("[-----]")
        print("[    0]")
        print("[  0  ]")
        print("[0    ]")
        print("[-----]")
    elif number == 4:
        print("[-----]")
        print("[0   0]")
        print("[     ]")
        print("[0   0]")
        print("[-----]")
    elif number == 5:
        print("[-----]")
        print("[0   0]")
        print("[  0  ]")
        print("[0   0]")
        print("[-----]")
    elif number == 6:
        print("[-----]")
        print("[0   0]")
        print("[0   0]")
        print("[0   0]")
        print("[-----]")

    roll_or_not = input("Do you want to roll the dice , y or n?? ")
    print()
print("Bye bye Have a good day!!")
