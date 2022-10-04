from itertools import product
import string
from odoo import api, fields, models, _
from odoo.exceptions import ValidationError


class ArtecForecastProduct(models.Model):
    _name = 'artec.forecast.product'
    _description = 'Artec Forecast Product'
    _order = 'date_forecasted'

    product_id = fields.Many2one(
        'product.product',
        string='Product',
    )
    qty_available = fields.Float(
        related='product_id.qty_available'
        )

    qty_forecasted = fields.Float(
        string='Forecasted Quantity',
    )

    date_forecasted = fields.Date(
        string='Forecasted Date'
    )
    
    forecast_state = fields.Selection(
        selection=[('normal', 'Stock Normal'),('out', 'Stock Out')],
        compute='_compute_forecast_state',
    )

    @api.depends('qty_forecasted')
    def _compute_forecast_state(self):
        for record in self :
            if record.qty_forecasted >= 0 :
                record.forecast_state ='normal'
            else:
                record.forecast_state ='out'
