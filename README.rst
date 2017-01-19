Microbial Metabolic Interactions
================================

**MMinte** (pronounced /‘minti/) allows users to explore the pairwise interactions
(positive or negative) that occur in a microbial network using COBRA metabolic
models. MMinte estimates growth under specific metabolic conditions,
analyzes pairwise interactions, assigns interaction types to network links,
and generates the corresponding network of interactions.

**mminte-mp** is a multiprocessor implementation of the core MMinte algorithm that
improves performance when analyzing a large microbial network.

For a single species model to be used by mminte-mp it must meet these requirements:

1. Reaction and metabolite IDs must have a compartment suffix using one of two
   types. A "bigg" compartment suffix has the format "[x]" where x is a single
   character compartment ID (for example, "[c]" for cytosol compartment). A
   "modelseed" compartment suffix has the format "_x" where x is a single character
   compartment ID (for example "_c" for cytosol compartment). You can mix ID types
   in the same model.
2. There can be only one objective to optimize for growth in each source model.
3. Exchange reactions are identified by an 'EX_' prefix on the reaction ID.
4. Exchange reactions have only one metabolite with a negative coefficient.

Installation
------------

**Coming soon ...**

Use pip to install mminte-mp from `PyPI <https://pypi.python.org/pypi/mminte-mp>`_
(we recommend doing this inside a `virtual environment
<http://docs.python-guide.org/en/latest/dev/virtualenvs/>`_)::

    pip install mminte-mp

mminte-mp requires the cobra, pandas, and six packages. Using SBML models requires the python-libsbml and lxml
packages.

Direct installation in virtual environment
------------------------------------------

1. If virtualenvwrapper is not installed, `follow the directions <https://virtualenvwrapper.readthedocs.io/en/latest/>`__
   to install virtualenvwrapper.

2. Create a virtualenv for mminte-mp with these commands::

    $ cd mminte-mp
    $ mkvirtualenv mminte-mp --python /Library/Frameworks/Python.framework/Versions/2.7/bin/python

   Use the ``--python`` option to select a specific version of Python for the virtualenv. For example,
   ``python=python3`` to select the latest python3 installed on the system.

   Note on macOS, matplotlib requires Python be installed as a framework but virtualenv creates a
   non-framework build of Python. See the `matplotlib FAQ <http://matplotlib.org/1.5.3/faq/virtualenv_faq.html>`__
   for details on a workaround.

3. Upgrade pip and setuptools to the latest versions with these commands::

    (mminte-mp)$ pip install --upgrade pip setuptools

4. Install all of the mminte-mp dependencies with this command::

    (mminte-mp) pip install -r requirements.txt

   This command can take a few minutes while numpy, pandas, and libsbml are built in the virtualenv.

5. Install the latest version of mminte-mp with this command::

    (mminte-mp)$ python setup.py install

Run examples in a notebook
--------------------------

An example of how to use mminte-mp is provided in a notebook. Here's how to start Jupyter and run
the notebook from the virtualenv.

1. Install Jupyter with this command::

    (mminte-mp)$ pip install jupyter

2. Install a kernel that uses the virtualenv installation with this command::

    (mminte-mp)$ ipython kernel install --name "mminte-mp Python 27" --user

3. Start the Jupyter notebook server with this command::

    (mminte-mp)$ juypter notebook

   Jupyter opens a web page in your default browser with a file browser.

4. Navigate to the "documentation_builder" folder and click on the "mminte.ipynb" notebook.

5. After the notebook opens, from the "Kernel" menu, select "Change kernel" and click on "mminte-mp Python 27".

6. Now you can run the cells in the notebook.

References
----------

`MMinte: an application for predicting metabolic interactions among the microbial
species in a community <http://dx.doi.org/doi:10.1186/s12859-016-1230-3>`_ describes
the MMinte algorithm.

The models provided in the mminte/test/data folder are from `Anoxic Conditions Promote
Species-Specific Mutualism between Gut Microbes In Silico <http://dx.doi.org/doi:10.1128/AEM.00101-15>`_.
