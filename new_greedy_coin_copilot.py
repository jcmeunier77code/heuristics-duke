#!/usr/bin/env python
import click


# Build a greedy algorithm to find the minimum number of coins but only using quarters and dimes
def greedy_coin(change):
    """Return a dictionary with the coin type as the key and the number of coins as the values only usring quarters and dimes"""

    print(f"Your change for {change} is:")
    amount_cents = round(change * 100)  # Convert to cents
    # Initialize the number of coins to 0
    coins = [0.25, 0.10]
    coin_lookup = {0.25: "quarters", 0.10: "dimes"}
    coin_dict = {}
    for coin in coins:
        coin_dict[coin] = 0
    for coin in coins:
        while amount_cents >= coin * 100:
            amount_cents -= coin * 100
            coin_dict[coin] += 1
    for coin in coin_dict:
        if coin_dict[coin] > 0:
            # print the number of coins
            print(f"{coin_dict[coin]} {coin_lookup[coin]}")
    return coin_dict


# Build a greedy algorithm to find the minimum number of coins but only using pennies, nickel and dimes
def greedy_coin2(change):
    """Return a dictionary with the coin type as the key and the number of coins as the values only using pennies,
    nickels and dimes
    """
    print(f"Your change for {change} is:")
    amount_cents = round(change * 100)  # Convert to cents
    # Initialize the number of coins to 0
    coins = 0
    coin_lookup = {0.25: "quarters", 0.10: "dimes", 0.05: "nickels", 0.01: "pennies"}
    coin_dict = {}
    for coin in coins:
        coin_dict[coin] = 0
    for coin in coins:
        while amount_cents >= coin * 100:
            amount_cents -= coin * 100
            coin_dict[coin] += 1
    for coin in coin_dict:
        if coin_dict[coin] > 0:
            # print the number of coins
            print(f"{coin_dict[coin]} {coin_lookup[coin]}")
    return coin_dict


# build a click group
@click.group()
def main():
    """Return the minimum of coins for a given change

    Examples:
        python new_greedy_coin_copilot.py 0.99
    """
    pass


#  build a click command that returns only quarters and dimes
@main.command("qd")
@click.argument("change", type=float)
def qd(change: float) -> None:
    """Return the minimum number of coins needed to make change for the given amount using only quarters and dimes.
    Args:
        change (float): The amount of change to make.
    Example:
        python new_greedy_coin_copilot.py 0.99
        Your change for 0.99 is:
        3 quarters
        2 dimes
    """
    greedy_coin(change)


# build a click command that returns only pennies, nickels and dimes
@main.command("pnd")
@click.argument("change", type=float)
def pnd(change: float) -> None:
    """Return the minimum number of coins needed to make change for the given amount using only pennies, nickels and dimes.
    Args:
        change (float): The amount of change to make.
    Example:
        python new_greedy_coin_copilot.py 0.99
        Your change for 0.99 is:
        2 dimes
        3 nickels
        4 pennies
    """
    greedy_coin2(change)

    if __name__ == "__main__":
        # pylint: disable=no-value-for-parameter
        main()
