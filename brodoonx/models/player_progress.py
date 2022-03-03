from odoo import models, fields, api

class player_progress(models.Model):
    _name = 'brodoonx.player_progress'
    _description = 'Players progress'

    name = fields.Integer(string='level')
    date_char = fields.Char(default= lambda d: fields.datetime.now())
    player = fields.Many2one('res.partner')