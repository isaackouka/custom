from itertools import product
from odoo import api, fields, models, _

class ArtecForecastPurchase(models.Model):
    _name = 'artec.forecast.purchase'
    _description = 'Artec Forecast Purchase'

    product_id = fields.Many2one(
        'product.product',
        string='Product',
        required=True,
        domain="[('detailed_type','=', 'product')]"
        )

    quantity_topurchase = fields.Integer(
        string='Quantity to purchase',
        required=True
    )
    
    date_purchase    = fields.Date()


    @api.constrains('product_id')
    def constrains_product_id(self):
        if self.env['artec.forecast.product'].search([('product_id','=',self.product_id.id)]):
            forecast = self.env['artec.forecast.product'].search([('product_id','=',self.product_id.id)])
            if self.date_purchase < forecast[0].date_forecasted :
                val = {
                    'product_id' : self.product_id.id,    
                    'qty_forecasted' : self.product_id.qty_available + self.quantity_topurchase ,  
                    'date_forecasted' : self.date_purchase,  
                }
                self.env['artec.forecast.product'].create(val)
                print("date ",self.date_purchase)
                for i in range(len(forecast)):
                    forecast[i].write({'qty_forecasted': forecast[i].qty_forecasted + self.quantity_topurchase})
                    
                    print("date ",forecast[i].date_forecasted)
            else:
                last=True
                for i in range(len(forecast)):
                    if self.date_purchase < forecast[i].date_forecasted :
                        val = {
                            'product_id' : self.product_id.id,    
                            'qty_forecasted' : forecast[i].qty_forecasted + self.quantity_topurchase ,  
                            'date_forecasted' : self.date_purchase,  
                        }
                        self.env['artec.forecast.product'].create(val)
                        print("date ",forecast[i-1].date_forecasted)
                        j=i
                        while j<len(forecast):
                            forecast[j].write({'qty_forecasted': forecast[j].qty_forecasted + self.quantity_topurchase})
                            print("date ",forecast[j].date_forecasted)
                            j=j+1
                        last=False
                        break
                if last == True :    
                    print("the self is the last ")

                # elif forecast[i].date_forecasted < self.date_purchase:
                #     print("date ",forecast[i].date_forecasted)
                # j = len(forecast)-1
                # print("date ",forecast[j].date_forecasted)

        # else :
        #     val = {
        #         'product_id' : self.product_id.id,    
        #         'qty_forecasted' : self.product_id.qty_available + self.quantity_topurchase ,  
        #         'date_forecasted' : self.date_purchase,  
        #     }
        #     self.env['artec.forecast.product'].create(val)



        #     forecasted_product = self.env['artec.forecast.product'].search([('product_id','=',self.product_id.id)])
        #     qty_forc = forecasted_product.qty_forecasted - self.quantity_topurchase
        #     #forecasted_product.write({'qty_forecasted': qty_forc})
        #     if self.date_purchase > forecasted_product.date_forecasted:
        #         forecasted_product.write({'date_forecasted': self.date_purchase})


        #     val = {
        #         'product_id' : self.product_id.id,    
        #         'qty_forecasted' : qty_forc,  
        #         'date_forecasted' : self.date_purchase,  
        #     }
        #     self.env['artec.forecast.product'].create(val)
