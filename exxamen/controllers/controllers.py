# -*- coding: utf-8 -*-
# from odoo import http


# class Exxamen(http.Controller):
#     @http.route('/exxamen/exxamen/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/exxamen/exxamen/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('exxamen.listing', {
#             'root': '/exxamen/exxamen',
#             'objects': http.request.env['exxamen.exxamen'].search([]),
#         })

#     @http.route('/exxamen/exxamen/objects/<model("exxamen.exxamen"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('exxamen.object', {
#             'object': obj
#         })
