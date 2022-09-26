from odoo import models, fields, api

class mark(models.Model):
    _name          = 'koukaauto.mark'
    _description   = 'koukaauto.mark'

    name           = fields.Char()
    vehiclead_ids  = fields.One2many('koukaauto.vehiclead', 'mark_id')
