from odoo import models, fields, api

class engine(models.Model):
    _name          = 'koukaauto.engine'
    _description   = 'koukaauto.engine'

    name           = fields.Char()
    model_ids      = fields.Many2many('koukaauto.model')
