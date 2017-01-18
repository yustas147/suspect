# -*- coding: utf-8 -*-

from openerp import models, fields, api


# class test_point(models.Model):
#     _name = 'test_point.test_point'

#     name = fields.Char()

class test_point(models.Model):
    #_name = 'new_module.new_module'
    _inherit = 'tasks.task'

    #story = fields.Char()
    #text_ids = fields.One2many(comodel_name="name", inverse_name="in_name", string="Text", required=False, )
    #st = fields.Float(string="String",  required=False, )
    story = fields.Selection(string="Story Point", selection=[('s05', '0.5'), ('s1', '1'), ('s2', '2'), ('s3', '3'),
                                                              ('s3', '3'), ('s5', '5'), ('s8', "8"),
                                                              ('s13', '13'), ('s20', '20'),
                                                              ('s40', '40'), ('s100', "100"), ], required=False, )
