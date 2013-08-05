from sys import exit


def map():
    print("""
-------------
|           |
|           |
|   $$$$    |
|           |----
|           |   |
------------- 8 |
|     |     |   |
| >_< |  s  |----
|     |     |
-------------
|   start   |
-------------
          """)


def freedom_room():
    print("You made it out alive. Time for a reward.")
    print("There is a stash of gold. How much do you take?")

    while True:
        gold_taken = raw_input("> ")
        if (gold_taken.isdigit()):
            print("Grats, bro. %d gold is yours." % int(gold_taken))
            exit(0)
        else:
            print("That's not a number O_o. Try again!")


def secret_passage():
    print("You found the passage but it's pitch black.")
    print("Would you like to proceed?")
    next_step = raw_input("(yes/no)> ")

    if next_step == "yes":
        print("You slowly move on and find the exit")
        freedom_room()
    elif next_step == "no":
        print("You backtrack to the previous room")
        snake_room()
    else:
        game_over("You cower in fear until you die.")


def snake_room():
    print("You enter a room full of snakes. What do you do?")
    print("a. Turn around")
    print("b. Look for a hidden passage")
    print("c. Run through the snakes")
    next_step = raw_input("(a, b, c)> ")

    if next_step == "a":
        start()
    elif next_step == "b":
        secret_passage()
    elif next_step == "c":
        game_over("Those are snakes. Nice try.")
    else:
        game_over("Your indecisiveness doesn't help. Snakes got ya!")


def hell_room():
    print("You enter a really hot room. In the middle stands Satan.")
    print("How are you going to get by this demon?")
    options = ['a. Hadouken him', 'b. Outrun him', 'c. Try to talk to him',
               'd. Turn around']
    for opt in options:
        print(opt)
    next_step = raw_input("(a, b, c, d)> ")

    if next_step == 'a' or next_step == 'b':
        print("This somehow works.")
        freedom_room()
    elif next_step == 'c' or next_step == 'd':
        game_over("Satan is having none of that. You are engulfed in flames.")
    else:
        game_over("You can't just ignore Satan. You are engulfed in flames.")


def game_over(message):
    print(message + " Game over!")
    exit(0)


def start():
    print("You find yourself in a lobby with a door to the left and right.")
    print("Which door would you like to go through?")
    next_step = raw_input("(left or right)> ")

    if next_step == "left":
        hell_room()
    elif next_step == "right":
        snake_room()
    else:
        game_over("You can't make a decision. Way to suck.")


map()
start()
