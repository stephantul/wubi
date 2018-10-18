# -*- coding: utf-8 -*-
from string import ascii_letters
from wubi.cw import cw
from wubi.wc import wc


# init wubi dict
data = {}
data['cw'] = cw
data['wc'] = wc


def _wubi_generator(chars):
    """Generate wubi for chars, if char is not chinese character,
    itself will be returned.
    Chars must be unicode list.
    """
    s = []
    for char in chars:
        # handle english in chinese
        var = ascii_letters
        if char == ' ':
            pass
        elif char in var:
                s.append(char)
                if char == chars[-1]:
                    yield ''.join(s)
        else:
            if len(s) != 0:
                yield ''.join(s)
                s = []
            wubi = data['cw'].get(char)
            if wubi is None:
                wubi = char
            yield wubi


def _chinese_generator(chars, delimiter):
    """Generate chinese for chars, if char is not chinese character,
    itself will be returned.
    Chars must be unicode list.
    """
    for char in chars.split(delimiter):
        yield data['wc'].get(char, char)


def get(s, type='', delimiter=' ', dictionary=None):
    """Return wubi of string, the string must be unicode"""
    if dictionary is not None:
        data['cw'].update(dictionary)
    if type == 'cw':
        return delimiter.join(_wubi_generator(s))
    elif type == 'wc':
        return ''.join(_chinese_generator(s, delimiter))
    else:
        return None
