from odoo.http import request
from odoo import http
import json

class Koukaauto(http.Controller):
    @http.route('/', auth='public',type='http',website=True,csrf=False)
    def home(self,**kw):
        vehicleads = http.request.env['koukaauto.vehiclead'].sudo().search([])
        return request.render("koukaauto_web.koukaauto_home",{
            "vehicleads":vehicleads
        })

    @http.route('/vehicle/<int:vehiclead_id>',  auth='public', type='http', website=True, csrf=False)
    def vehicle(self,vehiclead_id,page="1",**kw):
        vehicle = http.request.env['koukaauto.vehiclead'].browse(vehiclead_id)
        return request.render("koukaauto_web.vehicle",{
            "vehicle":vehicle
        })


    @http.route('/koukaauto',  auth='public', type='http', website=True, csrf=False)
    def index(self, **kw):
        marks = http.request.env['koukaauto.mark'].sudo().search([])
        models = http.request.env['koukaauto.model'].sudo().search([])
        finitions = http.request.env['koukaauto.finition'].sudo().search([])
        engines = http.request.env['koukaauto.engine'].sudo().search([])
        return request.render("koukaauto_web.website",{
            "marks":marks,
            "models":models,
            "finitions":finitions,
            "engines":engines,
        })

    @http.route('/koukaauto/mark/', auth='public', type='json', website=True, csrf=False)
    def mark(self, **kw):
        if kw["selectedmark"]:
            data = json.loads(kw["selectedmark"])
            model = http.request.env['koukaauto.model'].sudo().search_read([('mark_id.id', '=?', data)], ['name'])
            return model
            
    @http.route('/koukaauto/model/', auth='public', type='json', website=True, csrf=False)
    def finition_engine(self, **kw):
        if kw["selectedmodel"]:
            data = json.loads(kw["selectedmodel"])
            finition = http.request.env['koukaauto.finition'].sudo().search_read([('model_ids.id', '=?', data)], ['name'])
            return finition

    @http.route('/koukaauto/send/', auth='public', type='http', website=True, csrf=True)
    def get_data(self, **kw):
        errors = list()
        if kw:
            if errors == []:
                new_partner = http.request.env['koukaauto.vehiclead'].sudo().create(kw)
                return request.render("koukaauto_web.koukaauto_home")
            else:
                return "<div class='alert alert-warning' role='alert'>ERROR : INVALIDE DATA </div>"
        else:
            return "<div class='alert alert-warning' role='alert'> SOMETHING WENT WRONG </div>"
