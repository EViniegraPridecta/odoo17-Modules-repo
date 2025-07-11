===============
AEAT modelo 216
===============

.. 
   !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
   !! This file is generated by oca-gen-addon-readme !!
   !! changes will be overwritten.                   !!
   !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
   !! source digest: sha256:7890e57da4bfdf2f5ca373555e124690240c977f63cf7f1d2465433f55b7fb11
   !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

.. |badge1| image:: https://img.shields.io/badge/maturity-Mature-brightgreen.png
    :target: https://odoo-community.org/page/development-status
    :alt: Mature
.. |badge2| image:: https://img.shields.io/badge/licence-AGPL--3-blue.png
    :target: http://www.gnu.org/licenses/agpl-3.0-standalone.html
    :alt: License: AGPL-3
.. |badge3| image:: https://img.shields.io/badge/github-OCA%2Fl10n--spain-lightgray.png?logo=github
    :target: https://github.com/OCA/l10n-spain/tree/17.0/l10n_es_aeat_mod216
    :alt: OCA/l10n-spain
.. |badge4| image:: https://img.shields.io/badge/weblate-Translate%20me-F47D42.png
    :target: https://translation.odoo-community.org/projects/l10n-spain-17-0/l10n-spain-17-0-l10n_es_aeat_mod216
    :alt: Translate me on Weblate
.. |badge5| image:: https://img.shields.io/badge/runboat-Try%20me-875A7B.png
    :target: https://runboat.odoo-community.org/builds?repo=OCA/l10n-spain&target_branch=17.0
    :alt: Try me on Runboat

|badge1| |badge2| |badge3| |badge4| |badge5|

Modelo 216 de la AEAT. IRNR. Impuesto sobre la Renta de no Residentes.
Rentas obtenidas sin mediación de establecimiento permanente.
Retenciones e ingresos a cuenta.

**Table of contents**

.. contents::
   :local:

Configuration
=============

Debemos indicar los proveedores que son no residentes, en la ficha de la
empresa:

1. Vaya a *Contactos*.
2. Entrando al correspondiente, en la pestaña "Ventas y compras",
   seleccione en la posición fiscal la "Retención IRPF No residentes"
   que le corresponda.
3. Al crear facturas para dicho contacto, se mapearán los impuestos
   necesarios siempre que la línea de la factura tenga el producto
   informado con el impuesto nacional adecuado.

Usage
=====

Para crear un modelo:

1. Ir a Contabilidad > Informe > Informes legales > Declaraciones AEAT >
   Modelo 216.
2. Pulsar en el botón "Crear".
3. Seleccionar el año y el tipo de período. Las fechas incluidas se
   calculan automáticamente.
4. Seleccionar el tipo de declaración.
5. Rellenar el teléfono de contacto, necesario para la exportacion BOE.
6. Guardar y pulsar en el botón "Calcular".
7. Rellenar (si es necesario) aquellos campos que Odoo no calcula
   automáticamente:

   - Rentas no sometidas a retención/ingreso a cuenta: [04] Nº de rentas
     y [05] Base de retenciones
   - Resultados a ingresar anteriores: [06]

8. Cuando los valores sean los correctos, pulsar en el botón "Confirmar"
9. Podemos exportar en formato BOE para presentarlo telemáticamente en
   el portal de la AEAT

Bug Tracker
===========

Bugs are tracked on `GitHub Issues <https://github.com/OCA/l10n-spain/issues>`_.
In case of trouble, please check there if your issue has already been reported.
If you spotted it first, help us to smash it by providing a detailed and welcomed
`feedback <https://github.com/OCA/l10n-spain/issues/new?body=module:%20l10n_es_aeat_mod216%0Aversion:%2017.0%0A%0A**Steps%20to%20reproduce**%0A-%20...%0A%0A**Current%20behavior**%0A%0A**Expected%20behavior**>`_.

Do not contact contributors directly about support or help with technical issues.

Credits
=======

Authors
-------

* AvanzOSC
* Tecnativa

Contributors
------------

- `Tecnativa <https://www.tecnativa.com>`__:

  - Pedro M. Baeza
  - Antonio Espinosa
  - Victor M.M. Torres
  - David Bañón

- Ainara Galdona <ainara.galdona@avanzosc.es>
- Eficent - Jordi Ballester

Maintainers
-----------

This module is maintained by the OCA.

.. image:: https://odoo-community.org/logo.png
   :alt: Odoo Community Association
   :target: https://odoo-community.org

OCA, or the Odoo Community Association, is a nonprofit organization whose
mission is to support the collaborative development of Odoo features and
promote its widespread use.

.. |maintainer-pedrobaeza| image:: https://github.com/pedrobaeza.png?size=40px
    :target: https://github.com/pedrobaeza
    :alt: pedrobaeza

Current `maintainer <https://odoo-community.org/page/maintainer-role>`__:

|maintainer-pedrobaeza| 

This module is part of the `OCA/l10n-spain <https://github.com/OCA/l10n-spain/tree/17.0/l10n_es_aeat_mod216>`_ project on GitHub.

You are welcome to contribute. To learn how please visit https://odoo-community.org/page/Contribute.
