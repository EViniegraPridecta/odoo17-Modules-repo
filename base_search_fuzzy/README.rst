============
Fuzzy Search
============

.. 
   !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
   !! This file is generated by oca-gen-addon-readme !!
   !! changes will be overwritten.                   !!
   !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
   !! source digest: sha256:c60c78cf638853e1d97925fc4b8987d1ae7c758ec04854e1822e90e2624e34ee
   !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

.. |badge1| image:: https://img.shields.io/badge/maturity-Beta-yellow.png
    :target: https://odoo-community.org/page/development-status
    :alt: Beta
.. |badge2| image:: https://img.shields.io/badge/licence-AGPL--3-blue.png
    :target: http://www.gnu.org/licenses/agpl-3.0-standalone.html
    :alt: License: AGPL-3
.. |badge3| image:: https://img.shields.io/badge/github-OCA%2Fserver--tools-lightgray.png?logo=github
    :target: https://github.com/OCA/server-tools/tree/17.0/base_search_fuzzy
    :alt: OCA/server-tools
.. |badge4| image:: https://img.shields.io/badge/weblate-Translate%20me-F47D42.png
    :target: https://translation.odoo-community.org/projects/server-tools-17-0/server-tools-17-0-base_search_fuzzy
    :alt: Translate me on Weblate
.. |badge5| image:: https://img.shields.io/badge/runboat-Try%20me-875A7B.png
    :target: https://runboat.odoo-community.org/builds?repo=OCA/server-tools&target_branch=17.0
    :alt: Try me on Runboat

|badge1| |badge2| |badge3| |badge4| |badge5|

This addon provides the ability to create GIN or GiST indexes of char
and text fields and also to use the search operator % in search domains.
Currently this module doesn't change the backend search or anything
else. It provides only the possibility to perform the fuzzy search for
external addons.

**Table of contents**

.. contents::
   :local:

Installation
============

1. The PostgreSQL extension ``pg_trgm`` should be available. In debian
   based distribution you have to install the postgresql-contrib module.
2. Install the ``pg_trgm`` extension to your database or give your
   postgresql user the ``SUPERUSER`` right (this allows the odoo module
   to install the extension to the database).

Configuration
=============

If the odoo module is installed:

1. You can define ``GIN`` and ``GiST`` indexes for char and text via
   Settings -> Database Structure -> Trigram Index. The index name will
   automatically created for new entries.

Usage
=====

1. You can create an index for the name field of res.partner.

2. In the search you can use:

   ``self.env['res.partner'].search([('name', '%', 'Jon Smit')])``

3. In this example the function will return positive result for John
   Smith or John Smit.

4. You can tweak the number of strings to be returned by adjusting the
   set limit (default: 0.3). NB: Currently you have to set the limit by
   executing the following SQL statement:

   ``self.env.cr.execute("SELECT set_limit(0.2);")``

For further questions read the Documentation of the
`pg_trgm <https://www.postgresql.org/docs/current/static/pgtrgm.html>`__
module.

Usage with demo data
--------------------

There are some demo data that allow you to test functionally this module
if you are in a **demo** database. The steps are the following:

1. Go to *Contacts* and type the text **Jon Smith** or **Smith John** in
   the search box and select **Search Display Name for: ...**
2. You will see two contacts, and they are the ones with display names
   **John Smith** and **John Smizz**.

Known issues / Roadmap
======================

- Modify the general search parts (e.g. in tree view or many2one fields)
- Add better order by handling
- This module will not be necessary from version 16 (`[IMP] Better
  handling of indexes
  #83015 <https://github.com/odoo/odoo/pull/83015>`__)

Bug Tracker
===========

Bugs are tracked on `GitHub Issues <https://github.com/OCA/server-tools/issues>`_.
In case of trouble, please check there if your issue has already been reported.
If you spotted it first, help us to smash it by providing a detailed and welcomed
`feedback <https://github.com/OCA/server-tools/issues/new?body=module:%20base_search_fuzzy%0Aversion:%2017.0%0A%0A**Steps%20to%20reproduce**%0A-%20...%0A%0A**Current%20behavior**%0A%0A**Expected%20behavior**>`_.

Do not contact contributors directly about support or help with technical issues.

Credits
=======

Authors
-------

* bloopark systems GmbH & Co. KG
* ForgeFlow
* Serpent CS

Contributors
------------

- Christoph Giesel <https://github.com/christophlsa>
- Jordi Ballester <jordi.ballester@forgeflow.com>
- Serpent Consulting Services Pvt. Ltd. <support@serpentcs.com>
- Dave Lasley <dave@laslabs.com>
- `Tecnativa <https://www.tecnativa.com>`__:

  - Vicent Cubells
  - Ernesto Tejeda

- teodoralexandru@nexterp.ro 2020 NextERP SRL.
- Daniel Reis <dreis@opensourceintegrators.com>
- Nikul Chaudhary <nchaudhary@opensourceintegrators.com>
- Nguyen Minh Chien <chien@trobz.com>

Maintainers
-----------

This module is maintained by the OCA.

.. image:: https://odoo-community.org/logo.png
   :alt: Odoo Community Association
   :target: https://odoo-community.org

OCA, or the Odoo Community Association, is a nonprofit organization whose
mission is to support the collaborative development of Odoo features and
promote its widespread use.

This module is part of the `OCA/server-tools <https://github.com/OCA/server-tools/tree/17.0/base_search_fuzzy>`_ project on GitHub.

You are welcome to contribute. To learn how please visit https://odoo-community.org/page/Contribute.
