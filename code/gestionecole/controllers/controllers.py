# -*- coding: utf-8 -*-
# from odoo import http


# class Gestionecole(http.Controller):
#     @http.route('/gestionecole/gestionecole', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/gestionecole/gestionecole/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('gestionecole.listing', {
#             'root': '/gestionecole/gestionecole',
#             'objects': http.request.env['gestionecole.gestionecole'].search([]),
#         })

#     @http.route('/gestionecole/gestionecole/objects/<model("gestionecole.gestionecole"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('gestionecole.object', {
#             'object': obj
#         })
