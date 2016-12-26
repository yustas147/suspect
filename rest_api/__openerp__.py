# -*- coding: utf-8 -*-
{
    'name': 'REST API',
    'version': '1.0',
    'category': 'API',
    'author': 'Andrey Sinyanskiy SP',
    'license': 'Other proprietary',
    'price': 120.00,
    'currency': 'EUR',
    'summary': 'RESTful API, OAuth2*, Redis',
    'shortdesc': """
This module provide RESTful API (json) access to Odoo models with OAuth2 authentification (very simplified) and Redis token store.
""",
    'website': 'https://www.odoo.com/apps',
    'external_dependencies': {
        'python' : ['redis'],
    },
    'depends': [
        'base',
        'web',
    ],
    'data': [
        'data/ir_configparameter_data.xml',
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
}
