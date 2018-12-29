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



