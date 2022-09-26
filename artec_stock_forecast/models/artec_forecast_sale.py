from itertools import product
from odoo import api, fields, models, _

class ArtecForecastSale(models.Model):
    _name = 'artec.forecast.sale'
    _description = 'Artec Forecast Sale'

    product_id = fields.Many2one(
        'product.product',
        string='Product',
        required=True,
        domain="[('detailed_type','=', 'product')]"
        )

    quantity_tosale = fields.Integer(
        string='Quantity to sale',
        required=True
    )

    date_sale = fields.Date()


    @api.constrains('product_id')
    def constrains_product_id(self):
        if self.env['artec.forecast.product'].search([('product_id','=',self.product_id.id)]):
            forecasted_product = self.env['artec.forecast.product'].search([('product_id','=',self.product_id.id)])
            qty_forc = forecasted_product.qty_forecasted - self.quantity_tosale
            forecasted_product.write({'qty_forecasted': qty_forc})
            if self.date_sale > forecasted_product.date_forecasted:
                forecasted_product.write({'date_forecasted': self.date_sale})
        else :
            val = {
                'product_id' : self.product_id.id,    
                'qty_forecasted' : self.product_id.qty_available - self.quantity_tosale ,  
                'date_forecasted' : self.date_sale,  
            }
            self.env['artec.forecast.product'].create(val)