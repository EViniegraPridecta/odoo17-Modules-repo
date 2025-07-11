.. image:: https://odoo-community.org/readme-banner-image
   :target: https://odoo-community.org/get-involved?utm_source=readme
   :alt: Odoo Community Association

========================
Queue Job Cron Jobrunner
========================

.. 
   !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
   !! This file is generated by oca-gen-addon-readme !!
   !! changes will be overwritten.                   !!
   !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
   !! source digest: sha256:7564ebfbee734b5b3a2f9f52ef96311086789ca36c6fb021b9f0ef674c35759e
   !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

.. |badge1| image:: https://img.shields.io/badge/maturity-Alpha-red.png
    :target: https://odoo-community.org/page/development-status
    :alt: Alpha
.. |badge2| image:: https://img.shields.io/badge/license-AGPL--3-blue.png
    :target: http://www.gnu.org/licenses/agpl-3.0-standalone.html
    :alt: License: AGPL-3
.. |badge3| image:: https://img.shields.io/badge/github-OCA%2Fqueue-lightgray.png?logo=github
    :target: https://github.com/OCA/queue/tree/17.0/queue_job_cron_jobrunner
    :alt: OCA/queue
.. |badge4| image:: https://img.shields.io/badge/weblate-Translate%20me-F47D42.png
    :target: https://translation.odoo-community.org/projects/queue-17-0/queue-17-0-queue_job_cron_jobrunner
    :alt: Translate me on Weblate
.. |badge5| image:: https://img.shields.io/badge/runboat-Try%20me-875A7B.png
    :target: https://runboat.odoo-community.org/builds?repo=OCA/queue&target_branch=17.0
    :alt: Try me on Runboat

|badge1| |badge2| |badge3| |badge4| |badge5|

This module implements a simple ``queue.job`` runner using ``ir.cron``
triggers.

It's meant to be used on environments where the regular job runner can't
be run, like on Odoo.sh.

Unlike the regular job runner, where jobs are dispatched to the
HttpWorkers, jobs are processed on the CronWorker threads by the job
runner crons. This is a design decision because:

- Odoo.sh puts HttpWorkers to sleep when there's no network activity
- HttpWorkers are meant for traffic. Users shouldn't pay the price of
  background tasks.

For now, it only implements the most basic features of the ``queue_job``
runner, notably no channel capacity nor priorities. Please check the
ROADMAP for further details.

.. IMPORTANT::
   This is an alpha version, the data model and design can change at any time without warning.
   Only for development or testing purpose, do not use in production.
   `More details on development status <https://odoo-community.org/page/development-status>`_

**Table of contents**

.. contents::
   :local:

Configuration
=============

Warning

Don't use this module if you're already running the regular
``queue_job`` runner.

For the easiest case, no configuration is required besides installing
the module.

To avoid CronWorker CPU timeout from abruptly stopping the job
processing cron, it's recommended to launch Odoo with
``--limit-time-real-cron=0``, to disable the CronWorker timeout
altogether.

Note

In Odoo.sh, this is done by default.

Parallel execution of jobs can be achieved by leveraging multiple
``ir.cron`` records:

- Make sure you have enough CronWorkers available (Odoo CLI
  ``--max-cron-threads``)
- Duplicate the ``queue_job_cron`` cron record as many times as needed,
  until you have as much records as cron workers.

Known issues / Roadmap
======================

- Support channel capacity and priority. (See ``_acquire_one_job``)
- Gracefully handle CronWorker CPU timeouts. (See ``_job_runner``)
- Commit transaction after job state updated to started. (See
  ``_process``)

Bug Tracker
===========

Bugs are tracked on `GitHub Issues <https://github.com/OCA/queue/issues>`_.
In case of trouble, please check there if your issue has already been reported.
If you spotted it first, help us to smash it by providing a detailed and welcomed
`feedback <https://github.com/OCA/queue/issues/new?body=module:%20queue_job_cron_jobrunner%0Aversion:%2017.0%0A%0A**Steps%20to%20reproduce**%0A-%20...%0A%0A**Current%20behavior**%0A%0A**Expected%20behavior**>`_.

Do not contact contributors directly about support or help with technical issues.

Credits
=======

Authors
-------

* Camptocamp SA

Contributors
------------

- `Camptocamp <https://www.camptocamp.com>`__

     - Iván Todorovich <ivan.todorovich@camptocamp.com>

Maintainers
-----------

This module is maintained by the OCA.

.. image:: https://odoo-community.org/logo.png
   :alt: Odoo Community Association
   :target: https://odoo-community.org

OCA, or the Odoo Community Association, is a nonprofit organization whose
mission is to support the collaborative development of Odoo features and
promote its widespread use.

.. |maintainer-ivantodorovich| image:: https://github.com/ivantodorovich.png?size=40px
    :target: https://github.com/ivantodorovich
    :alt: ivantodorovich

Current `maintainer <https://odoo-community.org/page/maintainer-role>`__:

|maintainer-ivantodorovich| 

This module is part of the `OCA/queue <https://github.com/OCA/queue/tree/17.0/queue_job_cron_jobrunner>`_ project on GitHub.

You are welcome to contribute. To learn how please visit https://odoo-community.org/page/Contribute.
