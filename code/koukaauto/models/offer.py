from odoo import models, fields, api , _
from odoo.osv import expression
from odoo.exceptions import ValidationError

class offer(models.Model):
    _name          = 'koukaauto.offer'
    _description   = 'koukaauto.offer'

    price          = fields.Integer(required=True)
    statut         = fields.Selection(selection=[('accepte', 'accepte'),('refuse', 'refuse'),])
    user_id        = fields.Many2one('res.users',string="Partner Offer")
    vehiclead_id   = fields.Many2one('koukaauto.vehiclead')


    def accept_offer(self):
        for record in self:
            record.statut = "accepte"

    def refuse_offer(self):
        for record in self:
            record.statut = "refuse"

    # _sql_constraints = [
    #     ('check_price', 'CHECK(price > 0 )',
    #      'The price should be positive.')
    # ]

    # cree offre avec condition prix est plus que le prix de l annonce
    # @api.model
    # def create(self, vals):
    #     prix = self.env['koukaauto.vehiclead'].browse(vals['vehiclead_id'])
    #     if vals['price'] >= prix.expected_price:
    #         res = super(offer,self).create(vals)
    #         return res
    #     else : 
    #         raise ValidationError(_("You cannot put this offers"))