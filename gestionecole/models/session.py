from logging import warning
from tokenize import blank_re
from odoo import api, models , fields

class session(models.Model):
    _name              = "gestionecole.session"
    _description       = "gestionecole.session"

    name               = fields.Char()
    date               = fields.Date()
    number_seat        = fields.Integer()
    formation_id       = fields.Many2one("gestionecole.formation" , string="Formation")
    teacher_id         = fields.Many2one("gestionecole.teacher" , string="Teacher")

    # @api.onchange('number_seat')
    # def check_number_seats(self):
    #     if self.number_seat != 20 :
    #         return {'warning': {
    #                     'title': ("Warning"),
    #                     'message': ('Number of seats must be 20 seats pes session')
    #                     }
    #                 }