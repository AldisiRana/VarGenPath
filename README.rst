===========
VarGenPath
===========
VarGenPath (Variant-Gene-Pathway) is a tool that creates a network that contains variants, genes and their pathways using cystoscape app.

Structure
----------
- ``data``: A folder containing the data used.
- ``output``: the default file for saving the output of the package.

Prerequisite
----------------
To be able to use this package, you need to install `Cytoscape <https://cytoscape.org/>`_ and have it running in the background.

You will also need to install `CyTargetLinker <https://cytargetlinker.github.io/>`_, a Cytoscape extension.
CyTargetLinker can be installed using Cytoscape GUI by selecting Apps|App Manager from the menu bar,
or from `here <http://apps.cytoscape.org/apps/cytargetlinker>`_.

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


