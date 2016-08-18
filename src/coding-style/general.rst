==================
General guidelines
==================

These are our general guidelines to be used throughout the codebase. Not all of
these will apply to every language we use, but they cover a lot of the overlap.


Whitespace
==========

* Indentation should use spaces, not tabs
* No extra spacing between arguments and expressions
* Delete all trailing whitespace
* End files with a trailing new line


Braces
======

* `One True Brace Style`_
* Never omit braces for single-statement blocks


EditorConfig
============

`EditorConfig`_ helps define and maintain consistent coding styles. You would
do very well to install the plugin for your editor of choice.

.. literalinclude:: /../example/.editorconfig
    :language: ini
    :linenos:

The Zen of Python
=================

Also known as `PEP 20`_, these are the guiding principals of Python's design
and are generally good advice for any software developer.

.. code-block:: python

    >>> import this
    The Zen of Python, by Tim Peters

    Beautiful is better than ugly.
    Explicit is better than implicit.
    Simple is better than complex.
    Complex is better than complicated.
    Flat is better than nested.
    Sparse is better than dense.
    Readability counts.
    Special cases aren't special enough to break the rules.
    Although practicality beats purity.
    Errors should never pass silently.
    Unless explicitly silenced.
    In the face of ambiguity, refuse the temptation to guess.
    There should be one-- and preferably only one --obvious way to do it.
    Although that way may not be obvious at first unless you're Dutch.
    Now is better than never.
    Although never is often better than *right* now.
    If the implementation is hard to explain, it's a bad idea.
    If the implementation is easy to explain, it may be a good idea.
    Namespaces are one honking great idea -- let's do more of those!


.. _EditorConfig: http://editorconfig.org/
.. _One True Brace Style: https://en.wikipedia.org/wiki/Indent_style#Variant:_1TBS
.. _PEP 20: https://www.python.org/dev/peps/pep-0020
