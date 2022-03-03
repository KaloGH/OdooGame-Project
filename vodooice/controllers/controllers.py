# -*- coding: utf-8 -*-
# from odoo import http


# class Vodooice(http.Controller):
#     @http.route('/vodooice/vodooice/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/vodooice/vodooice/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('vodooice.listing', {
#             'root': '/vodooice/vodooice',
#             'objects': http.request.env['vodooice.vodooice'].search([]),
#         })

#     @http.route('/vodooice/vodooice/objects/<model("vodooice.vodooice"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('vodooice.object', {
#             'object': obj
#         })
