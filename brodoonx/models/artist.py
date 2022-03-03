from odoo import models, fields, api
from random import seed
from random import random
seed(1)
#! /////////////////////////////  ARTIST  \\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
#? Modelo cantante contiene informacion sobre el cantante. Solo pertenece a una discografica 
#? y tiene ninguna o muchas canciones
class artist(models.Model):
     _name = 'brodoonx.artist'
     _description = 'Artist which can be a part of discography or not'

     name = fields.Char(string='Name', required=True)
     genre = fields.Selection([
          ('m', 'Male'),
          ('f', 'Female')
     ], required=True)
     country = fields.Many2one('brodoonx.country',required=True)
     age = fields.Integer(string='Age', required=True)
     level = fields.Float(default=lambda s: 0 + (random() * (100 - 0)) ,string='Level')
     songs_as_prod = fields.Many2many('brodoonx.song', relation='producers_song_table',column1='artist_id', column2='song_id')
     songs_as_sing = fields.Many2many('brodoonx.song', relation='singers_song_table',column1='artist_id', column2='song_id')
     discography = fields.Many2one('brodoonx.discography')
# discography = fields.One2many('brodoonx.discography', 'producers')
     musical_genre_as_prod = fields.Many2many('brodoonx.musical_genre', relation='producers_musical_genre_table', column2='musical_genre_id',column1='artist_id')
     musical_genre_as_sing = fields.Many2many('brodoonx.musical_genre', relation='singers_musical_genre_table', column2='musical_genre_id',column1='artist_id')
     image = fields.Image(max_width=256 , max_height=256 , string="Photo")
     type_artist = fields.Selection([
          ('sing', 'Singer'),
          ('prod', 'Producer')
     ],required=True)

#! /////////////////////////////  END-ARTIST  \\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\