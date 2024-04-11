"""Provide the 1 most common words"""

from functools import singledispatch

@singledispatch
def the(arg):
    _self = getattr(arg, 'self', False)
    if not _self:
        return the(None)
    return the(_self)


@the.register(type(None))
def _(arg):
    return None

@the.register(str)
def _(arg):
    """Make the from a string

    """
    return arg
