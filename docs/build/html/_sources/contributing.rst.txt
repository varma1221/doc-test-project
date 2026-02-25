Contributing
============

We welcome contributions!

Docstring Format
----------------

Use Google-style docstrings:

.. code-block:: python

   def function_name(param1, param2):
       """
       Brief description.
       
       Args:
           param1 (type): Description
           param2 (type): Description
       
       Returns:
           type: Description
       
       Examples:
           >>> function_name(1, 2)
           3
       """

Building Documentation
----------------------

.. code-block:: bash

   cd docs
   .\make.bat html
