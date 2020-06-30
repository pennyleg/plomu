# -*- coding: utf-8 -*-
##############################################################################
#    OpenERP, Open Source Management Solution
#    Copyright (C) 2017 WebLine Apps 
##############################################################################
from odoo import models, fields, api

class mrp_bom_line(models.Model):
    _inherit = "mrp.bom.line"
    
    cost_price = fields.Float(string='Cost')
    total_cost_price = fields.Float(compute='_cost_price_total',
        string='Total Cost')
        
    @api.depends('product_qty','cost_price')
    def _cost_price_total(self,):
        for bom_line in self:
            bom_line.total_cost_price =  bom_line.cost_price * bom_line.product_qty
#            bom_line.product_id.write({'standard_price':bom_line.cost_price})
            

    @api.onchange('product_id')
    def change_product_price(self):
        for bom_line in self:
            if bom_line.product_id:
                bom_line.cost_price = bom_line.product_id.standard_price
                

            
class mrp_bom(models.Model):
    _inherit = "mrp.bom"
    
    total_bom_cost = fields.Float(compute='_total_bom_cost',
        string='Total BOM Cost')
        
    @api.depends('bom_line_ids')
    def _total_bom_cost(self,):
        for bom_obj in self:
            total_bom_cost = 0
            for bom_line in bom_obj.bom_line_ids:
                total_bom_cost += bom_line.total_cost_price
            bom_obj.total_bom_cost = total_bom_cost
            
        
        
        
        
        
        
        
        
        
    

# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
