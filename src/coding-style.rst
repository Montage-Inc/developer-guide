============
Coding style
============

Please follow these guidelines when writing new code for Buildicus.

General Guidelines
==================

These are our general guidelines to be used throughout the codebase. Not all of
these will apply to every language we use, but they cover a lot of the overlap.

Whitespace
----------

* Indentation should use spaces, not tabs
* No extra spacing between arguments and expressions
* Delete all trailing whitespace
* End files with a trailing new line

Braces
------

* `One True Brace Style`_
* Never omit braces for single-statement blocks

EditorConfig
------------

`EditorConfig`_ helps define and maintain consistent coding styles. You would
do very well to install the plugin for your editor of choice.

Here's a sample ``.editorconfig`` that should be used:

.. code-block:: ini

    root = true

    [*]
    charset = utf-8
    end_of_line = lf
    indent_style = space
    indent_size = 4
    insert_final_newline = true
    trim_trailing_whitespace = true

    [*.{js,jsx}]
    indent_size = 2


Python style
============

Unless otherwise specified please follow PEP 8 and Django's coding style guide:

* http://www.python.org/dev/peps/pep-0008/
* https://docs.djangoproject.com/en/dev/internals/contributing/writing-code/coding-style/

Read 'em. Know 'em. Use 'em. Thanks.

Checking code with pycodestyle
------------------------------

You can use `pycodestyle`_ to verify that your code conforms to our standards::

    (montage)user@host:~/dev/montage $ pycodestyle montage/

Or if you just want an overview of PEP 8 violations::

    (montage)user@host:~/dev/montage $ pycodestyle montage/ -qq --statistics

Javascript style
================

TBD, but build from this:

https://github.com/Seravo/js-winning-style

Checking code with ESLint
-------------------------

TBD.

http://eslint.org/

LESS/SASS/CSS style
===================

TBD.

.. EditorConfig: http://editorconfig.org/
.. One True Brace Style: https://en.wikipedia.org/wiki/Indent_style#Variant:_1TBS
.. pycodestyle: https://pypi.python.org/pypi/pycodestyle
