# -*- coding: utf-8 -*-
{
    'name': "tasks",

    'summary': """
       Test""",

    'description': """

    """,

    'author': "Alexandr Konopko",
    'website': "http://simbioz.com.ua",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/openerp/addons/base/module/module_data.xml
    # for the full list
    'category': 'test',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        'templates.xml',
        'views/task.xml',
        'security/ir.model.access.csv',
        'security/security_task.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo.xml',
    ],
}