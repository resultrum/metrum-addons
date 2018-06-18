# -*- coding: utf-8 -*-
# Copyright 2018 Jonathan Nemry <jonathan.nemry@metrum.lu>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

{
    'name': 'Account Invoice Delivery Address',
    'summary': """
        If you have to invoice a customer about another address:
        show a delivery address into the invoice too""",
    'version': '10.0.1.0.0',
    'license': 'AGPL-3',
    'author': 'Jonathan Nemry <jonathan.nemry@metrum.lu>,'
    'Odoo Community Association (OCA)',
    'website': 'https://metrum.lu',
    'depends': [
        'base',
        'account',
        'sale',
    ],
    'data': [
        'views/account_invoice.xml',
    ],
    'demo': [
    ],
}
