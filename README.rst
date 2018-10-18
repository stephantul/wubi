wubi
======

Code for transliterating Chinese characters to their `wubi <https://en.wikipedia.org/wiki/Wubi_method>`_ equivalents.
Wubi is an ASCII representation of Chinese that respects orthographic, but not necessarily semantic or phonological regularities in Chinese characters.
It has been used successfully in machine translation, and can serve as a "character-level" representation of Chinese characters.

This code was heavily adapted from: https://github.com/arcsecw/wubi

Improvements
------------
* Python 3 support
* Corpus support from the command line
* Support for custom characters using a JSON dictionary
* The forward and backward translations are identical, with the exception of full-width numerals being converted to their normalized counterparts.

Install
-------

This version is not on `pip`. If you use `pip`, you will get the non-forked version.

Short Introduction
-----

.. code:: python

    >>> import wubi
    >>> print(wubi.to_wubi('WenChaoWang爱自由'))
    WenChaoWang ep thd mh
    >>> print(wubi.from_wubi('WenChaoWang ep thd mh'))
    WenChaoWang爱自由
    >>> print(wubi.to_wubi('WenChaoWang爱自由','-'))
    WenChaoWang-ep-thd-mh
    >>> print(wubi.from_wubi('WenChaoWang-ep-thd-mh','-'))
    WenChaoWang爱自由

License
-------

MIT
