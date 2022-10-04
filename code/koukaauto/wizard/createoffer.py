from pyexpat import model
from odoo import models , api , fields

class createoffer(models.TransientModel):
    _name          = 'koukaauto.createoffer'
    _description   = 'koukaauto.createoffer'


    def _default_vehicle(self):

        return self.env['koukaauto.vehiclead'].browse(self._context.get('active_id'))

    vehiclead_id    = fields.Many2one('koukaauto.vehiclead' , string="Vehicle", index=True, tracking=True, default=_default_vehicle )
    price_offer     = fields.Integer()
    user_id         = fields.Many2one('res.users',index=True, tracking=True, default=lambda self: self.env.user)


    def create_offer(self):
        vals = {
            'price'        : self.price_offer,
            'statut'       : '',
            'user_id'      : self.user_id.id ,
            'vehiclead_id' : self.vehiclead_id.id ,       
        }
        return self.env['koukaauto.offer'].create(vals)