    # -*- coding: utf-8 -*-
##############################################################################
#
#    OpenERP, Open Source Management Solution
#    Copyright (C) 2015 DevIntelle Consulting Service Pvt.Ltd. (<http://devintellecs.com>).
#
##############################################################################

from odoo import fields, models, api


class product_template(models.Model):
    _inherit = "product.template"

    @api.multi
    def _get_bom_cost(self):
        for product in self:
            bom_ids = self.env['mrp.bom'].search([('product_tmpl_id', '=', product.id)])
            if bom_ids:
                bom_cost = 0.0
                for bom in bom_ids:
                    bom_cost += bom.cost_per_unit
                product.bom_cost = bom_cost

    bom_cost = fields.Float(string="Product Including BOM Cost", compute="_get_bom_cost")

# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
