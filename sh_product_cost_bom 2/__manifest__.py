# -*- coding: utf-8 -*-
# Part of Softhealer Technologies.
{
    'name': 'BOM Cost Price',
    
    'author' : 'Softhealer Technologies',
    
    'website': 'https://www.softhealer.com',    
    
    "support": "support@softhealer.com",   
    
    'version': '13.0.1',
    
    "category": "Manufacturing",
    
    'summary': """bom cost price app odoo, calculate total bom cost, get mrp product cost module, compute bill of material price""",
    
    'description': """This module used to get total cost of manufactuing product.
	bom cost price app odoo, calculate total bom cost, get mrp product cost module, compute bill of material price
	""",
    
    'depends': ['mrp'],
    
    'data': [
        'views/product_template.xml',
    ],
    
    'images': ['static/description/background.jpg',],
                  
    'auto_install':False,
    'installable' : True,
    'application': True,    
    
    "price": 13,
    "currency": "EUR"        
}
