from odoo import models, fields, api
from random import seed
from random import random
seed(1)

class paquet(models.Model):
    _name = 'examen.paquet'
    _description = 'examen.paquet'

    paquet_id = fields.Integer(default=lambda s: 0 + (random() * (1000 - 0)), required=True)
    volum = fields.Float(required=True)
    furgoneta = fields.Many2many('examen.furgoneta')
    viatge = fields.Many2many('examen.viatge')