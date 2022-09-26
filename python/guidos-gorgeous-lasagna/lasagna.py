"""We're going to write some code to help cook a gorgeous lasagna"""

EXPECTED_BAKE_TIME = 40
MINUTES = 2

def bake_time_remaining(bake_time):
    """Calculate the bake time remaining."""

    return EXPECTED_BAKE_TIME - bake_time


def preparation_time_in_minutes(number_of_layers):
    """
    This function takes the number of layers you want to add to the lasagna as
    an argument and returns how many minutes you would spend making them.
    Assuming each layer takes 2 minutes to prepare.
    """

    return number_of_layers * MINUTES


def elapsed_time_in_minutes(number_of_layers, elapsed_bake_time):
    """
    Return elapsed cooking time.

    This function takes two numbers representing the number of layers & the
    time already spent baking and calculates the total elapsed minutes spent
    cooking the lasagna.
    """

    return preparation_time_in_minutes(number_of_layers) + elapsed_bake_time
