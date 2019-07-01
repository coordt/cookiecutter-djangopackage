===========================
Cookiecutter Django Package
===========================

.. image:: https://travis-ci.org/coordt/cookiecutter-djangopackage.svg?branch=master
    :target: https://travis-ci.org/pcoordt/cookiecutter-djangopackage

A cookiecutter_ template for creating reusable Django packages (installable apps) quickly.

**Why?** Creating reusable Django packages has always been annoying. There are no defined/maintained
best practices (especially for ``setup.py``), so you end up cutting and pasting hacky, poorly understood,
often legacy code from one project to the other. This template, inspired by `cookiecutter-pypackage`_,
is designed to allow Django developers the ability to break free from cargo-cult configuration and follow
a common pattern dictated by the experts and maintained here.

.. _Cookiecutter: https://github.com/audreyr/cookiecutter
.. _cookiecutter-pypackage: https://github.com/audreyr/cookiecutter-pypackage

Features
--------

* Sane setup.py for easy PyPI registration/distribution
* Travis-CI configuration
* Codecov configuration
* Tox configuration
* Sphinx Documentation
* BSD licensed by default

Usage
-----

**Note**: Your project will be created with README.rst file containing a pypi badge, a travis-ci badge and a link to documentation on readthedocs.io. You don't need to have these accounts set up before using Cookiecutter or cookiecutter-djangopackage.

First, get Cookiecutter_ if you haven't already::

    pip install cookiecutter

Switch the the directory where you want your new repo to live::

    cd ~/Projects

Now run it against this repo::

    cookiecutter https://github.com/coordt/cookiecutter-djangopackage.git

You'll be asked some questions. The values in square brackets are the default answers. Pressing enter will accept the default.

``full_name``\ : Your name

``email``\ : Your email address

``github_username``\ : Your GitHub username

``pypi_username``\ : Your PyPI username

``project_name``\ : Convention dictates that the project name start with "Django," although it isn't necessary. If you do this, the following questions will get good defaults.

``repo_name``\ : The name of the repository on GitHub. The default converts the ``project_name`` to lowercase and replaces spaces with dashes.

``app_name``\ : The name of the Django app, or Python module. The default value removes ``django-`` and converts dashes to underscores.

``app_config_name``\ : Accept the default value unless you know what you are doing.

``project_short_description``\ : A brief description of what this app does.

``django_versions``\ : You can accept the default.

``version``\ : This is the starting version of your package. The default is acceptable.

``create_example_project``\ : You can have the template create an example project in the repo that can be used for examples or interactive testing. The default is ``Y`` for yes.

``open_source_license``\ : If this is not going to be open source, select ``5``\ . Otherwise select the appropriate license.

After you answer all the questions, the new Django package is created in your current directory.

Here is an example::

    cookiecutter https://github.com/coordt/cookiecutter-djangopackage.git
    full_name [Your full name here]: Pat Developer
    email [you@example.com]: patdev@coolco.com
    github_username [yourname]: patdev
    pypi_username [patdev]:
    project_name [Django Package]: Django Blogging for humans
    repo_name [django-blogging-for-humans]:
    app_name [blogging_for_humans]:
    app_config_name [BloggingForHumansConfig]:
    project_short_description []: This is a test of the cookiecutter template
    django_versions [2.1,2.2]:
    version [0.1.0]:
    create_example_project [Y]:
    Select open_source_license:
    1 - MIT
    2 - BSD
    3 - ISCL
    4 - Apache Software License 2.0
    5 - Not open source
    Choose from 1, 2, 3, 4, 5 [1]: 4

Enter the project and take a look around::

    cd django-blogging-for-humans/
    ls

