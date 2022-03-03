from odoo import models, fields, api

class furgoneta(models.Model):
    _name = 'examen.furgoneta'
    _description = 'examen.furgoneta'

    matricula = fields.Char(required=True)
    capacitat = fields.Float(required=True)
    viatges = fields.One2many('examen.viatge', 'furgoneta')
    paquets = fields.Many2many('examen.paquet')
    image = fields.Image(max_width=250 , max_height=250 , string="Imagen Furgoneta")

    # def _get_paquets(self):
    #     for frago in self:
    #         for viatge in frago.viatges:
    #             if(viatge.furgoneta == frago):
    #                 frago.paquets += viatge.paquets

