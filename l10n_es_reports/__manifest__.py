# -*- coding: utf-8 -*-


{
    'name': 'Spain - Accounting (PGCE 2008) Reports',
    'version': '10.0.1.0.1',
    'author': 'LANDOO',
    'website': 'https://github.com/landoo/oe-addons',
    'category': 'Localization',
    'description': """
        Fixing incompatibility between Odoo Enterprise v10 and l10n-spain
        USAGE
        Add this module to addons_path, BEFORE Odoo Enterprise
    """,
    'depends': [
        'l10n_es', 'account_reports',
    ],
    'data': [
        'data/account_financial_html_report_data_menu.xml',
    ],
    'installable': True,
    'auto_install': True,
    'license': 'LGPL-3',
}
