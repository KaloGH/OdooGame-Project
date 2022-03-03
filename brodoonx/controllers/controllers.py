# -*- coding: utf-8 -*-
from odoo import http

class Brodoonx(http.Controller):
    @http.route('/brodoonx/discography', auth='user', type='json')
    def discographie(self):
        return {
            'html': """
                <div id="brodoonx_banner">
                    <link href="/brodoonx/static/src/css/banner.css"
                        rel="stylesheet">
                        <h1>Discographies</h1>
                        <p>Creating new discographies</p>
                        <a class="btn_newDisc" type="action" data-reload-on-close="true" role="button" data-method="action_discography_wizard" data-model="brodoonx.discography_wizard">
                            <span> New Discography</span>
                        </a>
                        </div> """
        }

    @http.route('/brodoonx/battle', auth='user', type='json')
    def battle(self):
        return {
            'html': """
                <div id="brodoonx_banner">
                    <link href="/brodoonx/static/src/css/banner.css"
                        rel="stylesheet">
                        <h1>Battles</h1>
                        <p>Creating new fight</p>
                        <a class="btn_newDisc" type="action" data-reload-on-close="true" role="button" data-method="action_battle_wizard" data-model="brodoonx.battle_wizard">
                            <span> New Fight</span>
                        </a>
                        </div> """
        }

#     @http.route('/brodoonx/brodoonx/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('brodoonx.listing', {
#             'root': '/brodoonx/brodoonx',
#             'objects': http.request.env['brodoonx.brodoonx'].search([]),
#         })

#     @http.route('/brodoonx/brodoonx/objects/<model("brodoonx.brodoonx"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('brodoonx.object', {
#             'object': obj
#         })
