# -*- coding: utf-8 -*-
##############################################################################
#    OpenERP, Open Source Management Solution
#    Copyright (C) 2017 WebLine Apps 
##############################################################################

from odoo import models, fields, api

class product_template(models.Model):
    _inherit = "product.template"
    
    bom_cost_price = fields.Float(compute='_bom_cost_price',
        string='Final Bom Cost')
        
    def _bom_cost_price(self):
        for pt_obj in self:
            bom_cost = 0
            for bom_id in pt_obj.bom_ids:
                bom_cost += bom_id.total_bom_cost
            pt_obj.bom_cost_price = bom_cost

# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
