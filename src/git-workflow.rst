============
Git workflow
============

Commit messages
===============

Karma commits.

http://karma-runner.github.io/1.0/dev/git-commit-msg.html

Karma says 70 characters for the first line, but Github wraps at 50. Let's
go with 50.

Branching model
===============

Our workflow is based on Vincent Driessen's `"successful git branching model"`__,
with some minor adjustments. We still utilize ``develop``, ``master``, and
various types of feature branches, however we do not tag releases and there are
no release branches.

.. seqdiag:: /_static/diagrams/git-branching-strategy.diag
    :width: 600

`git-flow`_ is a git plugin that helps facilitate this branching strategy. It's
not required, but can help make things a bit easier to manage. There is also a
good write up on `using git-flow`__.

Feature branching
-----------------

All development happens in a feature branch. Feature branches are named as
``type/branch-slug``, where ``type`` can be one of:

* **feature** -- New features, both major and minor, in development
* **bugfix** -- Fixing a specific bug or regression in the code
* **refactor** -- Re-writing or re-architecting parts of the system
* **hotfix** -- Patches applied directly to the master branch and deployed to live

.. important::

    Feature branches are not considered complete until they include all of the
    following:

    * **Code** that conforms to our :doc:`coding style <coding-style/index>`.
    * **Unit tests** that pass locally and in our CI environment.
    * **Documentation** updates, as needed.

When a feature branch has been merged into develop, it is the responsiblity of
that branches main developer to ensure it is deleted from Github.

..

    Deployment strategy
    ===================

    All commits to ``develop`` are automatically tested and, if passing, deployed
    to the dev site. The same holds true for the ``master`` branch, which is
    deployed to production.

    .. blockdiag:: /_static/diagrams/deployment.diag
        :width: 600

    .. important::

        Under no circumstances is a production deployment allowed to be made
        without fully passing unit tests.

.. _git-flow: https://github.com/nvie/gitflow
.. _git-branch: http://nvie.com/posts/a-successful-git-branching-model/
.. _using-git-flow: http://jeffkreeftmeijer.com/2010/why-arent-you-using-git-flow/

__ git-branch_
__ using-git-flow_

.. index::
    deploying
    git-flow
