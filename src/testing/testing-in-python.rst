=================
Testing in Python
=================


Defining test cases with unittest
=================================

Tests cases should be defined with the built-in `unittest`_ module. This allows
for tests to be easily structured, and related tests can be grouped together.

Test assertions should be made with the ``assert`` statement, **not** the
``assertFoo`` methods provided by `unittest`_; it's cleaner and easier to
parse, and `pytest`_ understands it just fine.

.. code-block:: python
    :linenos:

    import unittest

    class YourModuleTests(unittest.TestCase):
        def test_add(self):
            assert 2 + 2 == 4


Running tests with pytest
=========================

Use `pytest`_ to run the tests. It integrates well with `unittest`_, and there
are a ton of `useful plugins`_.

There are two plugins that every project should use:

* `pytest-pep8`_ to check code style against `PEP 8`_
* `pytest-cov`_ to measure test coverage

When all is said and done, the command to run your tests should look something
like this::

    py.test tests/ --cov your_module --cov-append --cov-report term-missing --pep8


Automating tests with tox
=========================

`tox`_ is a tool that aims to automate and standardize tests. It's especially
useful when you need to test code in different environments (i.e., multiple
versions of Python).

``tox`` is a much simpler command to remember than a long ``py.test`` command,
so it's good to use even if you're only targeting a single environment.

A simple ``tox.ini`` looks like this:

.. literalinclude:: /../example/tox.ini
    :language: ini
    :linenos:

Now when you run ``tox``, you should see something like this::

    $ tox

    ... a whole lot of output, including test output and coverage summary ...

    _______________ summary _______________
      py27: commands succeeded
      py35: commands succeeded
      congratulations :)


Continuous Integration with CircleCI
====================================

Getting tests to run with `tox`_ on `CircleCI`_ requires the use of
`tox-pyenv`_ to make different Python versions available.

In this example ``circle.yml``, we'll run our tests and upload the coverage
results to `Codecov`_:

.. literalinclude:: /../example/circle.python.yml
    :language: ini
    :linenos:


.. _CircleCI: https://circleci.com/gh/Montage-Inc
.. _Codecov: https://codecov.io/
.. _PEP 8: https://www.python.org/dev/peps/pep-0008/
.. _pytest-cov: https://pypi.python.org/pypi/pytest-cov
.. _pytest-django: https://pypi.python.org/pypi/pytest-django
.. _pytest-pep8: https://pypi.python.org/pypi/pytest-pep8
.. _pytest-pythonpath: https://pypi.python.org/pypi/pytest-pythonpath
.. _pytest: https://pypi.python.org/pypi/pytest
.. _tox: https://pypi.python.org/pypi/tox
.. _tox-pyenv: https://pypi.python.org/pypi/tox-pyenv
.. _unittest: https://docs.python.org/3/library/unittest.html
.. _useful plugins: https://pypi.python.org/pypi?:action=search&term=pytest-
