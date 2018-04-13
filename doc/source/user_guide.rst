User Guide
==========

Welcome the the **IR** system user guide. In the following, the basic functionalities of the system will be explained,
along with instructions for running user defined queries.

The system allows users to

* Define customized research keys to be used for ranking queries
* Performing as many queries as users want.

Performing queries
------------------
To get basic information about the system, just type

.. code-block:: console

   $ python3.4 -m research_engine.pricesearcher -h
   usage: pricesearcher.py [-h] [--outpath OUTPATH]
                        [--fields FIELDS [FIELDS ...]] [--to_show TO_SHOW]

   Download and unpack data files, build inverse indexes, search and rank queries

   optional arguments:
   -h, --help            show this help message and exit
   --outpath OUTPATH     Outputpath for source data
   --fields FIELDS [FIELDS ...]
                        Fields users can use for searching. If fields do not
                        match then are removed. When all provided fields are
                        wrong, then default fields are used
   --to_show TO_SHOW     Number of results to be shown. Default is 10

The system can be run by using specific fields of search, or by just using all the available research fields contained in the data set.

.. code-block:: console

   $ python3.4 -m research_engine.pricesearcher --fields description
   #############################################################
   # WELCOME TO PRICESEARCHER, A REALLY SIMPLE RESEARCH ENGINE #
   #############################################################

   Downloading source zipped file from the following URL :

   https://s3-eu-west-1.amazonaws.com/pricesearcher-code-tests/software-engineer/products.json.gz

   Creating inverse indexes

   Indexes produced by using the following fields:  ['description']

   Inverse indexes created in XXX seconds

   Ready to search: please type EXIT to terminate the application, or type anything else to continue

   What do you want to search?

.. code-block:: console

   $ python3.4 -m research_engine.pricesearcher
   #############################################################
   # WELCOME TO PRICESEARCHER, A REALLY SIMPLE RESEARCH ENGINE #
   #############################################################

   Downloading source zipped file from the following URL :

   https://s3-eu-west-1.amazonaws.com/pricesearcher-code-tests/software-engineer/products.json.gz

   Creating inverse indexes

   Indexes produced by using the following fields:  ['description',  'merchant', 'title']

   Inverse indexes created in YYY seconds

   Ready to search: please type EXIT to terminate the application, or type anything else to continue

   What do you want to search?

The system is robust enough against wrongly given research fields. For more information you can consult the developer guide.

Example of Search
-----------------

The **IR** system uses a **Vector Space Model** representantion to rank user defined queries according to the **cosine similarity**.
Before performing any indexing or search, it applies some preprocessing on the data to ensure that:

1. stopwords get removed
2. stemmatization is applied
3. all the characters are set to lower case

These operations are applied both on source data, as well as on user defined queries.
For each research key, a reverse index is created. Then similarities between user's queries and all the indexes are computed and averaged.
This provides an averaged ranking score among the various research keys.
Results from the search are printed out ranked in descending order by using the averaged ranking score.

.. code-block:: console

   $ python3.4 -m research_engine.pricesearcher
   #############################################################
   # WELCOME TO PRICESEARCHER, A REALLY SIMPLE RESEARCH ENGINE #
   #############################################################

   Downloading source zipped file from the following URL :

   https://s3-eu-west-1.amazonaws.com/pricesearcher-code-tests/software-engineer/products.json.gz

   Creating inverse indexes

   Indexes produced by using the following fields:  ['description',  'merchant', 'title']

   Inverse indexes created in YYY seconds

   Ready to search: please type EXIT to terminate the application, or type anything else to continue

   What do you want to search?bulldog
                                          description    merchant                                              title
    0  East Urban Home Liven up your living space, ad...     Wayfair  'Black French Bulldog' Graphic Art Print East ...
    1  East Urban Home Liven up your living space, ad...     Wayfair  'French Bulldog Dog' Graphic Art Print East Ur...
    2  East Urban Home Liven up your living space, ad...     Wayfair  'French Bulldog Dog' Graphic Art Print East Ur...
    3  East Urban Home Liven up your living space, ad...     Wayfair  'French Bulldog Dog' Graphic Art Print East Ur...
    4  East Urban Home Liven up your living space, ad...     Wayfair  'French Bulldog Dog' Graphic Art Print East Ur...
    5  Perfect for young ladies, this fitted inverted...  John Lewis  Unbranded Girls' Wool Mix Inverted Pleat Schoo...
    6  A navy blue waterproof school tracksuit top fo...  John Lewis  Unbranded Meoncross School Waterproof Tracksui...
    7  Elegant damask curtains, in a natural shade th...  John Lewis  John Lewis Alba Damask Pair Lined Pencil Pleat...
    8  This blind can be custom made to fit your wind...  John Lewis  Harlequin Samara Roller Blind, Spring Mechanis...
    9  The Beanies Premium range is medium ground roa...      Exante  Beanies Flavour Co Beanies Premium Vanilla Nut...
    What do you want to search?
