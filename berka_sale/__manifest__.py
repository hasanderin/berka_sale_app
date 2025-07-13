# -*- coding: utf-8 -*-
{
    'name': "Berka Sale",
    'summary': """Berka Sale""",
    'description': """Berka Sale""",
    'author': "Kalendiya",
    'website': "https://www.kalendiya.com",
    'category': 'Sale',
    'version': '15.0',
    'depends': ['delivery', 'account', 'purchase'],
    'data': [
        'views/sale_views.xml',
        'views/account_views.xml',
        'views/purchase_views.xml',
        'report/sale_report_templates.xml',
        'report/purchase_report_templates.xml',
        'report/invoice_report_templates.xml',
        'report/sale_report.xml',
        'report/report_invoice.xml'
    ],
    'application': False,
}
