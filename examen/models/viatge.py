from odoo import models, fields, api
from odoo.exceptions import ValidationError
from random import seed
from random import random
seed(1)

# Cada viatge té un conductor (res.partner), un identificador, una furgoneta, una llista de paquets i els m3 aprofitats. 
# Un viatge no pot tindre més paquets dels que caben en la furgoneta.

class viatge(models.Model):
    _name = 'examen.viatge'
    _description = 'examen.viatge'

    conductor = fields.Many2one('res.partner')
    viatge_id = fields.Integer(default=lambda s: 0 + (random() * (1000 - 0)))
    furgoneta = fields.Many2one('examen.furgoneta')
    paquets = fields.Many2many('examen.paquet')
    metres_aprofitats = fields.Float(compute='_get_metres_aprofitats')
    
    def _get_metres_aprofitats(self):
        for viatge in self:
            _total_metres = 0
            for paquet in viatge.paquets:
                _total_metres += paquet.volum
            viatge.metres_aprofitats = _total_metres

    @api.constrains('paquets','furgoneta')
    def _check_something(self):
        for record in self:
            _volum_paquets_total = 0
            for paquet in record.paquets:
                _volum_paquets_total += paquet.volum

            if(_volum_paquets_total > record.furgoneta.capacitat):
                raise ValidationError("El tamaño de los paquetes excede la capacidad de la furgoneta")


