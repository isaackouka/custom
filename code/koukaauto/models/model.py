from odoo import models, fields, api
from datetime import datetime

class model(models.Model):
    _name          = 'koukaauto.model'
    _description   = 'koukaauto.model'

    mark_id        = fields.Many2one('koukaauto.mark')
    name           = fields.Char()
    engine_ids     = fields.Many2many("koukaauto.engine")
    finition_ids   = fields.Many2many("koukaauto.finition")
    year1          = fields.Integer()
    year2          = fields.Integer()