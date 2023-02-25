import random


def tortoise_move():
    move = random.randint(1, 20)
    if 1 <= move <= 8:
        return 3
    elif 9 <= move <= 10:
        return -6
    else:
        return 1


def hare_move():
    move = random.randint(1, 20)
    if 1 <= move <= 2:
        return 0
    elif 3 <= move <= 8:
        return 9
    elif 9 <= move <= 10:
        return -12
    elif 11 <= move <= 14:
        return 1
    else:
        return -2


def simulate_race():

    global tortoise_position
    global hare_position

    print("\nBANG! AND THEY'RE OFF!!!!!\n")

    while tortoise_position < 95 and hare_position < 95:
        tortoise_position += tortoise_move()
        hare_position += hare_move()

        if tortoise_position < 1:
            tortoise_position = 1
        if hare_position < 1:
            hare_position = 1

        for j in range(1, 96):
            if j == tortoise_position and j == hare_position:
                print("OUCH!!!", end="")
            elif j == tortoise_position:
                print("T", end="")
            elif j == hare_position:
                print("H", end="")
            else:
                print("-", end="")
        print()


        if tortoise_position >= 95 and hare_position >= 95:
            print("\nIt's a TIE")
            break
        elif hare_position >= 95:
            print("\nHARE WINS. YUCH!")
            break
        elif tortoise_position >= 95:
            print("\nTORTOISE WINS!!! YAY!!!")
            break


tortoise_wins = 0
hare_wins = 0
ties = 0


for i in range(50):
    tortoise_position = 1
    hare_position = 1
    simulate_race()
    if tortoise_position >= 95 and hare_position >= 95:
        ties += 1
    elif hare_position >= 95:
        hare_wins += 1
    elif tortoise_position >= 95:
        tortoise_wins += 1


print("\nRace results:")
print("Tortoise wins:", tortoise_wins)
print("Hare wins:", hare_wins)
print("Ties:", ties)