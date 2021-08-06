# -*- coding: utf-8 -*-
# from odoo import http


# class LatihanFadhil(http.Controller):
#     @http.route('/latihan_fadhil/latihan_fadhil/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/latihan_fadhil/latihan_fadhil/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('latihan_fadhil.listing', {
#             'root': '/latihan_fadhil/latihan_fadhil',
#             'objects': http.request.env['latihan_fadhil.latihan_fadhil'].search([]),
#         })

#     @http.route('/latihan_fadhil/latihan_fadhil/objects/<model("latihan_fadhil.latihan_fadhil"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('latihan_fadhil.object', {
#             'object': obj
#         })
