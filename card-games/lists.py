"""
program that helps with a card game
"""
def get_rounds(number):
    """

     :param number: int - current round number.
     :return: list - current round and the two that follow.
    """

    return [number, number + 1, number + 2]


def concatenate_rounds(rounds_1, rounds_2):
    """

    :param rounds_1: list - first rounds played.
    :param rounds_2: list - second set of rounds played.
    :return: list - all rounds played.
    """

    return rounds_1 + rounds_2


def list_contains_round(rounds, number):
    """

    :param rounds: list - rounds played.
    :param number: int - round number.
    :return:  bool - was the round played?
    """

    return number in rounds


def card_average(hand):
    """

    :param hand: list - cards in hand.
    :return:  float - average value of the cards in the hand.
    """

    length = len(hand)
    return sum(hand) / length


def approx_average_is_average(hand):
    """

    :param hand: list - cards in hand.
    :return: bool - if approximate average equals to the `true average`.
    """

    average = card_average(hand)
    average_two_numbers= (hand[-1] + hand[0]) / 2
    length = int(len(hand) / 2)
    middle_card = hand[length]
    return bool(average in (average_two_numbers,middle_card))


def average_even_is_average_odd(hand):
    """

    :param hand: list - cards in hand.
    :return: bool - are even and odd averages equal?
    """

    sub_hand_even = []
    sub_hand_odd = []
    for i in hand:
        position = hand.index(i)
        if position%2:
            sub_hand_even.append(i)
        else:
            sub_hand_odd.append(i)
    average_1= card_average(sub_hand_even)
    average_2 = card_average(sub_hand_odd)
    return bool(average_1 == average_2)


def maybe_double_last(hand):
    """

    :param hand: list - cards in hand.
    :return: list - hand with Jacks (if present) value doubled.
    """

    last_index = []
    last_card = hand[-1]
    if last_card == 11:
        double = hand[-1] * 2
        last_index.append(double)
        hand[-1:] = last_index
        return hand
    return hand
