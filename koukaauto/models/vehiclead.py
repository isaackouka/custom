from copy import copy
from email.policy import default
from plistlib import UID
from re import template
from odoo.exceptions import ValidationError
from odoo import models, fields, api,_
from datetime import datetime
from logging import warning

class vehiclead(models.Model):
    _name          = 'koukaauto.vehiclead'
    _description   = 'koukaauto.vehiclead'

    ref            = fields.Char(copy=False,required=True,readonly=True, default=lambda self:_('New'))
    state          = fields.Selection(selection=[('New', 'New'),('Offer receved', 'Offer receved'),('Offer accepted', 'Offer accepted'),('Solded','Solded'),('Canceled','Canceled')])
    user_id        = fields.Many2one('res.users', string='Seller', index=True, tracking=True, default=lambda self: self.env.user)
    name           = fields.Char(compute="_value_pc")
    mark_id        = fields.Many2one('koukaauto.mark')
    model_id       = fields.Many2one('koukaauto.model',domain="[('mark_id','=', mark_id)]")
    finition_id    = fields.Many2one("koukaauto.finition",domain="[('model_ids','=', model_id)]" )
    color          = fields.Char()
    engine_id      = fields.Many2one("koukaauto.engine",domain="[('model_ids','=', model_id)]" )
    energy         = fields.Selection(selection=[('Essence', 'Essence'),('Diesel', 'Diesel')])
    gearbox        = fields.Selection(selection=[('Manuel', 'Manuel'),('Auto', 'Auto')])
    km             = fields.Integer()
    expected_price = fields.Integer()
    @api.model
    def year_selection(self):
        year = 2000
        year_list = []
        while year <= 2022: 
            year_list.append((str(year), str(year)))
            year += 1
        return year_list
    year           = fields.Selection(year_selection,)
    description    = fields.Text()
    offer_ids      = fields.One2many('koukaauto.offer' , 'vehiclead_id')
    best_offer     = fields.Integer(compute="_bestprice",store=True)
    partner_id     = fields.Many2one('res.partner',string="Buyer",compute="_buyer")
    selling_price  = fields.Integer(compute="_selling_price")
    city           = fields.Selection(selection=[('Adrar', 'Adrar'),
        ('Chlef', 'Chlef'),
        ('Adrar', 'Adrar'),
        ('Laghouat', 'Laghouat'),
        ('Oum El Bouaghi', 'Oum El Bouaghi'),
        ('Batna', 'Batna'),
        ('Béjaïa', 'Béjaïa'),
        ('Biskra', 'Biskra'),
        ('Béchar', 'Béchar'),
        ('Blida', 'Blida'),
        ('Bouira', 'Bouira'),
        ('Tamanrasset', 'Tamanrasset'),
        ('Tébessa', 'Tébessa'),
        ('Tlemcen', 'Tlemcen'),
        ('Tiaret', 'Tiaret'),
        ('Tizi Ouzou', 'Tizi Ouzou'),
        ('Alger', 'Alger'),
        ('Djelfa', 'Djelfa'),
        ('Jijel', 'Jijel'),
        ('Sétif', 'Sétif'),
        ('Saïda', 'Saïda'),
        ('Skikda', 'Skikda'),
        ('Sidi Bel Abbès', 'Sidi Bel Abbès'),
        ('Annaba','Annaba'),
        ('Guelma','Guelma'),
        ('Constantine','Constantine'),
        ('Médéa','Médéa'),
        ('Mostaganem','Mostaganem'),
        ('M\'Sila','M\'Sila'),
        ('Mascara','Mascara'),
        ('Ouargla','Ouargla'),
        ('Oran ','Oran'),
        ('El Bayadh ','El Bayadh'),
        ('Illizi','Illizi'),
        ('Bordj Bou Arreridj','Bordj Bou Arreridj'),
        ('Boumerdès','Boumerdès'),
        ('El Tarf','El Tarf'),
        ('Tindouf','Tindouf'),
        ('Tissemsilt ','Tissemsilt'),
        ('El Oued','El Oued'),
        ('Khenchela','Khenchela'),
        ('Souk Ahras','Souk Ahras'),
        ('Tipaza','Tipaza'),
        ('Mila','Mila'),
        ('Aïn Defla','Aïn Defla'),
        ('Naâma','Naâma'),
        ('Aïn Témouchent', 'Aïn Témouchent'),
        ('Ghardaïa','Ghardaïa'),
        ('Relizane','Relizane'),
        ('Timimoun','Timimoun'),
        ('Bordj Badji Mokhtar','Bordj Badji Mokhtar'),
        ('Ouled Djellal','Ouled Djellal'),
        ('Béni Abbès ','Béni Abbès'),
        ('In Salah','In Salah'),
        ('In Guezzam ','In Guezzam '),
        ('Touggourt ','Touggourt '),
        ('Djanet ','Djanet '),
        ('El M\'Ghair ','El M\'Ghair '),
        ('El Meniaa','El Meniaa')])
    is_seller      = fields.Boolean(default=False ,compute="_is_user")
    image_ids      = fields.One2many('product.image','vehicle_id', string="Images", copy=True)

