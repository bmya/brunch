    # -*- coding: utf-8 -*-
##############################################################################
#
#    OpenERP, Open Source Management Solution
#    Copyright (C) 2015 DevIntelle Consulting Service Pvt.Ltd. (<http://devintellecs.com>).
#
##############################################################################
from odoo import fields, models, api


class mrp_bom_line(models.Model):
    _inherit='mrp.bom.line'
    
    product_cost = fields.Float(string = 'Unit Cost', compute='_get_price')
    sub_total = fields.Float(string = 'Sub Total',compute='sub_total_get')
    
    @api.depends('product_id','product_id.standard_price')
    def _get_price(self):
        for line in self:
            if line.product_id:
                line.product_cost = line.product_id.standard_price
    
#    def onchange_product_id(self, cr, uid, ids, product_id, product_qty=0, context=None):
#        res = super(mrp_bom_line, self).onchange_product_id(cr, uid, ids, product_id, product_qty=product_qty, context=context)
#        pro_data = self.pool.get('product.product').browse(cr,uid,product_id)
#        res['value'] = {
#                'product_cost': pro_data.standard_price,
#            }
#        return res
    
            
    @api.multi
    @api.onchange('product_id','product_cost','product_qty')
    def sub_total_get(self):
        for line in self:
            line.sub_total = line.product_cost * line.product_qty
            
            
class mrp_bom_(models.Model):
    _inherit='mrp.bom'
    
    cost_per_unit = fields.Float(string = 'Cost Per Unit', compute='_get_cost_per_unit')
    
    @api.multi
    @api.onchange('bom_line_ids')
    def _get_cost_per_unit(self):
        for bom in self:
            total = 0.00
            for line in bom.bom_line_ids:
                total += line.product_cost
            bom.cost_per_unit = total

# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:    
