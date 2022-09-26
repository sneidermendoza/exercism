"""
Function that adds a gigsecond to a given moment.
"""
import datetime
def add(moment):
    """
    :Add takes parameter for a moment
    :Moment is added with a gigasecond and returns a new moment.
    """
    return moment + datetime.timedelta(seconds= 10**9)
