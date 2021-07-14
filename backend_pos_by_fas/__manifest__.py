# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.
{

     'name': "Backend POS",
     'author': "Fasil",
     'version': '0.1',
     'sequence': -1,
     'website': 'https://www.facebook.com/fasilwdr/',
     'summary': """
             Create POS Orders from Backend""",
     'description': """
             
         """,
     'depends': ['base','point_of_sale'],
     'data': [
         'views/pos_config.xml',
         'views/pos_session.xml',
         'views/pos_order.xml',
         'views/views.xml',
         'views/menu_actions.xml',
     ],
    'demo': [],

    'installable': True,
    'application': True,
    'auto_install': False,
    'images': ['static/description/banner.gif'],

}
