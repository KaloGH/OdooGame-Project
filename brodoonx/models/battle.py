from odoo import models, fields, api

class battle(models.Model):
	_name = 'brodoonx.battle'

	discography1 = fields.Many2one('brodoonx.discography')
	discography2 = fields.Many2one('brodoonx.discography')
	win_result = fields.Char()
	fight_date = fields.Datetime()


class battle_wizard(models.TransientModel):
	_name = 'brodoonx.battle_wizard'


	state = fields.Selection([('1','Player 1'),    ('2','Player 2'),('3','Fight')],default='1')
	discography1 = fields.Many2one('brodoonx.discography',string="Player 1")
	discography2 = fields.Many2one('brodoonx.discography',string="Player 2")
	win_result = fields.Char(compute="_calculate_win_result")
	fight_date = fields.Datetime(default=lambda self: fields.Datetime.now())


	@api.model
	def action_battle_wizard(self):
		action = self.env.ref('brodoonx.action_battle_wizard').read()[0]
		return action

	@api.depends('discography1','discography2')
	def _calculate_win_result(self):
		if self.discography1.reputation > self.discography2.reputation:
			self.win_result = "Player 1 Win"
		else:
			self.win_result = "Player 2 Win"

	def next(self):
		if self.state == '1':
			self.state = '2'
		elif self.state == '2':
			self.state = '3'
		return {
			'type': 'ir.actions.act_window',
			'res_model': self._name,
			'res_id': self.id,
			'view_mode': 'form',
			'target': 'new',
		}

	def previous(self):
		if self.state == '2':
			self.state = '1'
		elif self.state == '3':
			self.state = '2'
		
		return {
			'type': 'ir.actions.act_window',
			'res_model': self._name,
			'res_id': self.id,
			'view_mode': 'form',
			'target': 'new',
		}

	def create_battle(self):
		for battle in self:
			battle.env['brodoonx.battle'].create({'discography1':battle.discography1.id ,
												'discography2':battle.discography2.id ,
												'win_result':battle.win_result ,
												'fight_date':battle.fight_date})
			print("Battle -> ",battle)