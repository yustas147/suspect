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

from openerp import fields, models, api, _

class account_invoice(models.Model):
    _inherit = 'account.invoice'
    
    categ_ids = fields.Many2many('crm.case.categ', 'sale_invoice_category_rel', 'invoice_id', 'category_id', 'Sale Tags', \
            domain="['|', ('section_id', '=', section_id), ('section_id', '=', False), ('object_id.model', '=', 'crm.lead')]", context="{'object_name': 'crm.lead'}")

class sale_order(models.Model):
    _inherit = "sale.order"
    
    @api.v7
    def _prepare_invoice(self, cr, uid, order, lines, context=None):
        res = super(sale_order, self)._prepare_invoice(cr, uid, order, lines, context=context)
        tags_ids = []
        if order.categ_ids:
            tags_ids = [tag.id for tag in order.categ_ids]
            res.update({'categ_ids': [(6, 0, tags_ids)]})
        return res

class sale_advance_payment_inv(models.TransientModel):
    _inherit = "sale.advance.payment.inv"
    
    @api.multi
    def _prepare_advance_invoice_vals(self):
        res = super(sale_advance_payment_inv, self)._prepare_advance_invoice_vals()
        tags_ids = []
        for sale in res:
            sale_data = self.env['sale.order'].browse(sale[0])
            if sale_data.categ_ids:
                tags_ids = [tag.id for tag in sale_data.categ_ids]
                sale[1].update({'categ_ids': [(6, 0, tags_ids)]})
        return res
    
# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:

