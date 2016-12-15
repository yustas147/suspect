# -*- coding: utf-8 -*-
##############################################################################
#
#    OpenERP, Open Source Management Solution
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################

{
    'name': 'Graph Widget for Kanban',
    'category': 'Enterprise',
    'description': """
This widget allows to display graph using NVD3 library.
""",
    'version': '1.0',
    'author' : 'Jonathan Bravo @jbravot',
    'complexity': 'normal',
    'website': 'http://jbravot.github.io/portafolio/',
    'depends': ['web_graph','web_kanban'],
    'data' : [
        'views/web_kanban_graph.xml',
    ],
    'qweb': [
    ],
    'auto_install': False,
}
