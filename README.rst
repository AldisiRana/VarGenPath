===========
VarGenPath
===========
VarGenPath (Variant-Gene-Pathway) is a tool that creates a network that contains variants, genes and their pathways using cystoscape app.

Structure
----------
- ``data``: A folder containing the data used.
- ``output``: the default file for saving the output of the package.

Installation
-------------
``vargenpath`` can be installed on python from the latest code on `GitHub <https://github.com/seffnet/seffnet>`_ with:

.. code-block:: sh

    $ pip install git+https://github.com/AldisiRana/VarGenPath.git

Usage
------
Command Line Interface
~~~~~~~~~~~~~~~~~~~~~~~
You can build vargenpath network using the following command:

.. code-block:: bash

    $ vargenpath --variant-list .\data\variant_list.txt

Note: cytoscape program has to be running in the background.
