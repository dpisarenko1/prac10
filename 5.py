def money_equal(money_on_card):
    """
    an amount of money going to card
    :param money_on_card: money without pluses
    :return: the end amount of money
    """
    if money_on_card == 5 or money_on_card == 10:
        return money_on_card
    elif money_on_card == 25:
        return money_on_card + 3
    elif money_on_card == 50:
        return money_on_card + 8
    elif money_on_card == 100:
        return money_on_card + 20

    return None

print(money_equal(100))
