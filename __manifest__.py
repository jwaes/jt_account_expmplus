# -*- coding: utf-8 -*-
{
    'name': "jt_account_expmplus",

    'summary': "ExpertM Plus import export functionality",

    'description': "Set BtchBookg to false by default",

    'author': "jaco tech",
    'website': "https://jaco.tech",
    "license": "AGPL-3",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/15.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Accounting',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['account'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'wizard/customer_export_views.xml',
        'views/account_move_views.xml',


    ],
    # only loaded in demonstration mode
    'demo': [
    ],
}
