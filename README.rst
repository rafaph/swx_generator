##############
SWX-GENERATOR
##############

* Version: 1.0.2

=============
Dependencies
=============

Django >= 1.7.*

=============
Installation
=============

* Activate your virtualenv:

.. code-block:: bash

    $ source bin/activate

* Install the package:

.. code-block:: bash

    $ pip install swx_generator-1.0.2.tar.gz

* Add **swx_generator** to your ``INSTALLED_APPS``.

==================
Avaliable Commands
==================

=============================================================  ==================
Command                                                        Function
=============================================================  ==================
``python manage.py generate <AppName> --model=<ModelName>``    Create a model
``python manage.py generate <AppName> --view=<view_name>``     Create a view
=============================================================  ==================

======
Usage
======

It's possible to create, for now, a ``model`` and ``view`` files using the **generate** command.

---------------
Create a model:
---------------

.. code-block:: bash

    $ python manage.py generate <AppName> --model=<ModelName>

The command above will create a model in the ``AppName``. Following three steps:

* Verify if package **models** exists in your ``AppName`` package, if it's not, it will be created.
* Create model file using model name in **snake case** notation.
* Add the model import in ``__init__.py`` file, like:

    .. code-block:: python

        from .model_name import ModelName

--------------
Create a view:
--------------

.. code-block:: bash

    $ python manage.py generate <AppName> --view=<view_name>

The command above will create a view file in the ``AppName``. Follow two steps:

* Verify if package **views** exists in your ``AppName`` package, if it's not, it will be created.
* Create view file with **view_name**, always in **snake case** notation.