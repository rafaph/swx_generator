##############
SWX-GENERATOR
##############

* Version: 1.0.0

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
    $ pip install swx_generator-1.0.0.tar.gz

* Add **swx_generator** to your ``INSTALLED_APPS``.

======
Usage
======

---------------
Create a model:
---------------

* The command below will create a model in the ``AppName``. Following a few steps:
    * Verify if package **models** exists in your ``AppName`` package, if it's not, it will be created.
    * Create model file using model name in **snake case** notation.
    * Add the model import in ``__init__.py`` file, like:
        .. code-block:: python
        
            from .model_name import ModelName


.. code-block:: bash

    $ python manage.py generate <AppName> --model=<ModelName>

    
