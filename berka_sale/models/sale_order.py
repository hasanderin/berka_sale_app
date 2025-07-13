from odoo import models, _, api
from odoo.exceptions import UserError


class SaleOrder(models.Model):
    _inherit = 'sale.order'

    def action_confirm(self):
        for rec in self:
            partner_id = rec.partner_id
            missing_fields = []
            fields_to_check = [
                ('name', _('Name')),
                ('street', _('Address')),
                ('city', _('City')),
                ('state_id', _('State')),
                ('zip', _('ZIP Code')),
                ('country_id', _('Country')),
                ('vat', 'VAT Number'),
                ('tax_office_id', _('Tax Office')),
                ('user_id', _('Salesperson')),
                ('property_payment_term_id', _('Payment Term')),
                ('property_delivery_carrier_id', _('Delivery Method')),
            ]
            for field, label in fields_to_check:
                if not getattr(partner_id, field):
                    missing_fields.append(label)
            if missing_fields:
                raise UserError(_("The following partner fields are required to create the order:\n- ") + "\n- ".join(missing_fields))
        return super().action_confirm()



    @api.onchange('partner_id')
    def onchange_partner_id(self):
        self.carrier_id = self.partner_id.property_delivery_carrier_id
        res = super(SaleOrder, self).onchange_partner_id()
        return res
