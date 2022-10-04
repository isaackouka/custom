# -*- coding: utf-8 -*-
# from odoo import http


# class ArtecStockForcast(http.Controller):
#     @http.route('/artec_stock_forcast/artec_stock_forcast', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/artec_stock_forcast/artec_stock_forcast/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('artec_stock_forcast.listing', {
#             'root': '/artec_stock_forcast/artec_stock_forcast',
#             'objects': http.request.env['artec_stock_forcast.artec_stock_forcast'].search([]),
#         })

#     @http.route('/artec_stock_forcast/artec_stock_forcast/objects/<model("artec_stock_forcast.artec_stock_forcast"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('artec_stock_forcast.object', {
#             'object': obj
#         })
