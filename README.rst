we-get: command-line tool for searching torrents.
#################################################

.. image:: https://img.shields.io/github/license/mashape/apistatus.svg?style=flat-square   :target:

.. class:: head

    .. image:: https://raw.githubusercontent.com/wiki/0xl3vi/we-get/screenshots/1.png
        :alt: Main screenshot.
        :width: 100%
        :align: center



.. contents::
.. section-numbering::

Installation
============

* Option 1

.. code-block:: bash

    $ sudo python setup.py install


* Option 2

.. code-block:: bash

    $ sudo pip install git+https://github.com/0xl3vi/we-get


Dependencies
============

`Python <https://www.python.org/>`_ 3.5 or above


Platforms
==========

* Linux
* Mac
* Windows

Basic Usage
===========

.. code-block:: bash

    $ we-get --search "royal pains" --target  the_pirate_bay,1337x --filter "S01"

General options
---------------

============ =============
-h --help    Help message.
-v --version Show version.
============ =============

Options
-------

===================== =====================================================
-s --search=<text>    Search for a torrent.                                
-l --list             List top torrents from modules.                      
-t --target=<target>  Select module to use or 'all'.                       
-L --links            Output results as links.                             
-J --json             Output results in JSON format.                       
-G --get-list         List targets (supported web-sites).                  
-f --filter=<str>     Match text or regular expression in the torrent name.
-n --results=<n>      Number of results to retrieve.                       
-S --sort-type=<type> Sort torrents by name/seeds (default: seeds).        
===================== =====================================================

Video options
-------------

================ ==================================================================
-q --quality=<q> Try to match quality for the torrent (720p,1080p, ...).           
-g --genre=<g>   Try to select video genre for the torrent (action, comedy, etc..).
================ ==================================================================



See also ``we-get --help``.

Supported websites
------------------

* 1337x
* thepiratebay
* eztv
* yts

and the list will grow.

Contributing
------------

Want to help with the development or test we-get on your platform?

* We need windows user to test we-get on windows.

Any collaboration is welcome!

If you want to write a module please see ``we_get/modules/``


Legal
------

The author of this project is not responsible of what users will search.
this tool will help you to search torrents, and will not download any torrents.

downloading/searching torrents in not a crime (only the illegal ones :wink:)

Licence
-------

`MIT <https://github.com/0xl3vi/we-get/blob/master/LICENSE>`_.
