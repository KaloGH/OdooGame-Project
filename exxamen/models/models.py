# -*- coding: utf-8 -*-
from odoo import models, fields, api


class cancion(models.Model):
    _name = 'exxamen.cancion'
    _description = 'exxamen.cancion'

    name = fields.Char()
    artista = fields.Char()
    popularidad = fields.Integer()
    clientes = fields.Many2many('res.partner', 
                                relation='clientes_canciones', 
                                column1='id_cancion',
                                column2='id_cliente')

    def restaPopularidad(self):
        all_songs = self.env['exxamen.cancion'].search([])
        for song in all_songs:
            if song.popularidad != 0:
                song.popularidad -= 1
               

class clientes(models.Model):
     _name = 'res.partner'
     _inherit = 'res.partner'

     favouriteSongs = fields.Many2many('exxamen.cancion', 
                                relation='clientes_canciones', 
                                column1='id_cliente',
                                column2='id_cancion')



class song_wizard(models.TransientModel):
    _name = 'exxamen.song_wizard'

    song = fields.Many2one('exxamen.cancion')
    cliente = fields.Many2one('res.partner')

    @api.model
    def action_song_wizard(self):
        action = self.env.ref('exxamen.action_song_wizard').read()[0]
        print('===========================')
        print("Entra aqui")
        return action


    def add_song(self):
        self.song.write({'popularidad': self.song.popularidad + 100 })
        self.cliente.write({'favouriteSongs': [(4, self.song.id)]})
        

    
       

        return {
                'name': 'Add song',
                'type': 'ir.actions.act_window',
                'res_model': 'res.partner',
                'res_id': self.cliente.id,
                'view_mode': 'form',
                'target': 'current'
            }


