Sofware Installation
====================

Installing the software is a quite simple procedure, just performs the following steps .

Prerequisites
-------------

The system has been written using `python3.4 <https://www.python.org/download/releases/3.4/>`_. Hence be sure you have this version supported on your machine.
You will also an enough updated version of the following python libraries:

* `Numpy <http://www.numpy.org>`_, version 1.11.2 or higher.
* `Pandas <https://pandas.pydata.org>`_, version 0.20.3 or higher.
* `Scikit-learn <http://scikit-learn.org/stable/>`_ , version 0.18.1 or higher.
* `NLTK <https://www.nltk.org>`_ , version 3.2.5 or higher.

Get the code
------------

Create a project folder, like

.. code-block:: console

   $ mkdir ${HOME}/Project_directory
   $ cd ${HOME}/Project_directory

in such folder, checkout a working copy of the code repository by tiping

.. code-block:: console

   $ git clone https://github.com/Fracappo87/Pricesearcher

then add the following line to your :code:`.bashrc` file (or :code:`.profile` if you are a Mac user)

.. code-block:: bash

   export PYTHONPATH="$PYTHONPATH:$HOME/Project_directory/Pricesearcher"

Run the code
------------

Before starting to use the system, open a new terminal, move into the code directory and run all the tests:

.. code-block:: console

   $ cd $HOME/Project_directory/Pricesearcher
   $ python3.4 -m unittest discover

it will take less then one minute. If all the tests passed successfully then you are ready to use the **IR** system!
