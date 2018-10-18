# -*- coding: utf-8 -*-
from string import ascii_letters, punctuation
from .cw import cw
from .wc import wc

roman = var = ascii_letters + '0123456789' + punctuation


def _wubi_generator(characters):
    """Generate wubi for chars, if char is not chinese character,
    itself will be returned.
    Chars must be unicode list.
    """
    buffer = []
    for char in characters:
        # handle roman characters in chinese
        if char == " ":
            buffer.append(" ")
        # If we encounter a roman character, add it to the buffer
        elif char in roman:
            buffer.append(char)
        else:
            # If the buffer is not empty
            # yield the buffer, set the buffer to 0
            if len(buffer) != 0:
                yield "".join(buffer)
                buffer = []
            yield cw.get(char, char)
    else:
        # Yield the buffer at the end.
        yield "".join(buffer)


def _chinese_generator(characters, delimiter):
    """Generate chinese for chars, if char is not chinese character,
    itself will be returned.
    Chars must be unicode list.
    """
    for char in characters.split(delimiter):
        yield wc.get(char, char)


def to_wubi(s, delimiter=" ", dictionary=None):
    """Translate chinese characters to wubi encoding."""
    if dictionary is not None:
        cw.update(dictionary)
    return delimiter.join(_wubi_generator(s))


def from_wubi(s, delimiter=" ", dictionary=None):
    """Translate wubi encoded characters to chinese."""
    if dictionary is not None:
        wc.update(dictionary)
    return "".join(_chinese_generator(s, delimiter))
