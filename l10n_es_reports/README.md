Fixing Odoo Enterprise incompatibility with l10n-spain
======================================================

Landoo SL, jun-2017, www.landoo.es
----------------------------------

This module is intended to fix actual incompatibility between Odoo Enterprise v10 and l10n-spain v10

KNOWN PROBLEMS:

l10n-spain, overrides l10n_es module from Odoo core, and this produces 2 problems:

* enterprise module l10n_es_reports tries to use a menuitem that is not created,
* enterprise module l10n_es_reports tries to use taxes that are not created

SOLUTION

Override original l10n_es_reports module by this one

USAGE

Download this module and declare it in addons_path, BEFORE Odoo Enterprise

Example of odoo.conf file if you download this module to /opt/odoo/odoo10e/extramodules:

addons_path = /opt/odoo/odoo10e/extramodules,/opt/odoo/odoo10e/enterprise,/opt/odoo/odoo10e/OCA/l10n-spain,/opt/odoo/odoo10e/odoo/odoo/addons,/opt/odoo/odoo10e/odoo/addons
