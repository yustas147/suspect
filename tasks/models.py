# -*- coding: utf-8 -*-

from openerp import models, fields, api

class task(models.Model):
    _name = 'tasks.task'

    name = fields.Char(string="Title", required=True)
    description = fields.Text('Description', size=128, required=True,
                              select=True, read=['project.group_project_user']) #groups='project.group_project_user', readonly=1

    responsible_id = fields.Many2one('res.users', ondelete='set null', string="Responsible", index=True)

    start_date = fields.Date()
    finish_date = fields.Date()
