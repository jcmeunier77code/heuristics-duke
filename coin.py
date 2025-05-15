# build a greedy algorithm to find the minimu number of coins
def main():
    # get the amount of change owed
    while True:
        try:
            change = float(input("Change owed: "))
            if change > 0:
                break
        except ValueError:
            print("Invalid input. Please enter a positive number.")

    # convert the change to cents
    cents = round(change * 100)

    # initialize the number of coins to 0
    coins = 0

    # use a greedy algorithm to find the minimum number of coins
    while cents >= 25:
        cents -= 25
        coins += 1
    while cents >= 10:
        cents -= 10
        coins += 1
    while cents >= 5:
        cents -= 5
        coins += 1
    while cents >= 1:
        cents -= 1
        coins += 1
    # print the minimum number of coins
    print(f"Minimum number of coins: {coins}")