Create a Git repo and make your first commit, and tag it `0.1.0`` (The tag is important for the automatic changelog creation)::

    git init
    git add .
    git commit -m "Initial commit"
    git tag 0.1.0

Create an empty repo on GitHub/GitLab/Bitbucket/etc. In our example below, we would call it ``django-blogging-for-humans``.

Create a GitHub repo and push it there::

    git init
    git add .
    git commit -m "first awesome commit"
    git remote add origin git@github.com:patdev/django-blogging-for-humans.git
    git push -u origin master
    git push --tags

Now take a look at your repo. Awesome, right?

Setting up Travis
~~~~~~~~~~~~~~~~~

You will need to explicitly activate your repo in your `Travis CI profile`_.
If the repo isn't showing up, run a manual synchronisation.

You will also want to install the `command line client`_ so you can encrypt passwords.

.. _Travis CI profile: https://travis-ci.org/profile/
.. _command line client: https://github.com/travis-ci/travis.rb#installation

Register on PyPI
~~~~~~~~~~~~~~~~

Once you've got at least a prototype working and tests running, it's time to register the app on PyPI::

    python setup.py register

You also need to encrypt your PyPI password in the Travis CI configuration::

    travis encrypt your-password-here --add deploy.password


Add to Django Packages
~~~~~~~~~~~~~~~~~~~~~~

Once you have a release, and assuming you have an account there,
just go to https://www.djangopackages.com/packages/add/ and add it there.


Developing your new app
-----------------------

Creating your environment
~~~~~~~~~~~~~~~~~~~~~~~~~

There are several ways to create your isolated environment. I recommend using virtualenvwrapper_\ . The example below assumes you have it installed.

::

    cd django-blogging-for-humans
    mkvirtualenv -a $(pwd) bloggingforhumans

The ``mkvirtualenv`` command creates a isolated Python environment (virtualenv) called ``testpkg`` and sets its working directory to your current working directory.

If you open a new terminal window and type::

    workon bloggingforhumans

You will find your working directory switched to ``django-blogging-for-humans`` and the virtualenv activated.

Create
.. _virtualenvwrapper: http://virtualenvwrapper.readthedocs.io/en/latest/

Setting Requirements
~~~~~~~~~~~~~~~~~~~~

Your requirements are split into parts: dev, prod, and test. They exist in the directory ``requirements``\ . ``Prod`` requirements are required for your app to work properly. ``Dev`` requirements are packages used to help develop this package, which include things for building documentation, packaging the app and generating the changelog. ``Test`` requirements are the libraries required to run tests.

As you develop, you will likely only modify ``requirements/prod.txt``\ .

If your virtualenv is created and activated, you can install the parts you need for development::

    pip install -r requirements/dev.txt

Testing
~~~~~~~

This template sets up the use of PyTest_, Tox_, Coverage_, and Flake8_. When you install the ``dev.txt`` requirements, the production and testing requirements are also installed. Tox_ is used to run the test suite.

Tests go in the appropriately named ``tests`` directory, and must start with ``test_`` for pytest to recognize them.

There are several ways to run your tests, depending on what you are doing. The simplest is to use the commands in the ``Makefile``\ .

``make lint`` will run Flake8 and lint your code.

``make test`` will run pytest using the default Python.

``make coverage`` will run pytest and generate HTML and terminal output of the test coverage. The HTML coverage report is available in the ``htmlcov`` directory.

``make test-all`` runs tox, which runs all the above, and will also test against multiple versions of Python and Django (if configured). You should ensure that this command passes before releasing a version.

.. _Tox: https://tox.readthedocs.io/en/latest/
.. _Pytest: https://docs.pytest.org/en/latest/
.. _Coverage: https://coverage.readthedocs.io/en/latest/
.. _Flake8: http://flake8.pycqa.org/en/latest/

Releasing your app
------------------

Once you have developed and tested your app, or revisions to it, you need to release new version.

Deciding the version
~~~~~~~~~~~~~~~~~~~~

First decide how to increase the version. Using `semantic versioning`_:

> Given a version number MAJOR.MINOR.PATCH, increment the:
>
> 1. MAJOR version when you make incompatible API changes,
> 2. MINOR version when you add functionality in a backwards-compatible manner, and
> 3. PATCH version when you make backwards-compatible bug fixes.

This is a judgement call, but here are some guidelines:

1. A database change should be a MINOR version bump at least.
2. If the PATCH version is getting above ``10``\ , as in ``1.0.14``\ , it is acceptable to do a MINOR version.
3. Dropping or adding support of a version of Python or Django should be at least a MINOR version.

.. _semantic versioning: https://semver.org/

Versioning and releasing
~~~~~~~~~~~~~~~~~~~~~~~~

Once you've decided how much of a version bump you are going to do, you will run one of three commands:

``make release-patch`` will automatically change the patch version, e.g. ``1.1.1`` to ``1.1.2``\ .

``make release-minor`` will automatically change the minor version, e.g. ``1.1.1`` to ``1.2.0``\ .

``make release-major`` will automatically change the major version, e.g. ``1.1.1`` to ``2.0.0``\ .

Each of these commands do several things:

1. Update the ``CHANGELOG.md`` file with the changes made since the last version, using the Git commit messages.
2. Increments the appropriate version number in the appropriate way.
3. Commits all the changes.
4. Creates a Git tag with the version number.
5. Pushes the repository and tags to the GitHub server.
6. Travis recognizes the new tag and publishes the package on PyPI
