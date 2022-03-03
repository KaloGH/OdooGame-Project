from odoo import models, fields, api

#! /////////////////////////////  MUSICAL GENRE  \\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\

class musical_genre(models.Model):
     _name = 'brodoonx.musical_genre'
     _description = 'Available musical genres and all kind of information about them'

     name = fields.Char(required=True)
     audience = fields.Integer(required=True)
     songs = fields.Many2many('brodoonx.song', string='Songs') # Songs by musical genre
     singers = fields.Many2many('brodoonx.artist', relation='singers_musical_genre_table', column1='musical_genre_id',column2='artist_id') # Singers by musical genre
     producers = fields.Many2many('brodoonx.artist', relation='producers_musical_genre_table', column1='musical_genre_id',column2='artist_id') # Producers by musical genre

#! /////////////////////////////  END-MUSICAL GENRE  \\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\