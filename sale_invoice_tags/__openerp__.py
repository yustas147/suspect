#########################################################################################
#
#    OpenERP, Open Source Management Solution
#    Copyright (C) 2004-TODAY OpenERP SA (<http://www.odoo.com>)
#    Copyright (C) 2014-TODAY Probuse Consulting Service Pvt. Ltd. (<http://probuse.com>).
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
#########################################################################################

{
    'name' : 'Add Invoice Tags',
    'version': '1.0',
    'license': 'AGPL-3',
    'author': 'Probuse Consulting Service Pvt. Ltd.',
    'category' : 'Accounting & Finance',
    'website': 'https://www.probuse.com',
    'description': ''' 
This module enables the feature to add tags on invoice form and allow user to pass tags from sales order to invoice.
Supporting for Invoice from Sales order / Advance Invoice / Percentage bases invoice from Sales Order.
  ''',
    'depends':['sale_crm', 'account'],
    'data' : [
        'security/ir.model.access.csv',
        'invoice_view.xml',
              ],
    'installable':True,
    'auto_install':False

}

# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:

