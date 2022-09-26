from odoo import models, fields, api,_

class lot(models.Model):
    _inherit         = ['stock.move.line']

    lot_name     = fields.Char('Lot/Serial Number Name',copy=False,required=True,readonly=True, default=lambda self:self.env['ir.sequence'].next_by_code('stock.move.line'))
    refused_qty  = fields.Integer()

    