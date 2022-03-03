# -*- coding: utf-8 -*-
{
    'name': "brodoonx",

    'summary': """
        Short (1 phrase/line) summary of the module's purpose, used as
        subtitle on modules listing or apps.openerp.com""",

    'description': """
        Long description of module's purpose
    """,

    'author': "My Company",
    'website': "http://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/14.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base','mail','product','sale'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/player.xml',
        'views/templates.xml',
        'views/song.xml',
        'views/musical_genre.xml',
        'views/discography_wizard.xml',
        'views/discography.xml',
        'views/country.xml',
        'views/artist.xml',
        'views/events.xml',
        'crons/crons.xml',
        'views/battle.xml',
        'views/views.xml',
        'views/premium.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
        # 'demo/players.xml',
        'demo/countries.xml',
        # 'demo/discographies.xml',
        'demo/musical_genres.xml',
        # 'demo/artists.xml',
        # 'demo/songs.xml',
    ],
}
