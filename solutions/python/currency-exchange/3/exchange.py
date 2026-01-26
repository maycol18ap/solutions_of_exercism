"""
    calculadora de cambio
"""

def exchange_money(budget, exchange_rate):
    """conversion"""
    return budget/exchange_rate
    
def get_change(budget, exchanging_value):
    """restante luego del cambio"""
    return budget - exchanging_value

def get_value_of_bills(denomination, number_of_bills):
    """

    :param denomination: int - the value of a bill.
    :param number_of_bills: int - total number of bills.
    :return: int - calculated value of the bills.
    """
    return denomination * number_of_bills


def get_number_of_bills(amount, denomination):
    """

    :param amount: float - the total starting value.
    :param denomination: int - the value of a single bill.
    :return: int - number of bills that can be obtained from the amount.
    """
    return  amount//denomination
    


def get_leftover_of_bills(amount, denomination):
    """

    :param amount: float - the total starting value.
    :param denomination: int - the value of a single bill.
    :return: float - the amount that is "leftover", given the current denomination.
    """

    return amount % denomination


def exchangeable_value(budget, exchange_rate, spread, denomination):

    actual_rate = exchange_rate * (1 + (spread / 100))
    total_value = budget / actual_rate
    number_of_bills = total_value // denomination    
    return int(number_of_bills * denomination)
