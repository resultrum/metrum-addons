# -*- coding: utf-8 -*-
# Copyright 2018 Jonathan Nemry <jonathan.nemry@metrum.lu>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import fields, models


class AccountInvoice(models.Model):

    _inherit = 'account.invoice'

    partner_shipping_id = fields.Many2one(
        comodel_name='res.partner',
        string='Delivery Address')
