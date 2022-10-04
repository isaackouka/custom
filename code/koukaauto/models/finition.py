from odoo import models, fields, api

class finition(models.Model):
    _name          = 'koukaauto.finition'
    _description   = 'koukaauto.finition'

    name           = fields.Char()
    model_ids      = fields.Many2many('koukaauto.model')