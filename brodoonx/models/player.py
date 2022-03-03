from odoo import models, fields, api
import re
import logging
import secrets
from odoo.exceptions import ValidationError

_logger = logging.getLogger(__name__)

#! /////////////////////////////  PLAYER  \\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
#? Modelo Player , va a ser el jugador principal que se registra. Podra gestionar una o mas discograficas
# TODO://///> hacer que el jugador en un principio solo pueda gestionar una discografica
# TODO://///> para gestionar mas discograficas se debe vender la ya existente , declararse en bancarrota, o pagar.
class player(models.Model):
     _name = 'res.partner'
     _inherit = 'res.partner'
     #_description = 'brodoonx.player'

     #name = fields.Char(string='Username',required=True)
     #user_email = fields.Char(required=True)
     is_player = fields.Boolean(default=False)
     user_password = fields.Char()
     user_discography = fields.One2many(comodel_name='brodoonx.discography', inverse_name='owner', string='Discographies')
     user_joinDate = fields.Datetime(default=lambda self: fields.Datetime.now())
     player_progress = fields.One2many(comodel_name='brodoonx.player_progress',inverse_name='player')
     level = fields.Integer()


     #isPremium = fields.Boolean(default=False , string="Premium")



     # Comprueba correo electronico y hace un restrict para que el email sea unico.
     @api.constrains('email')
     def _check_valid_email(self):
          regex = re.compile(r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b')
          for s in self:
               if(regex.match(s.email)):
                    _logger.debug('\033[94m'+str(s.email)+'\033[0m')
               else:
                    raise ValidationError('The email is wrong')
     
     _sql_constraints = [('email_uniq','unique(email)','Email already used')]

     @api.constrains('is_premium','user_discography')
     def _check_something(self):
          for record in self:
               if(record.is_premium == False and len(record.user_discography) > 1):
                    raise ValidationError("This user isn't premium , only can have one Discography")
    
     def generate_new_password(self):
          for s in self:
               password = secrets.token_urlsafe(12)
               s.write({'user_password':password})

     def change_join_date_to_now(self):
          for s in self:
               date = fields.Datetime.now()
               s.write({'user_joinDate':date})

     @api.model
     def update_players_progress(self):
          players = self.search([])
          date = fields.datetime.now()
          disco_level = 0
          for p in players:
               last_level = p.level
               for disc in p.user_discography:
                    disco_level = disco_level + round(disc.reputation)
               p.level = round(disco_level)
               #print(p.level, last_level)
               ##  if last_level != p.level:
               self.env['brodoonx.player_progress'].create({'name': p.level, 'player': p.id, 'date_char': date})

     def show_player_progress(self):
          return {
          'name': 'Player progress',
          'type': 'ir.actions.act_window',
          'res_model': 'brodoonx.player_progress',
          'view_mode': 'graph',
          'target': 'new',
          'context':  self._context,
          'domain': [('player', '=', self.id)]
          }

     

#! /////////////////////////////  END-PLAYER  \\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\