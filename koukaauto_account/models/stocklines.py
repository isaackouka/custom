from odoo import models, fields, api,_

class stocklines(models.Model):
    _inherit         = ['stock.move']

    refused_qty  = fields.Integer(compute="_compute" , store=True)

    @api.depends("move_line_ids")
    def _compute(self):
        for record in self :
            if record.move_line_ids:
                record.refused_qty=0
                for i in range(len(record.move_line_ids)):
                    record.refused_qty += record.move_line_ids[i].refused_qty
            else :
                record.refused_qty=0