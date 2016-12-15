Microbial Metabolic Interactions
================================

**MMinte__** (pronounced /‘minti/) allows users to explore the pairwise interactions
(positive or negative) that occur in a microbial network using COBRA metabolic
models. MMinte estimates growth under specific metabolic conditions,
analyzes pairwise interactions, assigns interaction types to network links,
and generates the corresponding network of interactions.

**mminte-mp** is a multiprocessor implementation of the core MMinte algorithm that
improves performance when analyzing a large microbial network.

Requirements for source metabolic models
----------------------------------------

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

Use pip to install mminte-mp from `PyPI <https://pypi.python.org/pypi/mminte-mp>`_
(we recommend doing this inside a `virtual environment
<http://docs.python-guide.org/en/latest/dev/virtualenvs/>`_)::

    pip install mminte-mp

mminte-mp requires the cobrapy, pandas, and six packages.

References
----------

`MMinte: an application for predicting metabolic interactions among the microbial
species in a community <http://dx.doi.org/doi:10.1186/s12859-016-1230-3>`_ describes
the MMinte algorithm.

The models provided in the mminte/test folder are from `Anoxic Conditions Promote
Species-Specific Mutualism between Gut Microbes In Silico <http://dx.doi.org/doi:10.1128/AEM.00101-15>`_.
