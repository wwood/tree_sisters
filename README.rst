tree_sisters
=================


Installation
--------------

tree_sisters can be installed by unzipping the source code in one directory and using this command: ::

    sudo python setup.py install

You can also install it directly from the Python Package Index with this command: ::

    sudo pip install tree_sisters

Usage
-----

    tree_sisters -t a.tree >lineages.csv
    
This will print out, for each leaf, the leaf ID, the taxonomy containing that leaf, and lineage(s) that 
the leaf is sister to.

To print out a subset of leaves in a newline separated file,

    tree_sisters -t a.tree -l leaves_list.txt >lineages.csv

Licence
--------

See file LICENCE.txt in this folder


Contribute
-----------
tree_sisters is an open-source software. Everyone is welcome to contribute !
