===============
Bugs and Issues
===============

Please follow these guidelines when creating new issues in Github.

Writing a useful bug report
===========================

Useful bug reports are ones that get bugs fixed. A useful bug report normally
has two qualities:

1. **Reproducible.** If your bug is not reproducible it will never get fixed.
   You should clearly mention the steps to reproduce the bug. Do not assume or
   skip any reproducing step. Described the issue, step-by-step, so that it is
   easy to reproduce and fix.

2. **Specific.** Do not write a essay about the problem. Be Specific and to the
   point. Try to summarize the problem in minimum words yet in effective way.
   Do not combine multiple problems even they seem to be similar. Write
   different reports for each problem.

Example
-------

A good bug report looks something like this:

.. parsed-literal::

    **OS**: Operating System and version (Windows 7, OS X 10.8, Ubuntu 13.04)
    **Browser**: Browser name and version (IE 10, Firefox 27, Google Chrome 30)

    **Steps to Reproduce**

    1. Step-by-step instructions that detail how to reproduce the bug
    2. Don't leave steps out or make any assumptions
    3. If screenshots are called for, provide them here
    4. Make sure these steps reliably reproduce the issue

    **Actual Result**

    Describe what happens when the above steps were followed. If there is any
    relevent information in the developer tools window, make note of it here.

    **Expected Result**

    Explain what should have happened -- or what you expected to happen -- when
    the above steps were followed.

    **Workaround**

    If you have know a way to work around the problem, describe it here.

Here's a template you can paste directly into Github:

::

    **OS**:
    **Browser**:

    **Summary**

    **Steps to Reproduce**

    **Actual Result**

    **Expected Result**

    **Workaround**

Effectively organizing tickets
==============================

Properly labeling tickets is *essential* to keeping our tracker organized. Some
labels stand by themselves, while others are organized into ``group:value``
pairs.

When creating a new ticker, it should, at the very minimum, have a label from
each of these groups:

The ``env`` group specifies which environment (or site) the issue occurred on.

* ``env:dev``
* ``env:prod``

The ``severity`` group specifies how severe the issue is, ranging from trivial
to catastrophic. Feature requests also fall under this group.

* ``severity:minor`` -- Minor loss of function, trivial UI problem
* ``severity:major`` -- Major loss of function
* ``severity:critical`` -- Application crash, loss of data
* ``severity:blocking`` -- The issue is preventing further testing or work from being done

Triaging tickets
================

When a ticket is first created, it is considered *unreviewed*. Unreviewed
tickets will be evaluated by a member of the development team or anyone else
qualified to make a judgement on the validity of the ticket.

If the ticket is deemed to contain a valid issue or viable feature, the triager
should apply the ``accepted`` label and leave a comment describing the action
to be taken or provide any other information necessary to get the issue
resolved.

When closing a ticket, you should always leave a comment providing the reason.

