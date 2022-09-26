# -*- coding: utf-8 -*-
{
    'name': "koukaauto",

    'summary': """
        Short (1 phrase/line) summary of the module's purpose, used as
        subtitle on modules listing or apps.openerp.com""",

    'description': """
        Long description of module's purpose
    """,

    'author': "My Company",
    'website': "http://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/15.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base','mail','contacts','product','website_sale'],
    'application': True,

    # always loaded
    'assets': {
        'web.assets_frontend': [
            'koukaauto/static/src/js/koukaauto_website.js',
        ],
    },
    'data': [
        'security/security.xml',
        'security/ir.model.access.csv',
        'data/data.xml',
        'wizard/createoffer.xml',
        'views/vehiclead.xml',
        'views/model.xml',
        'views/mark.xml',
        'views/offer.xml',
        'views/engine.xml',
        'views/finition.xml',
        'views/koukaauto_website.xml',
        'views/menu.xml',
        'report/vehiclead_report.xml'
    ],
    # only loaded in demonstration mode
    'demo': ['demo/demo.xml',],
}