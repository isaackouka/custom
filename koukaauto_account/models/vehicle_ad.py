from odoo import models, fields, api , Command
class vehicle_ad(models.Model):
    _inherit         = 'koukaauto.vehiclead'

    def sold_vehiclead(self):
        print("fonction herité")
        # for record in self:
        #     journal = record.env['account.journal'].sudo().search([('type','=','sale')])
        #     account = self.env['account.move'].sudo().create(
        #         {
        #             "partner_id"       : record.partner_id.id,
        #             "move_type"        :"out_invoice",
        #             "journal_id"       : journal.id ,
        #             "invoice_line_ids" : [
        #                 Command.create({
        #                     "name"       :"Move",
        #                     "quantity"   : 1 ,
        #                     "price_unit" : record.selling_price
        #                 })
        #             ],
        #         }
        #     )
        #     return super(vehicle_ad,self).sold_vehiclead()