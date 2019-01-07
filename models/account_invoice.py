# -*- coding: utf-8 -*-
from odoo import api, fields, models, _
from odoo.exceptions import Warning


class AccountInvoice(models.Model):
    _inherit = "account.invoice"

    is_affaire_id             = fields.Many2one('is.affaire', 'Affaire')
    is_date_paiement          = fields.Date('Date paiement')
    is_amount_untaxed_percent = fields.Float(compute='_compute_amount_untaxed_percent', string='Total HT(%)')


    def _compute_amount_untaxed_percent(self, field_names=None):
        res = {}
        for obj in self:
            res[obj.id] = {}
            res[obj.id]['is_amount_untaxed_percent'] = obj.amount_untaxed
            for k, v in res[obj.id].items():
                setattr(obj, k, v)
        return res


    @api.model
    def read_group(self, domain, fields, groupby, offset=0, limit=None, orderby=False, lazy=True):
        """
            Inherit read_group to calculate the sum of the non-stored fields, as it is not automatically done anymore through the XML.
        """
        res = super(AccountInvoice, self).read_group(domain, fields, groupby, offset=offset, limit=limit, orderby=orderby, lazy=lazy)
        for idx, item in enumerate(res):
            print(idx,item)
            res[idx]['is_amount_untaxed_percent']=123
        return res


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




