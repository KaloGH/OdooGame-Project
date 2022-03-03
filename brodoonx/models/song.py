from odoo import models, fields, api

#! /////////////////////////////  SONG  \\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
#? Modelo cancion contiene informacion sobre la cancion que es creada. Es creada por ninguno o muchos cantantes 
#? y uno o mas productores
class song(models.Model):
     _name = 'brodoonx.song'
     _description = 'Song , pertains to one discography , have one producer and can have or not a singer'

     name = fields.Char(required=True)
     duration = fields.Integer(required=True,string="Duration (s)")
     views = fields.Integer(required=True)
     musical_genre = fields.Many2many(comodel_name='brodoonx.musical_genre', string='Musical Genre/s')
     discography = fields.Many2one('brodoonx.discography')     
     singers = fields.Many2many('brodoonx.artist' , relation='singers_song_table', column1='song_id',column2='artist_id')
     producers = fields.Many2many('brodoonx.artist', relation='producers_song_table', column1='song_id',column2='artist_id')


#! /////////////////////////////  END-SONG  \\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\