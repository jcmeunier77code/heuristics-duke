import click


def greedy_coin(change: float) -> int:
    """return a dictionary with the coins as the key and the number of coins as the value"""

    print(f"Your change for {change} is:")
    # convert the change to cents
    coins = [0.25, 0.10, 0.05, 0.01]
    coin_lookup = {0.25: "quarters", 0.10: "dimes", 0.05: "nickels", 0.01: "pennies"}
    coin_dict = {}
    for coin in coins:
        coin_dict[coin] = 0
    for coin in coins:
        while change >= coin:
            change -= coin
            coin_dict[coin] += 1
    for coin in coin_dict:
        if coin_dict[coin] > 0:
            # print the number of coins
            print(f"{coin_dict[coin]} {coin_lookup[coin]}")
    return coin_dict


@click.command()
@click.argument("change", type=float)
def main(change: float) -> None:
    """Return the minimum number of coins needed to make change for the given amount.
    Args:
        change (float): The amount of change to make.
    Example:
        python greedy_coin.py 0.99
        Your change for 0.99 is:
        3 quarters
        2 dimes
        4 pennies
    """

    greedy_coin(change)


if __name__ == "__main__":
    # pylint: disable=no-value-for-parameter
    main()
