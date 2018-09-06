# -*- coding: utf-8 -*-
##############################################################################
#
#    OpenERP, Open Source Management Solution
#    Copyright (C) 2015 Devintelle Software Solutions (<http://devintellecs.com>).
#
##############################################################################
{
    'name': 'BOM Cost Price',
    'version': '1.1',
    'category': 'Generic Modules/Manufacturing',
    'sequence': 1,
    'summary': 'App will add cost per unit on bom and cost price on bom components lines.',
    'description': """
         App will add cost per unit on bom and cost price on bom components lines.
 """,
    'author': 'DevIntelle Consulting Service Pvt.Ltd',
    'website': 'http://devintellecs.com/',
    'depends': ['mrp'],
    'data': [
        'views/mrp_view.xml',
        'views/view_product_template.xml',
    ],
    'demo': [],
    'test': [],
    'css': [],
    'qweb': [],
    'js': [],
    'images': ['images/main_screenshot.png'],
    'installable': True,
    'application': True,
    'auto_install': False,
    'price':10.0,
    'currency':'EUR',
  #  'live_test_url':'https://youtu.be/A5kEBboAh_k',
}
# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