# calcule name 
    @api.depends("name")
    def _value_pc(self):
        for record in self:
            record.sudo().write({
                'name': record.mark_id.name+" "+record.model_id.name
            })

#calcule best offers
    @api.depends("offer_ids")
    def _bestprice(self):
        list = []
        for record in self:
            if record.offer_ids :
                for i in range(len(record.offer_ids)):
                    list.append(record.offer_ids[i].price)
                
                record.sudo().write({
                'best_offer': max(list)
                })
                record.sudo().write({
                'state': "Offer receved"
                })

            else:
                record.sudo().write({
                'best_offer': 0
                })
                record.sudo().write({
                'state': "New"
                })

# prix de vente
    @api.depends("offer_ids")
    def _selling_price(self):
            if self.offer_ids :
                for element in self.offer_ids:
                    if element.statut == "accepte":
                        # self.selling_price = element.price
                        # self.state         = "Offer accepted"
                        self.sudo().write({
                        'selling_price': element.price
                        })
                        self.sudo().write({
                        'state': "Offer accepted"
                        })

                    else : 
                        # self.selling_price = 0
                        # self.state         = "Offer receved"
                        self.sudo().write({
                        'selling_price': 0
                        })
                        self.sudo().write({
                        'state': "Offer receved"
                        })
            else : 
                # self.selling_price = 0
                # self.state         = "New"
                self.sudo().write({
                        'selling_price': 0
                        })
                self.sudo().write({
                        'state': "New"
                        })

# annuler l annonce
    def cancel_vehiclead(self):
        for record in self :
            if record.state  == "Solded":
                raise ValidationError(_("You cannot cancel announce is solded"))
            else:
                record.state  = "Canceled"
# vendu annonce
    def sold_vehiclead(self):
        for record in self :
            if record.state  == "Canceled":
                raise ValidationError(_("You cannot solded announce is canceled"))
            else:
                record.state = "Solded"
#cree l achteur
    @api.depends("offer_ids")
    def _buyer(self):
        for record in self:
            if record.offer_ids :
                for element in record.offer_ids:
                    if element.statut == "accepte":
                        # record.partner_id = element.partner_id
                        record.sudo().write({
                            'partner_id' : element.partner_id
                        })
                    else :
                        # record.partner_id = False
                        record.sudo().write({
                            'partner_id' : False
                        })
            else :
                # record.partner_id = False
                record.sudo().write({
                            'partner_id' : False
                        })

#cree l annonce avec state = New
    @api.model
    def create(self, vals):
        vals['state'] ="New"
        vals['ref']   = self.env['ir.sequence'].next_by_code('koukaauto.vehiclead') or _("New")
        return super(vehiclead,self).create(vals)

    @api.ondelete(at_uninstall=False)
    def _check_offer_sold(self):
        for record in self :
            if record.offer_ids :
                raise ValidationError(_("You cannot delate announce have offers"))

    @api.model
    def report_pdf(self):
        return self.env.ref('koukaauto.report_vehiclead').report_action(self)

    @api.depends("user_id")
    def _is_user(self):
        if self.user_id == self.env.user : 
            self.is_seller = True
        else :
            self.is_seller = False
    
    def action_view_invoice(self):
        return {
        "type": "ir.actions.act_window",
        "name": "Models",
        "res_model": "koukaauto.model",
        # "domain":['mark_id.id','=', self.mark_id.id],
        "context": {},
        'view_mode': 'tree,form',
        "target" : "current",
        }

    def send_email_validator(self):
        # template_id = self.env.ref("koukaauto.email_validator_technical").id
        # template2 = self.env['mail.mail'].browse(template_id)
        # template2.send(template2)
        body = """
            <b>Salut,</b>
            <br><b>Technical Validation.</b>
            <br>Le client {0} veut affecter un achat dont le montant dépasse le limite crédit défini dans le contrat
            <br>
            <br>Cordialement
            """.format(
            self.user_id.name,
        )
        recipient = self.user_id.partner_id.email
        if recipient:
            template_data = {
                'subject': 'Limit Credit Dépassé',
                'body_html': body,
                'email_to': ','.join(recipient)
            }
            template_id = self.env['mail.mail'].sudo().create(
                template_data)
            template_id.send(template_data)