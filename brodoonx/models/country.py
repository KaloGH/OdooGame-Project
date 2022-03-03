from itertools import count
from operator import gt
from odoo import models, fields, api
from random import seed
from random import random
seed(1)

#! /////////////////////////////  COUNTRY  \\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\

class country(models.Model):
     _name = 'brodoonx.country'
     _description = 'Information about country and what poblation it have'

     name = fields.Char(required=True)
     population = fields.Integer(required=True)
     discography_list = fields.One2many('brodoonx.discography', 'country')
     artists_list = fields.One2many('brodoonx.artist', 'country')

     #! /////////////////////////////  CRONS   \\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
     def update_population(self):
          all_countries = self.env['brodoonx.country'].search([])
          for country in all_countries:
               randnum = 0 + (random() * (100 - 0))
               isPlus = True if random() > 0.5 else False
               if isPlus:
                    country.population += randnum
                    #print("Población de "+ country.name +" ha subido con "+str(randnum)+" habitantes.")
               else:
                    country.population -= randnum
                    #print("Población de "+ country.name +" ha bajado con "+str(randnum)+" habitantes.")
#! /////////////////////////////  END-COUNTRY   \\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\

