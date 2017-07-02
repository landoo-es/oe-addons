Fixing Odoo Enterprise conflict with l10n-spain
======================================================
This module is intended to fix actual conflict between Odoo Enterprise Edition v10 (EE) and l10n-spain v10

KNOWN PROBLEMS
--------------
l10n-spain, overrides l10n_es module from Odoo core, and this produces 2 problems:

* enterprise module l10n_es_reports tries to use a menuitem that is not created,
* enterprise module l10n_es_reports tries to use taxes that are not created (and they are not used in Spain)

SOLUTION
--------
Override original l10n_es_reports module from EE  by this one

USAGE
-----
Download this module and declare it in addons_path, BEFORE Odoo Enterprise

Example of odoo.conf line::

addons_path = /opt/odoo/odoo10e/extramodules,/opt/odoo/odoo10e/enterprise,/opt/odoo/odoo10e/OCA/l10n-spain,/opt/odoo/odoo10e/odoo/odoo/addons,/opt/odoo/odoo10e/odoo/addons


AUTHOR
------
Landoo SL, jun-2017, www.landoo.es
