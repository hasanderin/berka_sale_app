from odoo import fields, models


class AccountMove(models.Model):
    _inherit = 'account.move'

    def get_sale_id(self):
        order_id = self.env['sale.order'].search([('invoice_ids', 'in', [self.id])])
        return order_id
