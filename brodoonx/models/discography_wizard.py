from odoo import models, fields, api

class discography_wizard(models.TransientModel):
    _name = 'brodoonx.discography_wizard'

    name = fields.Char()
    state = fields.Selection([('1','General Info'),    ('2','Add Artists')],default='1')
    budget = fields.Float(digits=(20,2) , default=200 , required=True)
    reputation = fields.Float()
    owner = fields.Many2one(comodel_name='res.partner', required=True, ondelete='cascade', help='The owner of the discography')
    singers = fields.Many2many(comodel_name='brodoonx.artist', # El model en el que es relaciona
                            relation='singer_artists', # (opcional) el nom del la taula en mig
                            column1='discography_wizard', # (opcional) el nom en la taula en mig de la columna d'aquest model
                            column2='singer')  # (opcional) el nom de la columna de l'altre model.
    producers = fields.Many2many(comodel_name='brodoonx.artist', # El model en el que es relaciona
                            relation='producer_artists', # (opcional) el nom del la taula en mig
                            column1='discography_wizard', # (opcional) el nom en la taula en mig de la columna d'aquest model
                            column2='producer')  # (opcional) el nom de la columna de l'altre model.
    # singers = fields.Many2many(comodel_name='brodoonx.artist' ,help='List of the singers that are working for this discography')
    # producers = fields.Many2many(comodel_name='brodoonx.artist' ,help='List of the producers that are working for this discography')
    songs = fields.One2many('brodoonx.song', 'discography')
    country = fields.Many2one('brodoonx.country')
    singers_available = fields.Many2many('brodoonx.artist_transient', compute="_get_singers_available")
    producers_available = fields.Many2many('brodoonx.artist_transient', compute="_get_producers_available")





    def _get_singers_available(self):
        artists = self.env['brodoonx.artist_transient']
        singers_available = self.env['brodoonx.artist'].search([('type_artist','=','sing')])

        for singer in singers_available:
            if len(singer.discography) == 0:
                artists = artists + self.env['brodoonx.artist_transient'].create({'artist': singer.id})
            
        self.singers_available = artists

    def _get_producers_available(self):
        artists = self.env['brodoonx.artist_transient']
        producers_available = self.env['brodoonx.artist'].search([('type_artist','=','prod')])

        for producer in producers_available:
            if len(producer.discography) == 0:
                artists = artists + self.env['brodoonx.artist_transient'].create({'artist': producer.id})
            
        self.producers_available = artists



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

    @api.model
    def action_discography_wizard(self):
        action = self.env.ref('brodoonx.action_discography_wizard').read()[0]
        return action

    def next(self):
        if self.state == '1':
            self.state = '2'
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
       
        return {
            'type': 'ir.actions.act_window',
            'res_model': self._name,
            'res_id': self.id,
            'view_mode': 'form',
            'target': 'new',
        }

    def create_discography(self):
            
            # for artist in self.singers:
            #     print('Cantante Nombre -> ',artist.name,' ID Cantante -> ',artist.id)
            # print('ANTES DEL CREATE')
            # print('SELF.SINGERS.ID ======',self.singers.ids)
            # print('SELF.SINGERS.IDS ======',self.singers.ids)
            # print('SELF.PRODUCERS.ID ======',self.producers.id)
            # print('SELF.PRODUCERS.IDS ======',self.producers.ids)
            # disco = self.env['brodoonx.discography'].browse(self.env['brodoonx.discography'].search([('name', '=', 'Mueva Records')]))


            # for singer in self.singers:
            #     artist = self.env['brodoonx.artist'].browse(singer)
            #     if artist:
            #         is_same = True
            #         print('ID-COINCIDE ',is_same, 'ID Artista -> ',artist.id.id ,' ID Artista Transient -> ',singer.id)
            #     else:
            #         is_same = False
            #         print('ID-COINCIDE ',is_same, 'ID Artista -> ',artist ,' ID Artista Transient -> ',singer.id)
            

            disco = self.env['brodoonx.discography'].create({
                'name':self.name ,
                'reputation':self.reputation,
                'budget':self.budget ,
                'owner':self.owner.id,
                'singers':self.singers.ids,
                'producers':self.producers.ids,
                'country':self.country.id
            })
            for singer in self.singers:
                singer.write({'discography': disco.id})
            
            for producer in self.producers:
                producer.write({'discography': disco.id})
            
            return {
                'name': 'Brodoonx Discography',
                'type': 'ir.actions.act_window',
                'res_model': 'brodoonx.discography',
                'res_id': disco.id,
                'view_mode': 'form',
                'target': 'current'
            }


class artist_transient(models.TransientModel):
    _name = 'brodoonx.artist_transient'

    artist = fields.Many2one('brodoonx.artist')
    avatar = fields.Image(related='artist.image')

    def select(self):
        wizard = self._context.get('discography_wizard_context')
        wizard = self.env['brodoonx.discography_wizard'].browse(wizard)
        print(wizard,'*************************')
        if self.artist.type_artist == "sing":
            wizard.write({'singers': [(4,self.artist.id,0)]})
        if self.artist.type_artist == "prod":
            wizard.write({'producers': [(4,self.artist.id,0)]})
        return {
            'name': 'Brodoonx discography wizard action',
            'type': 'ir.actions.act_window',
            'res_model': wizard._name,
            'res_id': wizard.id,
            'view_mode': 'form',
            'target': 'new',
            'context': wizard._context
        }


    
