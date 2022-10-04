from odoo import api, fields, models

class ProductImage(models.Model):
    _inherit = [
        "product.image",
    ]

    vehicle_id = fields.Many2one('koukaauto.vehiclead', index=True, ondelete='cascade')