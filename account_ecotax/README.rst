=================
Ecotax Management
=================

.. 
   !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
   !! This file is generated by oca-gen-addon-readme !!
   !! changes will be overwritten.                   !!
   !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
   !! source digest: sha256:317373272503c302234559cedceb3c0e4d2c9e67caa9d521a72126bc226133ba
   !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

.. |badge1| image:: https://img.shields.io/badge/maturity-Beta-yellow.png
    :target: https://odoo-community.org/page/development-status
    :alt: Beta
.. |badge2| image:: https://img.shields.io/badge/licence-AGPL--3-blue.png
    :target: http://www.gnu.org/licenses/agpl-3.0-standalone.html
    :alt: License: AGPL-3
.. |badge3| image:: https://img.shields.io/badge/github-OCA%2Faccount--fiscal--rule-lightgray.png?logo=github
    :target: https://github.com/OCA/account-fiscal-rule/tree/17.0/account_ecotax
    :alt: OCA/account-fiscal-rule
.. |badge4| image:: https://img.shields.io/badge/weblate-Translate%20me-F47D42.png
    :target: https://translation.odoo-community.org/projects/account-fiscal-rule-17-0/account-fiscal-rule-17-0-account_ecotax
    :alt: Translate me on Weblate
.. |badge5| image:: https://img.shields.io/badge/runboat-Try%20me-875A7B.png
    :target: https://runboat.odoo-community.org/builds?repo=OCA/account-fiscal-rule&target_branch=17.0
    :alt: Try me on Runboat

|badge1| |badge2| |badge3| |badge4| |badge5|

This module adds ecotax amount on invoice line. furthermore, a total
ecotax is added at the footer of each document.

To make easy ecotaxe management and to factor the data, ecotaxes are set
on products via ECOTAXE classifications. ECOTAXE classification can
either be a fixed or weight based ecotax.

A product can have one or serveral ecotax classifications. For example,
wooden window blinds equipped with electric motor can have ecotax for
wood and ecotax for electric motor.

This module has some limits : - The ecotax amount is always included in
the price of the product. - The ecotax amount is not isolated in an
specific accounting account but is included in the product income
account.

If one of these limits is an issue, you could install the submodule
account_ecotax_tax. This second module lets you manage the ecotax as a
tax, so you can configure if you want it to be included or excluded of
product price and also configuring an accounting account to isolate it.
The main consequence of this approach is that the ecotax won't be
considered in the turnover, since it is considered as a tax.

This module version add the possibility to manage several ecotax
classifications by product. A migration script is necessary to update
from previous versions.

There is the main change to manage in migration script:

renamed field model old field new field account.move.line
unit_ecotaxe_amount ecotaxe_amount_unit product.template
manual_fixed_ecotaxe force_ecotaxe_amount

changed fields model old field new field product.template
ecotaxe_classification_id ecotaxe_classification_ids

added fields model new field account.move.line ecotaxe_line_ids
product.template ecotaxe_line_product_ids

**Table of contents**

.. contents::
   :local:

Usage
=====

1. Add an ecotax classification via the menu **Accounting >
   Configuration > Taxes > Ecotax Classification**.

   - The ecotax classification can be either a fixed ecotax or a
     weight-based ecotax.
   - Ecotax classification information can be used for legal
     declarations.
   - For the fixed ecotax, the ecotax amount is used as a default value,
     which can be overridden on the product.
   - For the weight-based ecotax, define one ecotax by a coefficient
     applied to the weight (depending on the product's materials).

2. Assign one or more ecotax classifications to a product.

   - The ecotax amount can also be manually overridden on the product.

3. Create an invoice with this product

Bug Tracker
===========

Bugs are tracked on `GitHub Issues <https://github.com/OCA/account-fiscal-rule/issues>`_.
In case of trouble, please check there if your issue has already been reported.
If you spotted it first, help us to smash it by providing a detailed and welcomed
`feedback <https://github.com/OCA/account-fiscal-rule/issues/new?body=module:%20account_ecotax%0Aversion:%2017.0%0A%0A**Steps%20to%20reproduce**%0A-%20...%0A%0A**Current%20behavior**%0A%0A**Expected%20behavior**>`_.

Do not contact contributors directly about support or help with technical issues.

Credits
=======

Authors
-------

* Akretion

Contributors
------------

- Mourad EL HADJ MIMOUNE <mourad.elhadj.mimoune@akretion.com>
- Florian da Costa <florian.dacosta@akretion.com>

Maintainers
-----------

This module is maintained by the OCA.

.. image:: https://odoo-community.org/logo.png
   :alt: Odoo Community Association
   :target: https://odoo-community.org

OCA, or the Odoo Community Association, is a nonprofit organization whose
mission is to support the collaborative development of Odoo features and
promote its widespread use.

.. |maintainer-mourad-ehm| image:: https://github.com/mourad-ehm.png?size=40px
    :target: https://github.com/mourad-ehm
    :alt: mourad-ehm
.. |maintainer-florian-dacosta| image:: https://github.com/florian-dacosta.png?size=40px
    :target: https://github.com/florian-dacosta
    :alt: florian-dacosta

Current `maintainers <https://odoo-community.org/page/maintainer-role>`__:

|maintainer-mourad-ehm| |maintainer-florian-dacosta| 

This module is part of the `OCA/account-fiscal-rule <https://github.com/OCA/account-fiscal-rule/tree/17.0/account_ecotax>`_ project on GitHub.

You are welcome to contribute. To learn how please visit https://odoo-community.org/page/Contribute.
