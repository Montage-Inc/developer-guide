======
Python
======


PEP 8: Style guide for Python code
==================================

`PEP 8`_ provides coding conventions for the the Python code in the standard
library, and has been widely adopted by the community. All code should be
checked for PEP 8 conformity.

http://www.python.org/dev/peps/pep-0008/


Checking code with pycodestyle
------------------------------

You can use `pycodestyle`_ to verify that your code conforms to PEP 8 standards::

    $ pycodestyle montage/

Or if you just want an overview of PEP 8 violations::

    $ pycodestyle montage/ -qq --statistics


Django's style guide
====================

The Django project builds on top of PEP 8, and includes a number of useful
guidelines.

https://docs.djangoproject.com/en/dev/internals/contributing/writing-code/coding-style/


The Hitchhiker's Guide to Python
================================

Written by Kenneth Reitz, of `requests`_ fame, `The Hitchhiker's Guide to Python`_
is an opinionated guide to code style, best practices, and common idioms. It's
a good guide on how to write code that is `Pythonic`.

http://docs.python-guide.org/en/latest/


.. _PEP 8: http://www.python.org/dev/peps/pep-0008/
.. _pycodestyle: https://pypi.python.org/pypi/pycodestyle
.. _The Hitchhiker's Guide to Python: http://docs.python-guide.org/en/latest/
.. _requests: http://python-requests.org
