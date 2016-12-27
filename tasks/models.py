# -*- coding: utf-8 -*-

from openerp import models, fields, api

class task(models.Model):
    _name = 'tasks.task'

    name = fields.Char(string="Title", required=True)
    description = fields.Text()

    manager_id = fields.Many2one('res.partner', ondelete='set null', string="Manager", index=True)
    responsible_id = fields.Many2one('res.users', ondelete='set null', string="Responsible", index=True)

    start_date = fields.Date()
    finish_date = fields.Date()
