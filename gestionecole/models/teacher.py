# -*- coding: utf-8 -*-
from odoo import models, fields, api

class teacher(models.Model):
    _name             = 'gestionecole.teacher'
    _description      = 'gestionecole.teacher'
    _order            = 'name desc'
    
    first_name        = fields.Char()
    last_name         = fields.Char()
    name              = fields.Char(compute="_compute_name")
    formation_ids     = fields.Many2many("gestionecole.formation" , string="Formations")
    sequence          = fields.Integer('Sequence', default=1 )
    
    @api.depends("first_name","last_name")
    def _compute_name(self):
        for record in self:
            record.name = record.first_name+" "+record.last_name

    def action_do_something(self):
        for r in self :
            r.first_name = "ishak"
        return True
