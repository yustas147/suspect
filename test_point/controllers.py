# -*- coding: utf-8 -*-
from openerp import http

# class TestPoint(http.Controller):
#     @http.route('/test_point/test_point/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/test_point/test_point/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('test_point.listing', {
#             'root': '/test_point/test_point',
#             'objects': http.request.env['test_point.test_point'].search([]),
#         })

#     @http.route('/test_point/test_point/objects/<model("test_point.test_point"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('test_point.object', {
#             'object': obj
#         })