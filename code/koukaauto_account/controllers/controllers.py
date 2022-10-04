# -*- coding: utf-8 -*-
# from odoo import http


# class KoukaautoAccount(http.Controller):
#     @http.route('/koukaauto_account/koukaauto_account', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/koukaauto_account/koukaauto_account/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('koukaauto_account.listing', {
#             'root': '/koukaauto_account/koukaauto_account',
#             'objects': http.request.env['koukaauto_account.koukaauto_account'].search([]),
#         })

#     @http.route('/koukaauto_account/koukaauto_account/objects/<model("koukaauto_account.koukaauto_account"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('koukaauto_account.object', {
#             'object': obj
#         })
