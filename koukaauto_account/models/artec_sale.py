# -*- coding: utf-8 -*-
from odoo import api, fields, models


class ArtecSaleOrder(models.Model):
    
    _inherit = 'sale.order'

    _sql_constraints = [('order_product_uniq', 'unique (order_id,product_id)', 'Duplicate products in order line not allowed !')]