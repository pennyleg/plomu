# -*- coding: utf-8 -*-
##############################################################################
#    OpenERP, Open Source Management Solution
#    Copyright (C) 2017 WebLineApps 
###############################################################################
{
    'name': 'BOM Cost Price',
    'summary': """ This odoo apps provide BOM cost price on BOM product show for access right on particular user.
					it will show per unit price and unit price total on BOM form.
					all BOM total cost show in product Form , BOM report,BOM product cost price """,
    'version': '13.0.1.3',
    'category': 'Tools',
    'description': """
            This odoo apps provide BOM cost price on BOM product for particular user.
			it will show per unit price and unit price total on BOM form.
			all BOM total cost show in product Form , BOM report
    """,
    'author': 'webline apps',
    'website': 'weblineapps@gmail.com',
    'depends': ['mrp'],
    'data': [
       'security/security.xml',
       'view/product_template_view.xml',
       'view/bom_line_view.xml',
    ],
    'images' : ['static/description/banner.png'],
    'price': 10.00,
	'currency': 'EUR',
    'installable': True,
    'auto_install': False,
    'application': False,
    
}


