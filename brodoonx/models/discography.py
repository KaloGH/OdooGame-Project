from odoo import models, fields, api
import random


#! /////////////////////////////  DISCOGRAPHY  \\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
#? Modelo Discography , es la discografica que gestionara el usuario , el cual sera su duño. 
#? La reputacion sera la fama que tendra la discografica y lo que determinara su nivel , a mayor reputacion mayor nivel
#? El presupuesto sera el dinero que tendra la discografica.
#? Lista de cantantes contratados que le costaran un dinero temporal a la discografica y generaran dinero
#? Lista de productores contratados que le costaran un dinero temporal a la discografica y generaran dinero
#? Lista de canciones de la discografica , historial de los mejores temas que ha tenido y el dinero que le han generado
class discography(models.Model):
     _name = 'brodoonx.discography'
     _description = 'Discography which is managed by the Player'

     name = fields.Char(string='Name',required=True)
     reputation = fields.Float(string='Reputation',compute='_get_reputation_value')
     budget = fields.Float(string='Budget', digits=(20,2) , default=200 , required=True)
     owner = fields.Many2one(comodel_name='res.partner', required=True, ondelete='cascade', help='The owner of the discography')
     singers = fields.Many2many(comodel_name='brodoonx.artist', compute='_get_singers' ,help='List of the singers that are working for this discography')
     producers = fields.Many2many(comodel_name='brodoonx.artist', compute='_get_producers' ,help='List of the producers that are working for this discography')
     songs = fields.One2many('brodoonx.song', 'discography')
     country = fields.Many2one('brodoonx.country')

     def generate_random_song(self):
          for disc in self:
               song =  random.choice(self.env['brodoonx.song'].search([]).ids)
               disc.write({'songs': [(4,song,0)]})

     def _get_singers(self):
          for disc in self:
               disc.singers = self.env['brodoonx.artist'].search([('discography', '=', disc.id),('type_artist','=','sing')]).ids
     
     def _get_producers(self):
          for disc in self:
               disc.producers = self.env['brodoonx.artist'].search([('discography', '=', disc.id),('type_artist','=','prod')]).ids

     @api.depends('songs','singers','producers')
     def _get_reputation_value(self):
          for disc in self:
               _total_artists_level = 0
               _total_views = 0
               
               if len(disc.singers) > 0:
                    for singer in disc.singers:
                         _total_artists_level += singer.level

               if len(disc.producers) > 0:
                    for producer in disc.producers:
                         _total_artists_level += producer.level

               if len(disc.songs) > 0:
                    for song in disc.songs:
                         _total_views += song.views

               disc.reputation = _total_artists_level + _total_views * 0.05
          
               

#! /////////////////////////////  END-DISCOGRAPHY  \\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\