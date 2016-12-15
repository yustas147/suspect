# -*- coding: utf-8 -*-
# © 2015 OpenSynergy Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from openerp import models, fields


class res_company(models.Model):
    """override company to add liablity account"""
    _inherit = 'res.company'
    _name = 'res.company'

    liability_ids = fields.Many2many(
        string='Liabilities',
        comodel_name='account.account',
        relation='rel_company_2_liablity_acc',
        column1='company_id',
        column2='account_id',
        )
