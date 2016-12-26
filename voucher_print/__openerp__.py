{
    'name': 'voucher Print',
    'version': '8.0.1.0',
    'category': 'Accounting',
        'sequence': 1,
    'summary': "Print of payments",
    'description':"Print of payments",
    'author': 'DVIT.ME',
    'website': 'http://dvit.me',
    'website': 'http://www.dvit.me',
    'depends': ['account_voucher'],
    'data': [
        'views/voucher_report.xml',
        'voucher_print_report.xml',
    ],
    'installable': True,
    'auto_install': False,
}


