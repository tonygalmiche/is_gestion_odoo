# -*- coding: utf-8 -*-
from odoo import api, fields, models, _
from odoo.exceptions import Warning


class AccountInvoice(models.Model):
    _inherit = "account.invoice"

    is_affaire_id    = fields.Many2one('is.affaire', 'Affaire')
    is_date_paiement = fields.Date('Date paiement')


    @api.multi
    def calculer_tva(self):
        for obj in self:
            print(obj)
            obj.compute_taxes()


    @api.multi
    def acceder_facture_action(self, vals):
        for obj in self:

            res= {
                'name': 'Facture',
                'view_mode': 'form',
                'view_type': 'form',
                'res_model': 'account.invoice',
                'res_id': obj.id,
                'type': 'ir.actions.act_window',
                'view_id': self.env.ref('account.invoice_form').id,
                'domain': [('type','=','out_invoice')],
            }
            return res




