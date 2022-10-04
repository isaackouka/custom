# -*- coding: utf-8 -*-
from odoo import models, fields, api

class formation(models.Model):
    _name            = 'gestionecole.formation'
    _description     = 'gestionecole.formation'

    name             = fields.Char(string="Titre",required=True)
    description      = fields.Text()
    teacher_ids      = fields.Many2many('gestionecole.teacher', string="Teachers")
    #len(teacher_ids)