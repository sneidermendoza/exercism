"""
There are 64 squares on a chessboard
(where square 1 has one grain, square 2 has two grains, and so on).
"""
def square(number):
    """
    :on a chess board there are 64 squares.
    :function that calculates how many grains are in a box.
    """

    if not 1 <= number <= 64:
        raise ValueError("square must be between 1 and 64")
    return 2**(number - 1)

def total():
    """
    :function that calculates the total grains on a chess table.
    """
    return square(64) * 2 - 1
