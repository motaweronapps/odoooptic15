# -*- coding: utf-8 -*-

{
    'name': 'Optical / Eye Clinic Solution',
    'version': '15.0.0.2',
    'summary': """Optical / Eye Clinic Solution""",
    'description': """Optical / Eye Clinic Solution""",
    'category': 'Optical',
    'author': 'bisolv',
    'website': "www.bisolv.com",
    'license': 'AGPL-3',

    'price': 50.0,
    'currency': 'USD',

    'depends': ['hr', "sale_management", "hr", "sales_team"],

    'data': [
        'data/hr_job.xml',
        'security/ir.model.access.csv',
        'views/config.xml',
        'views/hr_employee_view.xml',
        'views/hr_job_view.xml',
        'views/sale_order_view.xml',
        'views/res_company_view.xml',
        'views/product_inherit.xml',
        'report/document.xml',

    ],
    'demo': [

    ],
    'images': ['static/description/banner.png'],
    'qweb': [],

    'installable': True,
    'auto_install': False,
    'application': False,
}