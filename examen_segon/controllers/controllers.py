# -*- coding: utf-8 -*-
# from odoo import http


# class ExamenSegon(http.Controller):
#     @http.route('/examen_segon/examen_segon/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/examen_segon/examen_segon/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('examen_segon.listing', {
#             'root': '/examen_segon/examen_segon',
#             'objects': http.request.env['examen_segon.examen_segon'].search([]),
#         })

#     @http.route('/examen_segon/examen_segon/objects/<model("examen_segon.examen_segon"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('examen_segon.object', {
#             'object': obj
#         })
