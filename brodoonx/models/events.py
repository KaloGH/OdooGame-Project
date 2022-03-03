from odoo import models, fields, api

class events(models.Model):
    _name = 'brodoonx.events'
    _description = 'Events in the game'

    name = fields.Char(string='Event Name')
    init_date = fields.Datetime(string="Starts on")
    fin_date = fields.Datetime(string="Finishes on")
